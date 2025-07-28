---
Created date: 2025-02-07 00:41
Modified date: 2025-07-27 22:48
---
# Loon 规则类型和内置策略

## 规则类型

### 规则集

**RULE-SET**
- 匹配规则集内容。规则集的内容需包含规则类型。（兼容仅包含 IP 地址且不带规则类型的规则集）
```
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Apple/Apple.list
```

**DOMAIN-SET**
- 匹配域名集内容。域名集的内容不包含规则类型。
```
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Apple/Apple_Domain.list
```

### 域名类规则

**DOMAIN**
- 匹配整个域名
```
DOMAIN,google.com,proxy
```

**DOMAIN-SUFFIX**
- 匹配域名后缀，例如 `apple.com` 可以匹配 `icloud.apple.com`，`www.apple.com`，但是不能够匹配 `app-apple.com`
```
DOMAIN-SUFFIX,apple.com,proxy
```

**DOMAIN-KEYWORD**
- 域名关键词匹配
```
DOMAIN-KEYWORD,apple,proxy
```

### IP 类规则

> no-resolve 可选: 当设置 no-resolve 后表示该规则只会对目标地址类型是 IP 类型的生效，域名类型的目标地址不会进行 dns 解析后再去匹配这个规则，为了防止域名类的目标地址做无效的 DNS 请求，请在给纯 IP 类型的域名制定的规则中加上 no-resolve。

**IPV4**
```
IP-CIDR,118.89.204.198/32,no-resolve
```

**IPV6**
```
IP-CIDR6,2402:4e00:1200:ed00:0:9089:6dac:96b6/128
```

**GEOIP**
- 根据 mmdb 查询的 IP 国家地区进行匹配
```
geoip,cn,DIRECT
```

**IP-ASN**
- 根据 IP 服务商进行匹配
```
IP-ASN,4134,DIRECT,no-resolve
```

### HTTP 类规则

> HTTP 类型的规则只会对 HTTP、HTTPS 类型的请求进行匹配

**URL-REGEX**
- 根据提供的正则表达式对请求的 url 进行匹配
```
URL-REGEX,^http://google\.com,PROXY
```

**USER-AGENT**
- 根据请求 header 中的 user-agent 进行匹配，支持通配符
```
USER-AGENT,Apple*,DIRECT
```

### 端口规则

> 根据请求的源端口或者目标端口进行匹配（3.1.7+）
> 表示特定的某个端口，如 `DEST-PORT,443,DIRECT`
> 表示端口闭区间，如 `DEST-PORT,80-443,DIRECT`
> 使用>, <, <=, >= 表示一个无穷区间，如 `DEST-PORT,>=443,DIRECT`

**SRC-PORT**
```
SRC-PORT,443,DIRECT
SRC-PORT,80-443,DIRECT
SRC-PORT,>=443,DIRECT
```

**DEST-PORT**
```
DEST-PORT,443,DIRECT
DEST-PORT,80-443,DIRECT
DEST-PORT,>=443,DIRECT
```

### 协议类规则

> 根据请求的协议类型进行匹配（3.1.7+），目前支持 `HTTP/HTTPS/TCP/QUIC/STUN/UDP`

**PROTOCOL**
```
PROTOCOL,STUN,REJECT
```

### 逻辑规则

> 使用或、与、非逻辑将多个规则合并成一个规则（3.1.7+）
- 如果逻辑规则里面有域名有 IP，尽量把 IP 的子规则放在后面，防止不必要的 DNS 查询

**AND**
- 多个子规则同时满足时才会匹配
```
AND,((子规则),(子规则)),PolicyName
AND,((DOMAIN-SUFFIX,axample),(DEST-PORT,443),(GEOIP,CN)),DIRECT
```

**OR**
- 子规则满足一个时匹配
```
OR,((子规则),(子规则)),PolicyName
OR,((DOMAIN-SUFFIX,axample),(DEST-PORT,443),(GEOIP,CN,no-resolve)),DIRECT
```

**NOT**
- 子规则不满足时匹配，只有有一个子规则
```
NOT,((子规则)),PolicyName
NOT,((AND,((DOMAIN-SUFFIX,axample),(DEST-PORT,443),(GEOIP,CN)))),DIRECT
```

### Final

- Final 表示最后、兜底，即在没有匹配到配置的规则后，使用 Final 指定的策略
```
final,DIRECT
```

## 内置策略

### 直连

- DIRECT：直连。连接不经过任何代理服务器。

### 拒绝

- REJECT：拒绝 返回 200 响应空的响应体)
- REJECT-IMG：拒绝 返回 200 和一个 1px GIF 的响应体)
- REJECT-DICT：拒绝 返回 200 和内容为空的 JSON 的响应体)
- REJECT-ARRY ：拒绝 返回 200 和一个内容为空的 JSON 数组)
- REJECT-DROP：拒绝 拒绝并丢弃请求，且不会返回任何响应。因为部分程序有着十分暴力的重试逻辑，连接失败后会立刻进行重试，导致请求风暴)

### 代理

- 除此之外，规则策略还可以选择「代理分组」、「订阅名称」、「分组」、「节点」。

## reference

- [规则 | Powerful Network Toolbox for iOS & tvOS](https://nsloon.app/docs/category/%E8%A7%84%E5%88%99)
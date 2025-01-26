## Clash.Meta 规则类型和规则策略
> data: 未知

> updata: 20250126

## 使用规则
```
rules:
  - 规则类型,字段,规则策略
  - DOMAIN-SUFFIX,google.com,DIRECT
```

## Clash.Meta 规则类型

### 规则集

**RULE-SET**
- 引用规则集合，需配置[rule-providers](https://wiki.metacubex.one/config/rule-providers/)

### 域名规则

**DOMAIN**
- 匹配完整域名

**DOMAIN-SUFFIX**
- 匹配域名后缀
```
rules:
  - DOMAIN-SUFFIX,google.com,DIRECT # 匹配 www.google.com/mail.google.com 和google.com,但不匹配 content-google.com.
```

**DOMAIN-KEYWORD**
- 使用域名关键字匹配

**DOMAIN-REGEX/URL-REGEX**
- 域名正则表达式匹配

**GEOSITE**
- 匹配 Geosite 内的域名，部分内容参考 v2fly/domain-list-community
```
rules:
  - GEOSITE,category-ads-all,REJECT
  - GEOSITE,geolocation-cn,DIRECT
  - GEOSITE,geolocation-!cn,PROXY
```

### IP规则

**IP-CIDR & IP-CIDR6**
- 匹配 IP 地址范围，IP-CIDR和IP-CIDR6效果是一样的，IP-CIDR6只是一个别名

**IP-SUFFIX** 
- 匹配 IP 后缀范围

**IP-ASN** 
- 匹配 IP 所属 ASN

**GEOIP** 
- 匹配 IP 所属国家代码
```
rules:
  - GEOIP,telegram,PROXY,no-resolve
  - GEOIP,private,DIRECT,no-resolve
  - GEOIP,cn,DIRECT
```

**SRC-GEOIP** 
- 匹配来源 IP 所属国家代码

**SRC-IP-ASN** 
- 匹配来源 IP 所属 ASN

**SRC-IP-CIDR** 
- 匹配来源 IP 地址范围

**SRC-IP-SUFFIX**
- 匹配来源 IP 后缀范围

### 端口规则

**DST-PORT** 
- 匹配请求目标端口范围

**SRC-PORT** 
- 匹配请求来源端口范围

**IN-PORT** 
- 匹配入站端口,可用端口范围

### 进程规则

**PROCESS-PATH** 
- 使用完整进程路径匹配

**PROCESS-PATH-REGEX** 
- 使用进程路径正则表达式匹配

**PROCESS-NAME** 
- 使用进程匹配，在Android平台可以匹配包名

**PROCESS-NAME-REGEX** 
- 使用进程名称正则表达式匹配，在Android平台可以匹配包名

### 其他规则

**IN-TYPE**
- 匹配入站类型

**IN-USER**
- 匹配入站用户名，支持使用 / 分隔多个用户名

**IN-NAME**
- 匹配入站名称

**UID**
- 匹配 Linux USER ID

**NETWORK**
- 匹配 tcp 或者 udp

**DSCP**
- 匹配 DSCP 标记 (仅限 tproxy udp 入站)

### 逻辑规则

 **AND & OR & NOT**
- 逻辑规则，需要注意括号的使用

**SUB-RULE**
- 匹配至子规则,需要注意括号的使用

### 兜底规则

**MATCH**
- 匹配所有请求，无需条件

### 附加参数

**no-resolve**
- 仅支持关于 `目标IP` 的规则
- 域名开始匹配关于 `目标IP` 规则时，mihomo 将触发 dns 解析来检查域名的 `目标IP` 是否匹配规则，可以选择 `no-resolve` 选项以跳过 dns 解析
- 如在更早的匹配中触发了 dns 解析，则依旧会匹配到添加了 `no-resolve` 选项的 `目标IP` 类规则

**src**
- 仅支持关于 `目标IP` 的规则
- 将 `目标IP` 匹配转为 `来源IP` 匹配

## reference
- [路由规则 - 虚空终端 Docs](https://wiki.metacubex.one/config/rules/#domain-regex)
---
Created date: 2025-02-07 00:41
Modified date: 2025-08-03 22:40
---
# Quantumult_X 规则类型和内置策略

## 规则类型

### IP 规则

**IP-CIDR**

```
IP-CIDR,127.0.0.0/8,policy(你的策略组)
```

**IP6-CIDR**

```
IP6-CIDR,2620:0:2d0:200::7/32,policy
```

**GEOIP(IP 地理位置 (国家代码)}**

```
GEOIP,CN,DIRECT
```

**IP-ASN(通过 IP 自治系统编号)**

```
IP-ASN,714
```

### 域名规则

> 可以用 “DOMAIN”

HOST(域名)

```
HOST,www.google.com,policy
```

HOST-SUFFIX(域名后缀)

```
HOST-SUFFIX,youtube.com,policy
```

HOST-KEYWORD(域名关键字)

HOST-WILDCARD(域名通配符)

### 其他规则

- USER-AGENT

### 兜底规则

- FINAL

## 内置策略

## reference
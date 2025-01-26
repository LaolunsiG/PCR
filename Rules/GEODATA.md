---
modified by: XiaoE
date: 2025-01-17 15:18
updated: 2025-01-27 00:05
---
# GEODATA
- 比较重要吧，不懂是什么东西
- 地理位置相关的数据，通常用于根据地理位置管理网络流量。

**DAT 和 MMDB 文件**
- 是存储 IP 地址和地理位置信息的数据文件，其中 MMDB 是一种更高效的格式，广泛应用于需要快速查询和精确地理位置信息的场景中。

## GEOIP
- 基于 IP 地址的地理位置数据库。主要用于根据 IP 地址的地理位置来路由或限制流量。

### mmdb
- [Hackl0us](https://github.com/Hackl0us/GeoIP2-CN/) 
	- 🇨🇳 小巧精悍、准确、实用 GeoIP2 数据库 🇨🇳
```
https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb
```
- [NobyDa](https://github.com/NobyDa/geoip) 
	- 用于代理工具的 GeoIPCN 的增强版。
```
https://raw.githubusercontent.com/NobyDa/geoip/release/Private-GeoIP-CN.mmdb
```
- [Loyalsoldier](https://github.com/Loyalsoldier/geoip) 
	- 🌚 🌍 🌝 GeoIP 规则文件加强版，同时支持定制 V2Ray dat 格式路由规则文件 geoip.dat 和 MaxMind mmdb 格式文件 Country.mmdb。
```
https://raw.githubusercontent.com/Loyalsoldier/geoip/release/Country-only-cn-private.mmdb
```

### dat
- [Loyalsoldier](https://github.com/Loyalsoldier/v2ray-rules-dat) 
	- 🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，兼容 Shadowsocks-windows、Xray-core、Trojan-Go、leaf 和 hysteria。
```
https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geoip.dat
```

## GEOSITE
- 基于域名的地理位置和类别分类数据库。主要用于根据域名类别来路由或管理流量。

### dat
- [Loyalsoldier](https://github.com/Loyalsoldier/v2ray-rules-dat) 
	- 🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，兼容 Shadowsocks-windows、Xray-core、Trojan-Go、leaf 和 hysteria。
```
https://raw.githubusercontent.com/Loyalsoldier/v2ray-rules-dat/release/geosite.dat
```

## ASN
- [Loon0x00](https://gitlab.com/Loon0x00/loon_data) 
	- Loon mmdb and default rule files
```
https://gitlab.com/Loon0x00/loon_data/-/raw/main/geo/GeoLite2-ASN.mmdb
```

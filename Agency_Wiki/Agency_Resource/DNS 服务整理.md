---
Created date: 2025-05-04 11:11
Modified date: 2025-08-04 09:30
---
# DNS 服务整理

## 国内 DNS 服务

| 服务提供商      | DNS 类型 | 服务 1                                                                                                                           | 服务 2                                                                 |
| ---------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 阿里 (Ali)DNS | UDP    | 223.5.5.5                                                                                                                     | 233.6.6.6                                                           |
| 阿里 (Ali)DNS | DOH    | https://223.5.5.5/dns-query<br>https://dns.alidns.com/dns-query                                                               | https://223.6.6.6/dns-query                                         |
| 阿里 (Ali)DNS | DOT    |                                                                                                                               | tls://dns.alidns.com:853                                            |
| 腾讯 DNS      | UDP    | 119.29.29.29 <br>119.28.28.28                                                                                                 | 182.254.116.116<br>182.254.118.118                                  |
| 腾讯 DNS      | DOH    | https://doh.pub/dns-query<br>https://1.12.12.12/dns-query<br>https://120.53.53.53/dns-query <br>https://sm2.doh.pub/dns-query |                                                                     |
| 腾讯 DNS      | DOT    |                                                                                                                               | tls://dot.pub:853<br>tls://1.12.12.12:853<br>tls://120.53.53.53:853 |

## 国外 DNS 服务

> 国内可以直连使用的 DNS 服务

| 服务提供商      | DNS 类型 | 服务 1                                                                                 | 服务 2                                       | 服务 3                                |     |
| ---------- | ------ | ----------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------- | --- |
| 台湾 Quad 101 | UDP    | 101.101.101.101                                                                     | 101.102.103.104                           |                                    |     |
|            | DOH    | https://dns.twnic.tw/dns-query - 不可用                                                |                                           |                                    |     |
| Google     | udp    | 8.8.8.8                                                                             | 8.8.4.4                                   |                                    |     |
|            | DOH    | https://dns.google/dns-query - 不可用                                                  |                                           | https://dns64.dns.google/dns-query |     |
|            | DOT    |                                                                                     | tls://8.8.4.4:853<br>tls://dns.google:853 |                                    |     |
|            | DOQ    |                                                                                     |                                           |                                    |     |
| Cloudflare | UDP    | 1.1.1.1                                                                             | 1.0.0.1                                   |                                    |     |
|            | DOH    | - https://1.1.1.1/dns-query<br>- https://cloudflare-dns.com/dns-query               | - https://1.0.0.1/dns-query               |                                    |     |
|            | DOT    | tls://one.one.one.one:853 - 不可用<br>tls://1dot1dot1dot1.cloudflare-dns.com:853 - 不可用 |                                           |                                    |     |
| 其他私人服务     | DOH    | https://doh.apad.pro/dns-query - 不可用                                                |                                           |                                    |     |

## reference

| DNS 服务资源                                                                                                                 | 介绍   |
| ------------------------------------------------------------------------------------------------------------------------ | ---- |
| https://dns.iui.im/#LOG                                                                                                  |      |
| [国内好用的 DNS 列表](https://blog.lindexi.com/post/%E5%9B%BD%E5%86%85%E5%A5%BD%E7%94%A8%E7%9A%84-DNS-%E5%88%97%E8%A1%A8.html) |      |
| https://dns.icoa.cn/                                                                                                     | 需要代理 |
| https://www.zyha.cn/select-a-good-public-dns-in-2024/                                                                    |      |
| https://config.net.cn/tools/Dns.html                                                                                     |      |
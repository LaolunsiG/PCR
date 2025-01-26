---
modified by: XiaoE
date: 2025-01-17 15:18
updated: 2025-01-27 00:04
---

# 国外 DNS 服务

## 国内可以直连使用的 DNS 服务

| 服务提供商      | DNS 类型 | 服务1                                                                                 | 服务2                                       | 服务3                                |     |
| ---------- | ------ | ----------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------- | --- |
| 台湾Quad 101 | UDP    | 101.101.101.101                                                                     | 101.102.103.104                           |                                    |     |
|            | DOH    | https://dns.twnic.tw/dns-query - 不可用                                                |                                           |                                    |     |
| Google     | udp    | 8.8.8.8                                                                             | 8.8.4.4                                   |                                    |     |
|            | DOH    | https://dns.google/dns-query - 不可用                                                  |                                           | https://dns64.dns.google/dns-query |     |
|            | DOT    |                                                                                     | tls://8.8.4.4:853<br>tls://dns.google:853 |                                    |     |
|            | DOQ    |                                                                                     |                                           |                                    |     |
| Cloudflare | UDP    | 1.1.1.1                                                                             | 1.0.0.1                                   |                                    |     |
|            | DOH    | - https://1.1.1.1/dns-query<br>- https://cloudflare-dns.com/dns-query               | - https://1.0.0.1/dns-query               |                                    |     |
|            | DOT    | tls://one.one.one.one:853 - 不可用<br>tls://1dot1dot1dot1.cloudflare-dns.com:853 - 不可用 |                                           |                                    |     |
| 其他私人服务     | DOH    | https://doh.apad.pro/dns-query - 不可用                                                |                                           |                                    |     |
 


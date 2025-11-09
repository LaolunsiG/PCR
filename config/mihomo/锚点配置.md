---
Created date: 2025-02-07 00:41
Modified date: 2025-11-09 18:48
---
# 锚点配置

## DNS 服务锚点

```yaml
# DNS 配置
# 锚点 - DNS 筛选组
## 锚点 - 国外 DoT DNS IP 服务器。无过滤
DoT_IP_NoFilter: &DoT_IP_NoFilter ['tls://94.140.14.140', 'tls://94.140.14.141', 'tls://1.1.1.1', 'tls://1.0.0.1', 'tls://8.8.8.8', 'tls://8.8.4.4', 'tls://208.67.222.2', 'tls://208.67.220.2', 'tls://9.9.9.10', 'tls://149.112.112.10', 'tls://77.88.8.1', 'tls://77.88.8.8', 'tls://[2606:4700:4700::1111]', 'tls://[2606:4700:4700::1001]', 'tls://[2606:4700:4700::64]', 'tls://[2606:4700:4700::6400]', 'tls://[2001:4860:4860::6464]', 'tls://[2001:4860:4860::64]', 'tls://[2620:0:ccc::2]', 'tls://[2620:0:ccd::2]', 'tls://[2620:fe::10]', 'tls://[2620:fe::fe:10]']
## 锚点 - 国外 DoT DNS IP 服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
DoT_IP_Safe: &DoT_IP_Safe ['tls://94.140.14.14', 'tls://94.140.15.15', 'tls://208.67.222.222', 'tls://208.67.220.220', 'tls://9.9.9.9', 'tls://149.112.112.112', 'tls://77.88.8.2', 'tls://77.88.8.88', 'tls://[2620:119:35::35]', 'tls://[2620:119:53::53]', 'tls://[2620:fe::fe]', 'tls://[2620:fe::9]']
## 锚点 - 国外 DoT DNS IP 服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
DoT_IP_Family: &DoT_IP_Family ['tls://94.140.14.15', 'tls://94.140.15.16', 'tls://208.67.222.123', 'tls://208.67.220.123', 'tls://77.88.8.3', 'tls://77.88.8.7', 'tls://[2620:119:35::123]', 'tls://[2620:119:53::123]']
## 锚点 - 国外 DoH DNS IP 服务器。无过滤
DoH_IP_NoFilter: &DoH_IP_NoFilter ['https://94.140.14.140/dns-query', 'https://94.140.14.141/dns-query', 'https://1.1.1.1/dns-query', 'https://1.0.0.1/dns-query', 'https://8.8.8.8/dns-query', 'https://8.8.4.4/dns-query', 'https://208.67.222.2/dns-query', 'https://208.67.220.2/dns-query', 'https://9.9.9.10/dns-query', 'https://149.112.112.10/dns-query', 'https://77.88.8.1/dns-query', 'https://77.88.8.8/dns-query', 'https://[2606:4700:4700::1111]/dns-query', 'https://[2606:4700:4700::1001]/dns-query', 'https://[2606:4700:4700::64]/dns-query', 'https://[2606:4700:4700::6400]/dns-query', 'https://[2001:4860:4860::6464]/dns-query', 'https://[2001:4860:4860::64]/dns-query', 'https://[2620:0:ccc::2]/dns-query', 'https://[2620:0:ccd::2]/dns-query', 'https://[2620:fe::10]/dns-query', 'https://[2620:fe::fe:10]/dns-query']
## 锚点 - 国外 DoH DNS IP 服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
DoH_IP_Safe: &DoH_IP_Safe ['https://94.140.14.14/dns-query', 'https://94.140.15.15/dns-query', 'https://1.1.1.2/dns-query', 'https://1.0.0.2/dns-query', 'https://208.67.222.222/dns-query', 'https://208.67.220.220/dns-query', 'https://9.9.9.9/dns-query', 'https://149.112.112.112/dns-query', 'https://77.88.8.2/dns-query', 'https://77.88.8.88/dns-query', 'https://[2606:4700:4700::1112]/dns-query', 'https://[2606:4700:4700::1002]/dns-query', 'https://[2620:119:35::35]/dns-query', 'https://[2620:119:53::53]/dns-query', 'https://[2620:fe::fe]/dns-query', 'https://[2620:fe::9]/dns-query']
## 锚点 - 国外 DoH DNS IP 服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
DoH_IP_Family: &DoH_IP_Family ['https://94.140.14.15/dns-query', 'https://94.140.15.16/dns-query', 'https://1.1.1.3/dns-query', 'https://1.0.0.3/dns-query', 'https://208.67.222.123/dns-query', 'https://208.67.220.123/dns-query', 'https://77.88.8.3/dns-query', 'https://77.88.8.7/dns-query', 'https://[2606:4700:4700::1113]/dns-query', 'https://[2606:4700:4700::1003]/dns-query', 'https://[2620:119:35::123]/dns-query', 'https://[2620:119:53::123]/dns-query']
## 锚点 - 国外 H3 DNS IP 服务器。无过滤
H3_IP_NoFilter: &H3_IP_NoFilter ['https://94.140.14.140/dns-query#h3=true', 'https://94.140.14.141/dns-query#h3=true', 'https://1.1.1.1/dns-query#h3=true', 'https://1.0.0.1/dns-query#h3=true', 'https://8.8.8.8/dns-query#h3=true', 'https://8.8.4.4/dns-query#h3=true', 'https://[2606:4700:4700::1111]/dns-query#h3=true', 'https://[2606:4700:4700::1001]/dns-query#h3=true', 'https://[2606:4700:4700::64]/dns-query#h3=true', 'https://[2606:4700:4700::6400]/dns-query#h3=true', 'https://[2001:4860:4860::6464]/dns-query#h3=true', 'https://[2001:4860:4860::64]/dns-query#h3=true']
## 锚点 - 国外 H3 DNS IP 服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
H3_IP_Safe: &H3_IP_Safe ['https://94.140.14.14/dns-query#h3=true', 'https://94.140.15.15/dns-query#h3=true', 'https://1.0.0.2/dns-query#h3=true', 'https://[2606:4700:4700::1112]/dns-query#h3=true', 'https://[2606:4700:4700::1002]/dns-query#h3=true']
## 锚点 - 国外 H3 DNS IP 服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
H3_IP_Family: &H3_IP_Family ['https://94.140.14.15/dns-query#h3=true', 'https://94.140.15.16/dns-query#h3=true', 'https://1.1.1.3/dns-query#h3=true', 'https://1.0.0.3/dns-query#h3=true', 'https://[2606:4700:4700::1113]/dns-query#h3=true', 'https://[2606:4700:4700::1003]/dns-query#h3=true']

## 锚点 - 国外 DoT DNS 域名服务器。无过滤
DoT_Domain_NoFilter: &DoT_Domain_NoFilter ['tls://dns-unfiltered.adguard.com', 'tls://one.one.one.one', 'tls://1dot1dot1dot1.cloudflare-dns.com', 'tls://dns64.cloudflare-dns.com', 'tls://private.canadianshield.cira.ca', 'tls://dns.google', 'tls://dns64.dns.google', 'tls://sandbox.opendns.com', 'tls://dns-nosec.quad9.net']
## 锚点 - 国外 DoT DNS 域名服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
DoT_Domain_Safe: &DoT_Domain_Safe ['tls://dns.adguard.com', 'tls://security.cloudflare-dns.com', 'tls://protected.canadianshield.cira.ca', 'tls://dns.opendns.com', 'tls://dns.umbrella.com', 'tls://dns.quad9.net']
## 锚点 - 国外 DoT DNS 域名服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
DoT_Domain_Family: &DoT_Domain_Family ['tls://family-filter-dns.cleanbrowsing.org', 'tls://adult-filter-dns.cleanbrowsing.org', 'tls://security-filter-dns.cleanbrowsing.org', 'tls://dns-family.adguard.com', 'tls://family.cloudflare-dns.com', 'tls://family.canadianshield.cira.ca', 'tls://familyshield.opendns.com']
## 锚点 - 国外 DoH DNS 域名服务器。无过滤
DoH_Domain_NoFilter: &DoH_Domain_NoFilter ['https://dns-unfiltered.adguard.com/dns-query', 'https://one.one.one.one/dns-query', 'https://1DoH1DoH1DoH1.cloudflare-dns.com/dns-query', 'https://dns64.cloudflare-dns.com/dns-query', 'https://private.canadianshield.cira.ca', 'https://dns.google/dns-query', 'https://dns64.dns.google/dns-query', 'https://sandbox.opendns.com/dns-query', 'https://dns-nosec.quad9.net/dns-query']
## 锚点 - 国外 DoH DNS 域名服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
DoH_Domain_Safe: &DoH_Domain_Safe ['https://dns.adguard.com/dns-query', 'https://security.cloudflare-dns.com/dns-query', 'https://protected.canadianshield.cira.ca', 'https://dns.opendns.com/dns-query', 'https://dns.umbrella.com/dns-query', 'https://dns.quad9.net/dns-query']
## 锚点 - 国外 DoH DNS 域名服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
DoH_Domain_Family: &DoH_Domain_Family ['https://family-filter-dns.cleanbrowsing.org/dns-query', 'https://adult-filter-dns.cleanbrowsing.org/dns-query', 'https://security-filter-dns.cleanbrowsing.org/dns-query', 'https://dns-family.adguard.com/dns-query', 'https://family.cloudflare-dns.com/dns-query', 'https://family.canadianshield.cira.ca', 'https://familyshield.opendns.com/dns-query']
## 锚点 - 国外 H3 DNS 域名服务器。无过滤
H3_Domain_NoFilter: &H3_Domain_NoFilter ['https://dns-unfiltered.adguard.com/dns-query#h3=true', 'https://1dot1dot1dot1.cloudflare-dns.com/dns-query#h3=true', 'https://dns64.cloudflare-dns.com/dns-query#h3=true', 'https://private.canadianshield.cira.ca/dns-query#h3=true', 'https://dns.google/dns-query#h3=true', 'https://dns64.dns.google/dns-query#h3=true']
## 锚点 - 国外 H3 DNS 域名服务器。安全。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域
H3_Domain_Safe: &H3_Domain_Safe ['https://dns.adguard.com/dns-query#h3=true', 'https://security.cloudflare-dns.com/dns-query#h3=true', 'https://protected.canadianshield.cira.ca/dns-query#h3=true']
## 锚点 - 国外 H3 DNS 域名服务器。家庭保护。基本安全筛选、用户定义的策略、拦截广告、跟踪器、恶意软件、网络钓鱼、漏洞利用工具包域、成人内容
H3_Domain_Family: &H3_Domain_Family ['https://dns-family.adguard.com/dns-query#h3=true', 'https://family.cloudflare-dns.com/dns-query#h3=true', 'https://family.canadianshield.cira.ca/dns-query#h3=true']

```

## 节点订阅的参数锚点

> 每 12 小时更新一次订阅节点，每 600 秒一次健康检查

```yaml
NodeParam: &NodeParam {type: http, interval: 43200, health-check: {enable: true, lazy: true, url: 'http://www.google.com/generate_204', interval: 600}}
```

**参数解析**

| 代理集的参数       | 解析                                      |
| ------------ | --------------------------------------- |
| filter       | 初步筛选需要的节点，可有效减轻路由器压力，支持正则表达式，不筛选可删除此配置项 |
| health-check | 健康检查，未选择到当前代理集合时，不会进行测试，有多个代理集合时可使用     |

## 节点筛选锚点

```
# 地区节点筛选锚点配置
regular-anchor:
  ## Africa
  filterIN: &filterIN '^(?=.*((?i)🇮🇳|印度|班加罗尔|孟买|(\b(Mumbai|IN|India)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  ## Asia
  filterHK: &filterHK '^(?=.*((?i)🇭🇰|香港|(\b(HK|Hong)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterJP: &filterJP '^(?=.*((?i)🇯🇵|日本|川日|东京|大阪|泉日|埼玉|(\b(JP|Japan)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterKR: &filterKR '^(?=.*((?i)🇰🇷|韩国|韓|首尔|(\b(KR|Korea)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterMO: &filterMO '^(?=.*((?i)🇲🇴|澳门|(\b(MO|Oman)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterRU: &filterRU '^(?=.*((?i)🇷🇺|俄罗斯|莫斯科|新西伯利亚|(\b(Новосиби́рская|Moscow|RU|Russia)\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterSG: &filterSG '^(?=.*((?i)🇸🇬|新加坡|狮|(\b(SG|Singapore)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterTW: &filterTW '^(?=.*((?i)🇹🇼|台湾|(\b(TW|Tai|Taiwan)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  ## Australia
  filterAU: &filterAU '^(?=.*((?i)🇦🇺|澳大利亚|(\b(AU|Australia)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  ## Europe
  filterAR: &filterAR '^(?=.*((?i)🇦🇷|阿根廷|(\b(AR|Argentinaia)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterDE: &filterDE '^(?=.*((?i)🇩🇪|德国|(\b(DE|Germany)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterFR: &filterFR '^(?=.*((?i)🇫🇷|法国|(\b(FR|FRA|France)(\d+)?\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterIE: &filterIE '^(?=.*((?i)🇮🇪|爱尔兰|(\b(IE|IRL|Ireland)(\d+)?\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterNL: &filterNL '^(?=.*((?i)🇳🇱|荷兰|(\b(NL|Holland|Netherlands)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterTR: &filterTR '^(?=.*((?i)🇹🇷|土耳其|(\b(TR|TUR|Turkey)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterUK: &filterUK '^(?=.*((?i)🇬🇧|英国|伦敦|(\b(UK|United Kingdom)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  ## North America
  filterCA: &filterCA '^(?=.*((?i)🇨🇦|加拿大|(\b(CA|Canada)\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterUS: &filterUS '^(?=.*((?i)🇺🇸|美国|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥|(\b(US|United States)\d{0,2}\b)))(?!.*((?i)回国|校园|游戏|🎮|(\b(GAME)\b))).*$'
  ## other
  filterOT: &filterOT '^(?=.*(🇬🇧|英|伦敦|(?i)UK|United Kingdom|GB))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇹🇷|土耳其|(?i)TR|TUR|Turkey))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇳🇱|荷|NL|Holland|Netherlands))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇩🇪|德|(?i)DE|Germany))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇮🇪|爱尔兰|IRL|Ireland))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇫🇷|法|FR|France))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*((?i)🇦🇺|澳大|AU|Australia))(?!.*((?i)回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇹🇼|台|(?i)TW|Tai))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇸🇬|新加坡|狮|(?i)SG|Singapore))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇷🇺|俄|莫斯科|新西伯利亚|Новосиби́рская|Moscow|RU|Russia))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇰🇷|韩|韓|首尔|(?i)KR|Korea))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*((?i) 🇯🇵|日|川日|东京|大阪|泉日|埼玉|JP|Japan))(?!.*((?i)回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇭🇰|港|虚通|(?i)HK|Hong))(?!.*(回国|校园|游戏|教育|(?i)GAME|IPV6)).*$`^(?=.*(🇮🇳|印|班加罗尔|孟买|Mumbai|IN|India))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$`^(?=.*(🇺🇸|美|波特兰|达拉斯|俄勒冈|凤凰城|费利蒙|硅谷|拉斯维加斯|洛杉矶|圣何塞|圣克拉拉|西雅图|芝加哥|(?i)US|United States))(?!.*(回国|校园|游戏|教育|久虚|(?i)GAME|IPV6)).*$`^(?=.*(🇨🇦|加拿大|CA|Canada))(?!.*(回国|校园|游戏|教育|久虚|GAME|IPV6)).*$'
  filterGL: &filterGL '^(?=.*(.*))(?!.*((?i)邀请|返利|循环|官网|客服|网站|网址|获取|订阅|流量|到期|机场|下次|版本|官址|备用|到期|过期|已用|联系|邮箱|工单|群|贩卖|通知|倒卖|防止|国内|🎮|(\b(GAME|USE|USED|TOTAL|EXPIRE|EMAIL|Panel)\d{0,2}\b|(\d{4}-\d{2}-\d{2}|\dG)))).*$'
  filterBA: &filterBA '^(?=.*(回国))(?!.*((?i)校园|游戏|🎮|(\b(GAME)\b))).*$'
  filterGA: &filterGA '^(?=.*((?i)游戏|🎮|(\b(GAME)\d{0,2}\b)))(?!.*((?i)回国|校园)).*$'
```

## 策略组参数锚点

```
# 策略组锚点
strategy-anchor:  
  ## 手动选择参数
  select-test: &select-test {type: select, interval: 60, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: false, expected-status: 204}
  select-h: &select-h {type: select, proxies: [🚀 Proxy, 🎯 Direct, 🇮🇳 India 延迟优选, 🇭🇰 Hong Kong 延迟优选, 🇯🇵 Japan 延迟优选, 🇰🇷 Korea 延迟优选, 🇲🇴 Oman 延迟优选, 🇷🇺 Russia 延迟优选, 🇸🇬 Singapore 延迟优选, 🇨🇳 Taiwan 延迟优选, 🇦🇺 Australia 延迟优选, 🇦🇷 Argentinaia 延迟优选, 🇫🇷 France 延迟优选, 🇩🇪 Germany 延迟优选, 🇮🇪 Ireland 延迟优选, 🇳🇱 Netherlands 延迟优选, 🇹🇷 Turkey 延迟优选, 🇬🇧 United Kingdom 延迟优选, 🇨🇦 Canada 延迟优选, 🇺🇸 United States 延迟优选]}
  select-d: &select-d {type: select, proxies: [🎯 Direct, 🚀 Proxy, 🇮🇳 India 延迟优选, 🇭🇰 Hong Kong 延迟优选, 🇯🇵 Japan 延迟优选, 🇰🇷 Korea 延迟优选, 🇲🇴 Oman 延迟优选, 🇷🇺 Russia 延迟优选, 🇸🇬 Singapore 延迟优选, 🇨🇳 Taiwan 延迟优选, 🇦🇺 Australia 延迟优选, 🇦🇷 Argentinaia 延迟优选, 🇫🇷 France 延迟优选, 🇩🇪 Germany 延迟优选, 🇮🇪 Ireland 延迟优选, 🇳🇱 Netherlands 延迟优选, 🇹🇷 Turkey 延迟优选, 🇬🇧 United Kingdom 延迟优选, 🇨🇦 Canada 延迟优选, 🇺🇸 United States 延迟优选]}
  select-p: &select-p {type: select, proxies: [🚀 Proxy, 🇮🇳 India 延迟优选, 🇭🇰 Hong Kong 延迟优选, 🇯🇵 Japan 延迟优选, 🇰🇷 Korea 延迟优选, 🇲🇴 Oman 延迟优选, 🇷🇺 Russia 延迟优选, 🇸🇬 Singapore 延迟优选, 🇨🇳 Taiwan 延迟优选, 🇦🇺 Australia 延迟优选, 🇦🇷 Argentinaia 延迟优选, 🇫🇷 France 延迟优选, 🇩🇪 Germany 延迟优选, 🇮🇪 Ireland 延迟优选, 🇳🇱 Netherlands 延迟优选, 🇹🇷 Turkey 延迟优选, 🇬🇧 United Kingdom 延迟优选, 🇨🇦 Canada 延迟优选, 🇺🇸 United States 延迟优选]}
  ## 时延优选参数
  urlTest: &urltest {type: url-test, tolerance: 50, interval: 60, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: false, include-all: true, expected-status: 204}
  ## 故障转移参数
  fallBack: &fallback {type: fallback, interval: 60, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: false, include-all: true, expected-status: 204}
  ## 负载均衡参数
  loadbalance-1: &loadbalance-1 {type: load-balance, strategy: round-robin, interval: 15, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: true, include-all: true, expected-status: 204}
  loadbalance-2: &loadbalance-2 {type: load-balance, strategy: consistent-hashing, interval: 15, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: true, include-all: true, expected-status: 204}
  loadbalance-3: &loadbalance-3 {type: load-balance, strategy: sticky-sessions, interval: 15, url: 'https://www.google.com/generate_204', disable-udp: false, timeout: 3000, max-failed-times: 3, lazy: true, hidden: true, include-all: true, expected-status: 204}
```

## 规则参数

> 每小时更新一次订阅规则，更新规则时使用直连策略

```yaml
# 远程规则锚点 [每小时更新一次订阅规则，更新规则时使用直连策略],默认格式为yaml，可以更改为text。
rule-anchor:
    ip-yaml: &ip-yaml {type: http, behavior: ipcidr,interval: 86400, format: yaml}
    ip-mrs: &ip-mrs {type: http, behavior: ipcidr,interval: 86400, format: mrs}
    ip-text: &ip-text {type: http, behavior: ipcidr,interval: 86400, format: text}
    domain: &domain {type: http, behavior: domain, interval: 86400, format: yaml}
    domain-mrs: &domain-mrs {type: http, behavior: domain, interval: 86400, format: mrs}
    domain-text: &domain-text {type: http, behavior: domain, interval: 86400, format: text}
    classical-yaml: &classical-yaml {type: http, behavior: classical, interval: 86400, format: yaml}
    classical-text: &classical-text {type: http, behavior: classical, interval: 86400, format: text}
```

## reference

- Clash.Meta(mihomo) 提供的锚点配置

---
modified by: XiaoE
date: 2025-01-17 15:18
updated: 2025-03-29 16:30
---
# Quantumult_X
[Quantumult_X规则类型](https://github.com/LaolunsiG/XiaoE_PCR/blob/main/rules/Quantumult_X/Quantumult_X%E8%A7%84%E5%88%99%E7%B1%BB%E5%9E%8B.md)

**Quantumult_X规则匹配顺序**
- 本地>远程>final
- 不开分流匹配优化：按照在配置中的顺序从上到下，域名类规则>IP类规则
- 开分流匹配优化：host > host-suffix > host-keyword(wildcard) > geoip = ip-cidr (ip6-cidr)> user-agennt
- 远程规则开插入资源：优先级会大于本地规则

## 规则分类

## reference
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/QuantumultX)



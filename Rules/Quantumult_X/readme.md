# Quantumult_X
> data: 未知

> updata: 20250126
- [Quantumult_X规则类型](https://github.com/LaolunsiG/XiaoE_PCR/blob/main/rules/Quantumult_X/Quantumult_X%E8%A7%84%E5%88%99%E7%B1%BB%E5%9E%8B.md)

**Quantumult_X规则匹配顺序**
- 本地>远程>final
- 不开分流匹配优化：按照在配置中的顺序从上到下，域名类规则>IP类规则
- 开分流匹配优化：host > host-suffix > host-keyword(wildcard) > geoip = ip-cidr (ip6-cidr)> user-agennt
- 远程规则开插入资源：优先级会大于本地规则

## 规则分类

## 规则来源
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/QuantumultX)



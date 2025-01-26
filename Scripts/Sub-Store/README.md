# Sub-Store 脚本整理
> data: 20250126

> updata: 20250126
* Sub-Store 脚本整理

## 通用脚本

| 脚本名称                                     | 介绍                                      |
| ---------------------------------------- | --------------------------------------- |
| [rename.js](https://keywos.cf/rename.js) | 本地: 按原节点, 批量重命名, 速度最快 支持所有支持SubStore的设备 |

### 以下两个Sub-Store 脚本，仅支持 `Loon`、 `Surge` 
 > Surge 必须使用带 有参数 [ability=http-client-policy] 走指定节点功能的substore否则脚本无效 
 
| 脚本名称                                   | 介绍                     |
| -------------------------------------- | ---------------------- |
| [cname.js](https://keywos.cf/cname.js) | 联网:真实 入口查询 落地查询 去重并重命名 |
| [pname.js](https://keywos.cf/pname.js) | 联网:Ping去除无效节点 不改名      |

## reference
- [KazooDemo/rule](https://github.com/KazooDemo/rule)

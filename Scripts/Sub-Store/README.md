# Sub-Store 脚本整理
> data: 20250126

> updata: 20250126
* Sub-Store 脚本整理

## 节点检测

### 仅支持 `Loon`、 `Surge` 

| 脚本名称   | 作者  | 脚本链接                                                                                                                                                                      | 介绍     |
| ------ | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| gpt.js |     | [链接](https://raw.githubusercontent.com/xream/scripts/main/surge/modules/sub-store-scripts/check/gpt.js#timeout=1000&retries=1&retry_delay=1000&concurrency=10&client=iOS) | GPT 检测 |

## 节点测速

| 脚本名称   | 作者  | 脚本链接                                                                                                                                                                      | 介绍     |
| ------ | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| gpt.js |     | [链接](https://raw.githubusercontent.com/xream/scripts/main/surge/modules/sub-store-scripts/check/gpt.js#timeout=1000&retries=1&retry_delay=1000&concurrency=10&client=iOS) | GPT 检测 |

## 节点重命名
### 通用脚本

| 脚本名称      | 作者  | 脚本链接                                                                          | 介绍                                      |
| --------- | --- | ----------------------------------------------------------------------------- | --------------------------------------- |
| rename.js |     | [链接](https://raw.githubusercontent.com/Keywos/rule/refs/heads/main/rename.js) | 本地: 按原节点, 批量重命名, 速度最快 支持所有支持SubStore的设备 |
|           |     |                                                                               |                                         |

### 仅支持 `Loon`、 `Surge` 
 > Surge 必须使用带 有参数 [ability=http-client-policy] 走指定节点功能的substore否则脚本无效 
 
| 脚本名称     | 作者  | 脚本链接 | 介绍                     |
| -------- | --- | ---- | ---------------------- |
| cname.js |     |      | 联网:真实 入口查询 落地查询 去重并重命名 |
| pname.js |     |      | 联网:Ping去除无效节点 不改名      |

## reference
- [Sub-Store 脚本](https://www.jovegg.tech/posts/5)
- [KazooDemo/rule](https://github.com/KazooDemo/rule)
# 自用代理资源存储库-PCR
- Clash 因不再更新，不支持新规则和新的加密，所以创建此自用存储库。
- 本存储库会将一些规则合在一起，以便于使用。
- [Clash.Meta](https://github.com/LaolunsiG/PCR/tree/main/rules/Clash.Meta) 可用于旧版 Clash 内核的 Clash for Android(3.0.3) and Clash for Windows。

<details> 
  <summary> 更新日志和未来规划 </summary>

> 只保留 5 次记录

### 2025-01-02
- 删去了不必要规则和优化了部分笔记的呈现。

### 2025-01-01
- 决定修改规则资源和部分笔记的呈现，之后再修改优化配置文件。

### 2024-11-25
- loon 配置文件节点筛选错误修复

### 2024-11-24
- 优化了多个页面的可读性，并修复了配置的部分错误。
- 修改了 shadowrocket 的配置文件，主要去除了不必要的配置。

### 2024-11-12
- 修复 [loon 配置文件](https://github.com/LaolunsiG/PCR/blob/main/Config_File/Loon/XiaoE_Loon.conf) 的 DNS 服务，配置文件整体修改，去除了不必要的代码解释。


</details>

## 不同代理工具的配置文件及其教程

| 内核                                                                                  | 操作系统       | 配置文件 | 教程  | 介绍                       |
| ----------------------------------------------------------------------------------- | ---------- | ---- | --- | ------------------------ |
| [Clash](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Clash)（以删库）          | 多平台        |      |     |                          |
| [Clash.Meta](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Clash.Meta)     | 多平台        |      |     |                          |
| [LanceX](https://github.com/LaolunsiG/PCR/tree/main/Config_File/LanceX)             | IOS, MacOS |      |     | 此软件还未完善，不推荐使用            |
| [Loon](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Loon)                 | IOS, MacOS |      |     |                          |
| [Quantumult_X](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Quantumult_X) | IOS, MacOS |      |     |                          |
| [Shadowrocket](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Shadowrocket) | IOS, MacOS |      |     | 支持加密协议最多的代理软件            |
| [Sing-Box](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Sing-Box)         | 多平台        |      |     | 支持加密协议最多的代理软件            |
| [Stash](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Stash)               | IOS, MacOS |      |     |                          |
| [Surfboard](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Surfboard)       | Android    |      |     |                          |
| [Surge](https://github.com/LaolunsiG/PCR/tree/main/Config_File/Surge)               | IOS, MacOS |      |     | IOS上最贵的代理工具，也是功能最全的代理工具。 |

## 代理规则
- [All](https://github.com/LaolunsiG/PCR/tree/main/Rules)

### ruleset

| 内核               | 规则                                                            |
| ---------------- | :------------------------------------------------------------ |
| Clash            | https://github.com/LaolunsiG/PCR/tree/main/Rules/Clash        |
| Clash.Meta/Stash | https://github.com/LaolunsiG/PCR/tree/main/Rules/Clash.Meta   |
| Shadowrocket     | https://github.com/LaolunsiG/PCR/tree/main/Rules/Shadowrocket |
| Quantumult_X     | https://github.com/LaolunsiG/PCR/tree/main/Rules/Quantumult_X |
|                  |                                                               |

### geodata

## 其他代理教程
- [GetSomeCats](https://github.com/getsomecat/GetSomeCats/tree/Surge)

### 注释规则
> 配置文件的注释符号

| 配置文件格式 | (单行)注释符号  | Wiki                                                                                         |
| ------ |:---------:| -------------------------------------------------------------------------------------------- |
| JSON   | 无         | [JavaScript和Json的区别](https://blog.csdn.net/qq_44273429/article/details/117409345)-CSDN       |
| INI    | ; & # & ! | [programming-note](https://programming-note-sylarliu.readthedocs.io/zh-cn/latest/index.html) |
| YAML   | #         | [菜鸟教程](https://www.runoob.com/w3cnote/yaml-intro.html)                                       |

## 免责申明
- 本项目涉及的脚本仅用于资源共享和学习研究，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断.
- 间接使用该项目的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本项目对于由此引起的任何隐私泄漏或其他后果概不负责.
- 请勿将本项目的任何内容用于商业或非法目的，否则后果自负.
- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本.
- 对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害.
- 您必须在下载后的24小时内从计算机或手机中完全删除以上内容.
- 任何以任何方式查看此项目的人或直接或间接使用该项目的使用者都应仔细阅读此声明。保留随时更改或补充此免责声明的权利。一旦使用并复制了该项目的任何文件，则视为您已接受此免责声明.

## 感谢以下作者/项目
> 排名不分先后

| 作者/项目名        | 仓库链接/其他链接                                         | Telegram 频道         |
| ------------- | ------------------------------------------------- | ------------------- |
| blackmatrix7  | https://github.com/blackmatrix7/ios_rule_script   |                     |
| iKeLee        | https://gitlab.com/lodepuly/vpn_tool/             | https://t.me/iKeLee |
| ProxyResource | https://github.com/luestr/ProxyResource/tree/main |                     |
| Moli-X        | https://github.com/Moli-X                         | https://t.me/QuantX |
| whatshub.top  | https://whatshub.top/                             |                     |

# Pi Agent × OpenClaw 技术洞察

归档日期：2026-07-14  
证据截止：2026-07-08

## 归档范围

本目录归档《Pi Agent 的分层 Harness，以及它如何与 OpenClaw 的平台控制面相遇》技术长报告。报告分两条主线展开：第一部分沿 Pi Agent 的演进历史解释 Provider、coding agent、Harness、TUI/CLI、Extension/RPC 与稳定性机制如何逐层形成；第二部分先排除未经证实的单向驱动关系，再分析 OpenClaw 与 Pi Agent 如何因长期 Agent 任务的共同要求而形成能力对应与分层协作。

## 交付文件

| 文件 | 说明 |
| --- | --- |
| `pi_agent_technical_insight_report.html` | 可离线打开的 SingleFile HTML 技术长报告 |

## 核心结论

Agent 架构正在从“模型调用工具”走向“业务平台托管长期任务”。业务平台与运行内核将逐渐分层：业务侧持续创新入口、工作流、插件、权限和行业场景，内核侧持续创新模型访问、任务执行、长期状态和工具能力；稳定接口、完整状态生命周期和可执行架构记忆，使两侧能够以不同速度独立演进。

报告没有把 OpenClaw 与 Pi Agent 写成谁驱动谁的关系。现有证据支持的判断是：两者独立演进，但 Agent 任务长期化、并行化和受控运行，使业务平台与运行内核在能力上自然对齐。Pi 已经进入 OpenClaw 的部分真实运行路径，但不能据此推断 Pi 是唯一或必选的运行内核。

## 证据与方法

- Pi Agent 证据来自 `earendil-works/pi` 的 release、PR、issue、commit、代码与测试演进；本次代码核验基线为 commit `86afffe01f6f9c28207a3c712f5cddad10332987`。
- OpenClaw 证据来自 `openclaw/openclaw` 的 ReleaseNote、PR、issue 和公开代码记录；需求密度统计以 625 条唯一 primary ReleaseNote 为基线。
- 双方关系判断区分直接记录、结构对应和反向因果空证据；五条 embedded Pi 直接记录只用于证明部分真实接入，不外推到全部会话或完整调用链。
- 分析过程依次完成数据采集、结构化归一、时间阶段划分、分层机制分析、claim/反证核验、语义图建模和浏览器视觉检查。

依据本仓库的正式交付归档规则，数据采集缓存、上游源码副本、分析过程文档、生成脚本和 QA 中间记录不进入本目录；报告正文已经呈现与核心结论相关的证据、口径、边界和参考索引。

## 主要来源

- Pi Agent: <https://github.com/earendil-works/pi>
- OpenClaw: <https://github.com/openclaw/openclaw>

## 归档校验

- 使用仓库 `scripts/export_singlefile_archive.py` 完成 SingleFile 导出，结果为 1/1 成功。
- HTML 不依赖旁路 CSS、JavaScript、图片或字体文件，不包含 `localhost`、`127.0.0.1` 或 `file://` 临时地址。
- 报告专项结构与语义图校验通过。
- `python scripts/pre_commit_gate.py` 通过，包含 14 个归档与 SingleFile 单元测试。

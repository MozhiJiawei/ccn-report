# Molt：PyTorch 原生的智能体强化学习框架

## SMART 技术一句话

截至 2026-08-03 的 NVIDIA 官方仓库快照，Molt 是以普通 Python Agent 程序为训练对象的 PyTorch 原生智能体强化学习框架，通过 Ray、vLLM、NVIDIA AutoModel、token-exact loopback 与 MoE Routing Replay 组合训练闭环，官方仓库当日口径约为 9.2K 行 RL 代码并覆盖至 1T-class MoE，用于降低大规模 Agent RL 的框架改造和系统集成成本。

## 归档信息

- 任务编号：TASK-20260803-02
- 热点编号：HS-20260803-02
- 周期：2026-W32
- 本地归档日期：2026-08-03
- 创建者：Codex

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile Source Understanding HTML。

## 来源与证据边界

- 关键技术断言优先采用作者论文与 NVIDIA 官方仓库，任务指定的 MarkTechPost 报道作为发布时点材料。
- 2026-08-01 报道口径为约 8.6K 行 RL 代码、覆盖到 700B；2026-08-03 官方仓库口径为约 9.2K 行、覆盖到 1T-class MoE，两组数字不是同一版本事实。
- 论文实验和项目方规模声明不构成对任意模型、硬件或生产负载的普遍性能保证。

## QA 状态

- 五个来源包 validator：全部通过。
- SingleFile 导出：成功。
- 三份来源理解产物均通过独立视觉 QA；本目录归档主报告，最终主报告 QA 为 PASS。

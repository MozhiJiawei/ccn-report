# Evo-Harness：把执行上下文编译为可复用技能

## 一句话总结

Evo-Harness 是 2026 年发布的冻结智能体在线技能编译框架，它不更新 Solver 参数，而是从顺序任务流的执行轨迹、结果与环境反馈中提炼跨任务模式和任务类型流程并持续维护外部 Skill Harness，在 Claude Opus 4.6 Solver 的论文实验中于 5 个现实基准均取得最高成功率、其中 TerminalBench-2 相对 No-Evolve 提高 10.11 个百分点，用于让可验证的单次经验跨后续任务复用。

## 任务信息

- 序号：27
- 任务编号：TASK-20260827173622-5e2d7cb4
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：Evo-Harness将单次执行编译为复用技能，使冻结智能体跨任务持续改进技术线索
- 任务来源：[https://arxiv.org/abs/2608.15071](https://arxiv.org/abs/2608.15071)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 Evo-Harness 的技能编译闭环、两层技能结构、实验结果与适用边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [EVO-HARNESS: Context-to-Harness Skill Compilation for Self-Evolving Agents](https://arxiv.org/abs/2608.15071)：用于支撑冻结 Solver、执行反思、技能编译和 Harness 更新机制，以及五基准成功率与消融边界。
- [A-Evolve / Evo-Harness 官方代码](https://github.com/A-EVO-Lab/a-evolve/tree/release/evo-harness)：用于核对技能目录结构、基准入口、输出产物和当前公开实现边界。


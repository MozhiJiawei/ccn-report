# LongHorizon-Harness

## 一句话总结

阿里巴巴 DreamX 团队在 2026 年 8 月 3 日发布的 LongHorizon-Harness 论文 v1 提出面向长程计算机任务的管理、执行与独立审计循环，通过仅以环境核验证据更新外置任务状态，在相同 Qwen 3.7-Plus 与 Claude Code 后端的作者 root 权限实验中将 WeaveBench 的任务通过率从 51.8% 提升至 80.7%，为多步骤智能体减少错误状态累积提供运行架构。

## 任务信息

- 序号：89
- 任务编号：TASK-20260910151814-f3659cb9
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：指定分类为 null，自动归类；全文主要贡献是 Manager、fresh-context Executor 与 read-only Auditor 的任务编排和状态转换，记忆、工具与评测属于支撑要素，故唯一归入 Agent架构与编排；已比较02与06细则，无指定分类冲突。
- 任务正文：阿里LongHorizon-Harness
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.01964)

## 交付件说明

- [LongHorizon-Harness.html](./LongHorizon-Harness.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LongHorizon-Harness.pptx](./LongHorizon-Harness.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

WeaveBench 作者实验使用 root 权限，不与普通权限官方成绩直接比较；OSWorld同时改变工具能力；Opus34任务子集正文20.6%/35.3%与摘要20.0%/34.3%冲突，报告以正文表格为准并披露；没有完整MEA组件单因素消融；token成本因任务与模型而异。

## 引用信息源说明

- [LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks v1](https://arxiv.org/abs/2608.01964v1)：支撑MEA架构、原始图表、实验数据、成本与证据边界。

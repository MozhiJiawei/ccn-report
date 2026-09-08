# Agentic Transaction：面向长链智能体的语义 ACID 事务

## 一句话总结

Agentic Transaction 是 2026 年 8 月预印本提出的长链智能体事务框架，它把探索、执行、验证和提交组织成具有语义原子性、一致性、隔离性与持久性的可恢复单元，并在 KramaBench、同一 Qwen 骨干的论文实验中把 ACID-Agent 总体得分由 Claude Code 风格基线的 64.0 提高到 74.6（+10.6 个绝对得分点），用于降低智能体修改持久环境时半成品泄漏和失败状态污染的风险。

## 任务信息

- 序号：19
- 任务编号：TASK-20260827145339-86d4e48e
- 热点编号：HS-20260814-article133044
- 周期：2026-W33
- 任务正文：Agentic Transaction 提出 ACID 兼容智能体框架，性能超越 Claude Code 10.6%
- 任务来源：[https://arxiv.org/abs/2608.13900](https://arxiv.org/abs/2608.13900)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 Agentic Transaction 的语义 ACID 模型、ACID-Agent 系统、实验结果与证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Agentic Transaction: Towards ACID-Compliant Agent Systems](https://arxiv.org/abs/2608.13900)：用于支撑语义 ACID 定义、系统架构、KramaBench 得分、步骤和成本权衡。
- [ACID-Agent 官方代码仓库](https://github.com/TsinghuaDatabaseGroup/ACID-Agent)：用于核对可运行实现、系统组件、评测入口与复现边界。


# MemoryLake on MemoryArena：智能体记忆后端的匹配研究

## 一句话总结

MemoryLake on MemoryArena 是 2026 年发布的智能体记忆后端匹配研究，它在同一 Agent 框架、模型别名、任务样本和评分代码下比较 MemoryLake、Mem0、Vector RAG 与 Long Context，在五域等权 Macro Success Rate 的观测中取得 20.5% 对最佳比较系统 13.6%，但旅行任务全部失败且购物 150 个任务仅成功 1 个，用于揭示后端收益依赖任务与交接策略、不能被外推为稳定因果优势。

## 任务信息

- 序号：26
- 任务编号：TASK-20260827173445-99ce4154
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：MemoryLake系统级对比揭示记忆后端优势不稳定，真实任务仍普遍失效技术线索
- 任务来源：[https://arxiv.org/abs/2608.13883](https://arxiv.org/abs/2608.13883)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 MemoryArena 闭环任务、四类后端配置、PS/SR 指标、观测结果和统计边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends](https://arxiv.org/abs/2608.13883)：用于支撑四种后端的匹配比较、五类任务结果、小样本置信区间和因果边界。
- [MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks](https://arxiv.org/abs/2602.16313)：用于支撑跨会话依赖链、Process Score、Success Rate 与任务规模定义。
- [MemoryLake MemoryArena 配套评测仓库](https://github.com/memorylake-ai/memorylake-memoryarena-benchmark)：用于核对实验协议、样本清单、后端接口、方法披露和复现边界。


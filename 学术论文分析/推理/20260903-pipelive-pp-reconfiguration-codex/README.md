# PipeLive 在线流水线重配置

## 一句话总结

截至 2026 年 4 月论文版本，PipeLive 在动态 LLM serving 中执行原地流水线并行重配置，以减少扩缩容切换开销，并在论文实验范围内验证服务连续性和性能收益。

## 任务信息

- 序号：52
- 任务编号：`PPTRANS-20260902-018`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：PipeLive: Efficient Live In-place Pipeline Parallelism Reconfiguration for Dynamic LLM Serving
摘要：面向动态负载和异构 GPU 环境中的 PP 在线重构，设计可实时调整大小的 KV cache 布局、PageAttention 扩展和增量 KV 修补机制，使源配置与目标配置在不中断推理的情况下同步状态并安全切换。重构开销从秒级降至 10 ms 以下，TTFT 和 TPOT 分别最多改善 54.7% 与 14.7%。
- 任务来源：[https://arxiv.org/abs/2604.12171](https://arxiv.org/abs/2604.12171)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [PipeLive 原始论文](https://arxiv.org/abs/2604.12171)：用于支撑在线重配置机制、系统实现和实验数据。

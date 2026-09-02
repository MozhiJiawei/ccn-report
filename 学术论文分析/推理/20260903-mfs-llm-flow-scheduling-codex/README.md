# LLM 多阶段流调度

## 一句话总结

截至 2026 年 3 月论文版本，Multi-stage Flow Scheduling 以跨推理阶段的流量感知调度协调 LLM serving 通信，并在论文实验条件下验证尾延迟和吞吐收益。

## 任务信息

- 序号：48
- 任务编号：`PPTRANS-20260902-014`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：Multi-stage Flow Scheduling for LLM Serving
摘要：观察到 KV-block 检索、collective 和 P2D transfer 等依赖流会竞争共享瓶颈链路，提出 stage-aware 的 Defer-and-Promote 流调度和 Reverse Multi-Level Queue。作为 vLLM 插件在 8 服务器、32 GPU 环境评估，TTFT SLO 达成率提高 1.2–2.4 倍。
- 任务来源：[https://arxiv.org/abs/2603.17456](https://arxiv.org/abs/2603.17456)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Multi-stage Flow Scheduling 原始论文](https://arxiv.org/abs/2603.17456)：用于支撑调度机制、系统实现和评测结论。

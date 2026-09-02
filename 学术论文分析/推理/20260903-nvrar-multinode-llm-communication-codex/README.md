# 多节点 LLM 推理通信优化

## 一句话总结

截至 2026 年正式论文版本，该研究系统刻画多节点 LLM 推理的通信瓶颈并提出 NVRAR 等优化，在论文覆盖的平台、模型和并行配置下量化验证通信与推理性能改善。

## 任务信息

- 序号：46
- 任务编号：`PPTRANS-20260902-012`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：Understanding and Improving Communication Performance in Multi-node LLM Inference
摘要：系统研究多节点 LLM 推理中的 TP 与混合 TP+PP 通信瓶颈，并提出基于 NVSHMEM recursive doubling 的分层 AllReduce。对 128 KB–2 MB 的 decode 小消息，相比 NCCL 延迟降低 1.9–3.6 倍；Llama 3.1 405B 的 decode-heavy batch latency 最高改善 1.72 倍。
- 任务来源：[https://doi.org/10.1145/3786335.3813165](https://doi.org/10.1145/3786335.3813165)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [原始论文 DOI](https://doi.org/10.1145/3786335.3813165)：用于支撑瓶颈分析、优化方法与实验结果。

# UCCL-Zip GPU 通信无损压缩

## 一句话总结

截至 2026 年 4 月论文版本，UCCL-Zip 将严格等价的无损压缩融合进 GPU 点对点与 NCCL collective 通信路径，并在论文的 vLLM 实验中将端到端推理延迟最高降低 10%。

## 任务信息

- 序号：36
- 任务编号：`PPTRANS-20260902-002`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：UCCL-Zip: Lossless Compression Supercharged GPU Communication
摘要：将无损压缩直接集成到 GPU 点对点和 collective 通信原语中。P2P 路径支持大块数据的分段发送，collective 路径把压缩融合进 NCCL persistent kernel，在不改变数值正确性的前提下降低通信数据量；在 vLLM 上端到端推理延迟最高降低 10%。
- 任务来源：[https://arxiv.org/abs/2604.17172](https://arxiv.org/abs/2604.17172)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [UCCL-Zip 原始论文](https://arxiv.org/abs/2604.17172)：用于支撑压缩原语、NCCL 融合方式和端到端结果。

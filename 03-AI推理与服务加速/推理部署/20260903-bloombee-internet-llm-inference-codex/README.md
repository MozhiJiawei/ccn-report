# BloomBee 互联网尺度分布式生成推理

## 一句话总结

截至 2026 年 4 月论文版本，BloomBee 面向低带宽互联网链路联合优化层分配、微批处理、张量卸载、无损压缩与推测解码，在论文实验中将吞吐最高提升 1.76 倍并将平均延迟最高降低 43.20%。

## 任务信息

- 序号：35
- 任务编号：`PPTRANS-20260902-001`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：Distributed Generative Inference of LLM at Internet Scales with Multi-Dimensional Communication Optimization (BloomBee)
摘要：面向互联网尺度的分布式生成式 LLM 推理。BloomBee 联合优化层分配、微批处理、张量卸载、无损压缩和推测式解码；其阶段间 FP16 激活采用字节平面拆分与熵编码，可逐 bit 恢复。在低带宽网络上，系统吞吐最高提升 1.76 倍，平均延迟最高降低 43.20%。
- 任务来源：[https://arxiv.org/abs/2604.21072](https://arxiv.org/abs/2604.21072)

## 交付件说明

- [BloomBee-互联网分布式推理.html](./BloomBee-互联网分布式推理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [BloomBee-互联网分布式推理.pptx](./BloomBee-互联网分布式推理.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [BloomBee 原始论文](https://arxiv.org/abs/2604.21072)：用于支撑系统方法、无损激活压缩机制及吞吐和延迟结果。

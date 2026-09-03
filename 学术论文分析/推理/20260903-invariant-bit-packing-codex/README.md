# Invariant Bit Packing 无损张量压缩

## 一句话总结

截至 2026 年 5 月论文版本，Invariant Bit Packing 识别张量集合中的不变 bit 并以 GPU 友好的并行解码减少 PCIe 搬运，在论文覆盖的 GNN、DLRM 与 LLM 推理中使 LLM 推理平均加速约 24%。

## 任务信息

- 序号：38
- 任务编号：`PPTRANS-20260902-004`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：Reducing the GPU Memory Bottleneck with Lossless Compression for ML
摘要：提出 Invariant Bit Packing，通过识别一组张量中的不变 bit 并采用 GPU 友好的并行解码，减少 PCIe 上的按需张量搬运。方法保持完全无损，并被集成到 GNN、DLRM 和 LLM 推理框架中；LLM 推理平均加速约 24%。
- 任务来源：[https://arxiv.org/abs/2605.30728](https://arxiv.org/abs/2605.30728)

## 交付件说明

- [Invariant-Bit-Packing-GPU内存压缩.html](./Invariant-Bit-Packing-GPU内存压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Invariant-Bit-Packing-GPU内存压缩.pptx](./Invariant-Bit-Packing-GPU内存压缩.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Invariant Bit Packing 原始论文](https://arxiv.org/abs/2605.30728)：用于支撑无损编码方法、集成范围和性能数据。

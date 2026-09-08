# NetZIP 网内无损压缩

## 一句话总结

截至 2026 年公开论文版本，NetZIP 以张量 bit/value 两级变换和 FPGA NIC 旁路压缩器降低分布式大模型通信量，在论文实验中将激活压缩效果提高 43–75 个百分点并将训练时间降低 35%。

## 任务信息

- 序号：37
- 任务编号：`PPTRANS-20260902-003`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：NetZIP: Algorithm/Hardware Co-design of In-network Lossless Compression for Distributed Large Model Training
摘要：提出面向大模型张量通信的算法—硬件协同无损压缩。算法在 bit/value 两级变换梯度和激活，硬件则把轻量压缩器部署到 FPGA NIC 中，以旁路方式降低编解码延迟。对多种大模型，激活压缩效果比重型通用无损算法高 43–75 个百分点，训练时间降低 35%。
- 任务来源：[https://research.ibm.com/publications/netzip-algorithmhardware-co-design-of-in-network-lossless-compression-for-distributed-large-model-training](https://research.ibm.com/publications/netzip-algorithmhardware-co-design-of-in-network-lossless-compression-for-distributed-large-model-training)

## 交付件说明

- [NetZIP-网内无损压缩.html](./NetZIP-网内无损压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NetZIP-网内无损压缩.pptx](./NetZIP-网内无损压缩.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [IBM Research 论文页](https://research.ibm.com/publications/netzip-algorithmhardware-co-design-of-in-network-lossless-compression-for-distributed-large-model-training)：用于支撑算法—硬件协同设计与实验结论。

# NCCLX 十万卡集群通信

## 一句话总结

截至 2025 年 10 月论文版本，NCCLX 面向十万卡以上 GPU 集群重构 collective 通信路径，并在论文披露的超大规模部署与实验条件下验证可扩展性和通信性能。

## 任务信息

- 序号：45
- 任务编号：`PPTRANS-20260902-011`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：Collective Communication for 100k+ GPUs (NCCLX)
摘要：提出面向十万级 GPU 集群的 NCCLX 通信框架，覆盖训练与低延迟推理。系统针对 PP 提供 SM-free、zero-copy Send/Recv，针对 TP 提供 RMA Put，并支持 GPU-resident dynamic AllToAllv；还会根据机架和跨楼拓扑调整 QP 数量及 outstanding data。
- 任务来源：[https://arxiv.org/abs/2510.20171](https://arxiv.org/abs/2510.20171)

## 交付件说明

- [NCCLX-十万卡集体通信.html](./NCCLX-十万卡集体通信.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NCCLX-十万卡集体通信.pptx](./NCCLX-十万卡集体通信.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [NCCLX 原始论文](https://arxiv.org/abs/2510.20171)：用于支撑系统架构、规模范围与性能结果。

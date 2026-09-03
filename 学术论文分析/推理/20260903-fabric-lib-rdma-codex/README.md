# fabric-lib LLM 系统 RDMA 通信

## 一句话总结

截至 2025 年 10 月论文版本，fabric-lib 为 LLM 系统提供 RDMA 点对点通信抽象，并在论文覆盖的设备与工作负载下验证跨后端可用性和通信性能。

## 任务信息

- 序号：47
- 任务编号：`PPTRANS-20260902-013`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：fabric-lib: RDMA Point-to-Point Communication for LLM Systems
摘要：为 LLM 系统提供跨 ConnectX 和 AWS EFA 的统一 RDMA P2P 接口。其 one-sided WriteImm 与 ImmCounter 不依赖传输层有序语义，能够透明管理多 NIC，并已用于 KV cache 迁移、MoE dispatch/combine 和异步权重更新；两类 NIC 上均达到 400 Gbps。
- 任务来源：[https://arxiv.org/abs/2510.27656](https://arxiv.org/abs/2510.27656)

## 交付件说明

- [fabric-lib-RDMA通信.html](./fabric-lib-RDMA通信.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [fabric-lib-RDMA通信.pptx](./fabric-lib-RDMA通信.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [fabric-lib 原始论文](https://arxiv.org/abs/2510.27656)：用于支撑 RDMA 抽象、系统实现和基准结果。

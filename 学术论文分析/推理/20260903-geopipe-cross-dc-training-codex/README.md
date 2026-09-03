# GeoPipe 跨数据中心训练

## 一句话总结

截至 2025 年 10 月论文版本，GeoPipe 在无损 RDMA 数据中心光传送网上增强地理分布式 LLM 训练的流水线并行，并在论文仿真与实验范围内验证通信和训练性能收益。

## 任务信息

- 序号：49
- 任务编号：`PPTRANS-20260902-015`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：GeoPipe: a Geo-distributed LLM Training Framework with Enhanced Pipeline Parallelism in a Lossless RDMA-enabled Datacenter Optical Transport Network
摘要：在由无损 RDMA 数据中心光传送网连接的多数据中心环境中实现增强型流水线并行，并联合考虑跨数据中心带宽和 HBM 约束。该研究验证的是 LLM 训练而非自回归推理，且性能收益包含通信—计算重叠，但为 PP 跨域传输协议和网络架构提供了直接参考。
- 任务来源：[https://arxiv.org/abs/2510.12064](https://arxiv.org/abs/2510.12064)

## 交付件说明

- [GeoPipe-跨地域流水线训练.html](./GeoPipe-跨地域流水线训练.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [GeoPipe-跨地域流水线训练.pptx](./GeoPipe-跨地域流水线训练.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [GeoPipe 原始论文](https://arxiv.org/abs/2510.12064)：用于支撑跨域训练架构、网络假设和性能结果。

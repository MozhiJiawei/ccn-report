# exo 本地分布式推理深度洞察

截至 2026-09-22、基于 exo commit `21a54c5ea0230a3bec1e1a786d200126c7e34ec6` 与 EXO 1.0 公开证据，exo 是面向 Apple Silicon 等本地设备的开源分布式推理编排软件，通过 pipeline/tensor parallelism 与 Thunderbolt 5 RDMA 聚合模型容量和算力；四台 M3 Ultra 的独立测试中 Qwen3-235B 8-bit generation 吞吐由单节点 19.5 tok/s 提升至四节点 31.9 tok/s，但收益受模型、量化、并发、网络路径与指标口径约束，因此本报告为本地集群选型和复现实验提供证据边界而非无条件性能承诺。

## 归档内容

- `source_understanding_review.html`：主报告，包含 exo 架构、能力边界、证据审计以及模型和性能子报告入口。
- `model-support/index.html`：内置模型目录、支持层级和限制条件。
- `benchmark/index.html`：公开性能证据、可比口径、复现要求与不可引用数据源说明。

所有 HTML 均已导出为 dependency-free SingleFile，可离线打开；主报告中的子报告链接保持为相对路径。

## 分类说明

- 一级分类：`03-AI推理与服务加速`
- 二级分类：`推理部署`
- 归类理由：报告主体是消费级设备上的分布式推理部署、模型切分、节点编排、RDMA 互联与性能边界，而非模型能力评测或通用硬件评测。

## 人工核验备注

- 官方 benchmark 网站在核验时仍为 Coming soon 演示页，前端使用硬编码基础数组和随机扰动，未作为测量数据引用。
- 官方异构实验标题中的“4×”不是端到端总加速；同表总时间重算为 `6.42 / 2.32 = 2.77×`，与原文四舍五入的 2.8×一致。
- Jeff Geerling 的三组 RDMA 数据只在各自模型系列内比较；报告未跨模型、量化或测试来源拼接总榜。

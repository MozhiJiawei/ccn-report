# CoFiBench-压缩保真

## 一句话总结

2026年10月30日arXiv v4论文提出上下文压缩保真诊断基准CoFiBench，在Qwen与LLaMA的27种压缩配置、4/16/64倍压缩率下用知识覆写与语义漂移QA揭示：更大压缩器即使重建分数更高，也可能更难保留原文事实和关系。

## 任务信息

- 序号：300
- 任务编号：neurips2026-H9lFJNJ2so
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：API category=null；按2026-11-03人类审阅表，将主归属调整为推理输入输出数据：正文围绕上下文输入压缩的表示与保真边界，CoFiBench用于诊断该压缩过程。评测方法与数据集为次要关联；不把诊断基准表述为新剪枝算法或已验证的推理加速。
- 任务正文：When Less is More: The LLM Scaling Paradox in Context Compression
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：上下文压缩质量分析；非新token剪枝算法
压缩对象：compressor-decoder上下文压缩中的compressed memory与重建文本
方法线索（既有摘要）：分析27种压缩器配置在不同模型规模、家族和压缩率下的重建忠实性；不是新剪枝算法。
2026-11-03独立复核的纳入依据：主审保留为上下文压缩质量分析：直接研究compressor-decoder、压缩率、compressed memory和重建忠实性，符合语义压缩研究范围。没有提出新的剪枝算法，也未证明下游推理加速；不臆造soft slot数量。
证据边界：研究faithful recovery而非压缩推理端到端加速；soft memory具体结构需正文核实。；本轮复核：compressed memory具体形式、压缩率及下游QA适用性需正文核实；摘要主要研究重建而非端到端推理。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/153967)

## 交付件说明

- [CoFiBench-压缩保真.html](./CoFiBench-压缩保真.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [CoFiBench-压缩保真.pptx](./CoFiBench-压缩保真.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [When Less is More: The LLM Scaling Paradox in Context Compression（arXiv v4，2026-10-30）](https://arxiv.org/abs/2602.09789v4)：正文方法、CoFiBench、连续memory表示、压缩率、重建及下游QA实验和证据边界。
- [NeurIPS 2026 Poster: When Less is More](https://neurips.cc/virtual/2026/poster/153967)：会议Poster身份与摘要对照。

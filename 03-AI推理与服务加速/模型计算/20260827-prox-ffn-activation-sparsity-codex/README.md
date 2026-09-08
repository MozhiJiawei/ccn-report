# Prox：无需训练的 FFN 激活稀疏化

## 一句话总结

Prox 是 2026 年 7 月 30 日发布的无需训练 SwiGLU FFN 激活稀疏方法，它先用稀疏输入和 INT4 代理权重近似中间通道显著性以生成共享 mask，再仅对入选通道使用原始权重精算，在论文覆盖的 10 个模型、6 个家族和 NVIDIA A6000 单 batch 解码实验中于 60%–70% FFN 稀疏下取得 1.51–1.99 倍端到端加速，用于在不重训模型的条件下降低 FFN 权重访问与乘加开销。

## 任务信息

- 序号：23
- 任务编号：TASK-20260827163532-f08c637f
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：Prox框架实现LLM FFN激活稀疏化无需训练且解码加速2倍技术线索
- 任务来源：[https://arxiv.org/abs/2607.27591](https://arxiv.org/abs/2607.27591)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 Prox 的代理显著性、两阶段稀疏执行、质量与性能证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Prox: Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience in LLMs](https://arxiv.org/abs/2607.27591)：用于支撑两阶段代理筛选与精确稀疏计算方法，以及不同模型、稀疏率、GPU 和自定义 kernel 条件下的质量与加速结果。


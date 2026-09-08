# HiLS-Attention：面向超长上下文的层次化稀疏注意力

本目录归档 HiLS-Attention 原始论文的 Source Understanding 正式报告，面向不了解该技术的技术读者，解释其如何通过可学习的块级检索、块内精确注意力与端到端语言模型损失监督，同时改善超长上下文外推能力和推理效率。

## 一句话描述

HiLS-Attention 是一种原生可训练的层次化块稀疏注意力机制，通过可学习 Landmark 选块与块内精确注意力，在论文设定下将 8K 训练上下文免训外推至 4M（512×），并在 H800、512K 上下文中实现 13.5× prefill 和 15.7× 单步解码加速。

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile HTML，可离线打开，不依赖外部图片、CSS、JavaScript 或字体文件。

## 唯一主证据

- 论文：**Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling**
- arXiv：https://arxiv.org/abs/2607.02980
- 版本边界：arXiv 预印本；报告结论以论文披露的模型、硬件、上下文长度、稀疏预算和测试任务为限。

## 核心证据边界

- “512×免训外推”指已经完成 HiLS 训练或转换的模型从 8K 训练长度直接测试至 4M，不表示任意全注意力模型可以零训练切换为 HiLS。
- `13.5×` 对应论文 H800、batch size 1、bf16、512K 上下文条件下的 prefill 加速。
- `15.7×` 对应同一测试口径下的单步 decode 加速，不等同于端到端请求吞吐或成本下降。
- 现有全注意力模型转换为 HiLS 仍需轻量参数调优或继续预训练；论文中的峰值结果不可无条件泛化到其他模型、硬件或负载。

## 人工与质量状态

- Source Understanding：用户已确认归档。
- 论文图表解析：24/24 已索引。
- SingleFile 导出：成功。
- 独立视觉 QA：PASS；未发现破图、溢出、裁切或遮挡。

归档日期：2026-07-30  
Creator：Codex

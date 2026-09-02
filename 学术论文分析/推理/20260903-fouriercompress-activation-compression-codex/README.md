# FourierCompress 频域激活压缩

## 一句话总结

截至 2025 年 10 月论文版本，FourierCompress 面向协同 LLM 推理按层选择频域激活压缩强度，并在论文实验范围内验证带宽、准确率与延迟之间的可控取舍。

## 任务信息

- 序号：41
- 任务编号：`PPTRANS-20260902-007`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：FourierCompress: Layer-Aware Spectral Activation Compression for Efficient and Accurate Collaborative LLM Inference
摘要：利用早期 Transformer 层激活在低频域的能量集中性，对阶段边界激活执行二维 FFT，仅传输低频系数并在服务端重构。Llama 3 和 Qwen2.5 实验中，激活平均缩小 7.6 倍，平均准确率损失低于 0.3%，压缩时间相对 Top-k 降低 32 倍以上。
- 任务来源：[https://arxiv.org/abs/2510.16418](https://arxiv.org/abs/2510.16418)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [FourierCompress 原始论文](https://arxiv.org/abs/2510.16418)：用于支撑分层频域压缩方法与实验结果。

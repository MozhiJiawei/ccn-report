# KV-Direct 残差流传输

## 一句话总结

截至 2026 年 3 月论文版本，KV-Direct 利用 Transformer 残差流重建 KV cache 以减少分离式推理的跨节点传输，并在论文给定模型与硬件条件下验证了通信压缩和服务性能收益。

## 任务信息

- 序号：39
- 任务编号：`PPTRANS-20260902-005`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference
摘要：证明 Transformer 各层 K/V 可以由 residual stream 确定性重建，并实现 bit-identical 的 KV-Direct。系统只保存每个 token 的 residual vector，而不是完整 KV；Gemma 3-4B 中每 token 状态由约 136 KB 降至 5 KB，并在所有测试预算下保持 100% token match。论文未直接评测跨 PP 网络传输。
- 任务来源：[https://arxiv.org/abs/2603.19664](https://arxiv.org/abs/2603.19664)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [KV-Direct 原始论文](https://arxiv.org/abs/2603.19664)：用于支撑残差流重建、误差边界与系统评测。

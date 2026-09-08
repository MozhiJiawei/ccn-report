# RED-PIM：PIM Transformer 推理数据移动优化

截至 2026 年 7 月 23 日发布的 arXiv 预印本 v1，RED-PIM 是一种面向基于 PIM 的 Transformer 推理的算法—架构协同设计，通过将 attention 的跨 bank 数据移动从 `O(N²)` 降至 `O(N)`、把中间矩阵从 `N×N` 缩小为 `d×d`，在作者模拟评测中相对 baseline PIM implementation 实现 16.05%–99.99%、几何平均 66.42% 的推理时间降低，为长序列推理减少通信与容量压力，同时将结论边界限定于论文模型、数据集、近似策略和模拟硬件配置。

## 交付件

- `source_understanding_review.html`：SingleFile 离线来源理解报告。

## 来源与核验

- 原始来源：[RED-PIM: Reducing Data Movement for Transformers using Processing-in-Memory](https://arxiv.org/abs/2607.21731)
- 本报告仅分析 RED-PIM 原始论文，不包含同类方案对照。
- 原始报告已通过独立视觉 QA；SingleFile 归档导出成功，未归档 PDF、截图、XML、QA 记录或生成日志。
- `66.42%` 是论文相对其 baseline PIM implementation 报告的推理时间降低几何平均值，不应外推为所有 GPU、CPU、模型或生产部署的普适收益。

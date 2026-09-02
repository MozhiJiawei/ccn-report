# Feather 跨地域推理压缩

## 一句话总结

截至 2026 年论文版本，Feather 以学习式激活压缩降低跨地域 LLM 推理通信开销，并在论文给定网络、模型和服务负载下验证性能与质量取舍。

## 任务信息

- 序号：44
- 任务编号：`PPTRANS-20260902-010`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：Feather: Towards Network-Efficient Cross-Regional Inference
摘要：面向跨地域 WAN 上的流水线推理，在阶段边界加入轻量学习式 MLP codec，并保持原模型参数冻结。该方法将激活最多压缩 48 倍，准确率与原模型差距不超过 2%；在 10 Gbps、10 ms RTT 环境下端到端加速最高 4.96 倍。
- 任务来源：[https://doi.org/10.1145/3789240.3828744](https://doi.org/10.1145/3789240.3828744)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Feather ACM 论文记录](https://doi.org/10.1145/3789240.3828744)：用于支撑论文元数据与正式发表信息。
- [Feather 作者公开论文](https://www.ertza.me/files/feather/feather.pdf)：用于支撑方法细节、实验设置和量化结果。

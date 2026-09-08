# MemSpec：边缘设备的内存感知投机解码运行时

## 一句话总结

MemSpec 是 2026 年 LCTES 论文提出的边缘设备投机解码运行时，它通过上下文预测、Top-K 草稿驻留集和异步预取，把草稿选择与其内存可用性联合调度，在 8GB Jetson Orin Nano、batch 1、贪心解码的论文实验中相对 MAB-Async 将平均稳态生成吞吐提高 40.7% 并达到同内存约束动态 Oracle 的 95%–97%，用于降低非驻留草稿切换造成的等待和回退执行。

## 任务信息

- 序号：24
- 任务编号：TASK-20260827163558-4a01d2f6
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：MemSpec内存感知运行时提升边缘设备投机解码吞吐40.7%技术线索
- 任务来源：[https://arxiv.org/abs/2608.10362](https://arxiv.org/abs/2608.10362)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 MemSpec 的内存约束、预测与缓存调度机制、实验结果和证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices](https://arxiv.org/abs/2608.10362)：用于支撑草稿加载开销、预测引擎、缓存管理器、运行时控制器，以及 Jetson Orin Nano 上的稳态吞吐和端到端延迟实验边界。


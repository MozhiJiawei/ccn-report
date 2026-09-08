# RAC 参考感知激活压缩

## 一句话总结

截至 2026 年 8 月论文版本，RAC 利用参考激活减少拆分式 LLM 推理的中间激活传输，并在论文覆盖的模型、数据集与链路条件下验证通信压缩和任务质量边界。

## 任务信息

- 序号：42
- 任务编号：`PPTRANS-20260902-008`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：RAC: Reference-Aware Activation Compression for Communication-Efficient Split LLM Inference
摘要：面向本地—云端—本地的 split LLM 推理，用历史 token 片段、同轮重建状态和轻量预测器生成边界参考，再对对齐后的残差进行量化。三个模型和九组链路实验中，TTFT 改善 1.24–2.72 倍，TPOT 改善 1.01–2.79 倍，非困惑度任务分数变化为 −0.40 至 +2.50。
- 任务来源：[https://arxiv.org/abs/2608.04991](https://arxiv.org/abs/2608.04991)

## 交付件说明

- [RAC-参考感知激活压缩.html](./RAC-参考感知激活压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [RAC-参考感知激活压缩.pptx](./RAC-参考感知激活压缩.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [RAC 原始论文](https://arxiv.org/abs/2608.04991)：用于支撑参考感知编码机制、实验指标和证据边界。

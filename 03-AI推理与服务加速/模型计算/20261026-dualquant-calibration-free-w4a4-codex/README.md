# DualQuant

## 一句话总结

DualQuant是2026年10月9日发布的免校准后训练权重与激活量化方法，通过静态权重重建优化产生行列双尺度并支持MX与NVFP4格式，在RTX 4090上以Llama-3.1-8B、INT4 G64真packed W4A4短序列测试将端到端内存缩至BF16的约38%–40%、吞吐达到BF16的1.39–2.46倍，同时保留PPL 6.74高于BF16 5.61的质量代价。

## 任务信息

- 序号：295
- 任务编号：TASK-20261026154031-0cc16a9d
- 热点编号：HS-20261026-article1793000431589671
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：API指定分类null，自动分类；已加载03与09细则，主要贡献是免校准后训练模型压缩和线性层低位推理，03/模型计算直接承接。MX/NVFP4与RTX4090均为使用既有硬件和数值格式，不涉及新芯片、互联或硬件结构，因此不归09；KV仍BF16，不属KV Cache。无指定分类差异。
- 任务正文：DualQuant免校准双尺度量化支持MX与NVFP4，内存降2.61倍技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.13767)

## 交付件说明

- [DualQuant.html](./DualQuant.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [DualQuant.pptx](./DualQuant.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs（arXiv v1）](https://arxiv.org/abs/2610.13767v1)：支撑双尺度权重重建MSE求解、免校准激活重缩放、格式感知投影、MX/NVFP4假量化精度，以及Table3/AppendixI中的真实INT4部署、四工况峰值、内存/吞吐和精度损失边界。

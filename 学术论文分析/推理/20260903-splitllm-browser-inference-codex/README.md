# 浏览器内 SplitLLM 激活量化

## 一句话总结

截至 IEEE Access 2026 论文版本，SplitLLM 通过浏览器—服务器拆分推理与激活量化降低自回归 LLM 的传输负担，并在论文实验条件下报告延迟、流量与生成质量结果。

## 任务信息

- 序号：43
- 任务编号：`PPTRANS-20260902-009`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：In-Browser Split Inference for Autoregressive Large Language Models with Activation Quantization
摘要：提出浏览器 WebGPU—远端服务器协同的 SplitLLM，在两端维护 KV cache，并用离线校准、共享 scale 的 per-channel INT8 压缩边界 hidden state。传输载荷减半；带宽受限时 decode 加速 1.7–2.6 倍、prefill 加速 2.4–2.9 倍，困惑度相对 FP16 增幅约 0–7%。
- 任务来源：[https://doi.org/10.1109/ACCESS.2026.3720562](https://doi.org/10.1109/ACCESS.2026.3720562)

## 交付件说明

- [SplitLLM-浏览器拆分推理.html](./SplitLLM-浏览器拆分推理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [SplitLLM-浏览器拆分推理.pptx](./SplitLLM-浏览器拆分推理.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [SplitLLM 原始论文](https://doi.org/10.1109/ACCESS.2026.3720562)：用于支撑浏览器拆分架构、量化方法和评测结果。

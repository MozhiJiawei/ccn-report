# Diffuplex

## 一句话总结

NVIDIA于2026年10月13日发布的Diffuplex论文v1提出全双工语音语言模型，以自回归策略判断交互时机、以离散扩散并行生成回答，在单GB300、batch1、thinking的答案文本解码实验中报告13.0 token/forward和1872 token/s；代码和权重仍计划发布。

## 任务信息

- 序号：252
- 任务编号：TASK-20261021221010-0540b52b
- 热点编号：HS-20261021-article1792591811029754
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：指定分类null，自动选择04-AI模型/话音模型与模型架构；核心贡献为全双工语音模型的训练与架构解耦，解码吞吐是模型设计效果，故不以03-AI推理与服务加速/解码为主归属；无调用方指定分类差异。
- 任务正文：Diffuplex以离散扩散实现全双工语音建模，思考模式下每前向13.0 token、每秒1872 token技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.17780)

## 交付件说明

- [Diffuplex.html](./Diffuplex.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Diffuplex.pptx](./Diffuplex.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Full-duplex Spoken Language Modeling with Discrete Diffusion (arXiv:2610.17780v1)](https://arxiv.org/abs/2610.17780v1)：唯一核心来源；支撑AR交互/扩散响应双轴架构、三阶段训练、前缀承诺、VoiceBench与解码效率；限定GB300/batch1/thinking答案文本，保留BF16/FP8与13.0/10.15口径冲突，代码权重尚待发布。

# LEO 卫星协同 LLM 推理

## 一句话总结

截至 2026 年 4 月论文版本，该方案面向低轨卫星网络压缩与调度协同 LLM 推理通信，并在论文仿真条件下分别验证通信字节量、时延和任务质量结果。

## 任务信息

- 序号：50
- 任务编号：`PPTRANS-20260902-016`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：Communication-Efficient Collaborative LLM Inference over LEO Satellite Networks
摘要：将完整 LLM 拆分为多个子模型并部署到不同 LEO 卫星，通过星间链路顺序传输中间激活；联合优化模型切分位置与自适应激活压缩率，在星载内存和精度约束下最小化推理延迟。相较基线，通信开销最多降低 71%、推理延迟最多降低 42%，精度损失低于 1%。论文同时采用计算—通信重叠，因此其纯传输收益需与调度收益区分。
- 任务来源：[https://arxiv.org/abs/2604.04654](https://arxiv.org/abs/2604.04654)

## 交付件说明

- [LEO-卫星协同推理.html](./LEO-卫星协同推理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LEO-卫星协同推理.pptx](./LEO-卫星协同推理.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [LEO 协同推理原始论文](https://arxiv.org/abs/2604.04654)：用于支撑算法、卫星网络设置和分项实验结果。

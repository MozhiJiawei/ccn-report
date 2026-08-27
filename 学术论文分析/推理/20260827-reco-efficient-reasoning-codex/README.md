# ReCo：奖励协调的高效推理

## 一句话总结

ReCo 是 2026 年 8 月 5 日发布的奖励协调推理框架，它用 30M 参数过程奖励估计器在每个推理步骤联合调节 KV cache 保留、反思 token 抑制与置信度早停，在 3 个 7B–8B 模型、6 个数学与科学基准及单张 NVIDIA H20 的论文实验中相对 Full CoT 减少 37%–65% 生成 token 并实现 2.08–2.35 倍端到端加速，用于同时控制推理的记忆成本与生成长度。

## 任务信息

- 序号：22
- 任务编号：TASK-20260827163502-74b0088f
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：ReCo奖励协调压缩减少推理token 37%-65%，延迟降低2倍以上技术线索
- 任务来源：[https://arxiv.org/abs/2608.04771](https://arxiv.org/abs/2608.04771)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 ReCo 的问题、三项控制机制、实验结果与证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Fewer Tokens, Smaller Cache: Reward-Coordinated Efficient Reasoning](https://arxiv.org/abs/2608.04771)：用于支撑奖励协调 KV cache 压缩、反思抑制与早停方法，以及 token、延迟、准确率和显存实验边界。


# AcceptMoE：自调整专家集的 MoE 投机解码

## 一句话总结

AcceptMoE 是 2026 年 8 月 4 日发布的无需训练 MoE 投机解码验证器优化方法，它按草稿 token 的承诺概率自调专家集合并进行驻留感知裁剪，在单张 RTX 5090、batch size 1、每层 48 个专家物理卸载的论文实验中相对 Standard SD 将平均吞吐提升至 2.06 倍，同时把专家权重 H2D/token 降低 73.6%–77.1%，用于降低专家权重搬运对解码吞吐的限制。

## 任务信息

- 序号：21
- 任务编号：TASK-20260827163403-b4af71a7
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：AcceptMoE自调整专家集，MoE投机解码吞吐提升2.06倍技术线索
- 任务来源：[https://arxiv.org/abs/2608.02989](https://arxiv.org/abs/2608.02989)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 AcceptMoE 的问题、方法、实验结果与证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding](https://arxiv.org/abs/2608.02989)：用于支撑承诺概率加权、自调整专家集合、驻留感知裁剪方法，以及吞吐、H2D 流量和准确率证据边界。


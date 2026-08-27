# Skill Self-Play：让技能库驱动可验证自进化

## 一句话总结

Skill Self-Play 将 skill 从推理提示升级为同时封装任务条件、执行规则与验证接口的训练单元，用可演化技能库路由出题、有效性门控过滤候选、solver 成功率定位学习边界，再让 proposer、solver 与技能库共同更新；论文在 5 个 3B–14B backbone、工具调用与逻辑推理任务上均报告收益，最大绝对提升分别为 42.9 点和 12.0 点，但增益依赖具体基座、任务可验证性、训练配置与算力条件。

## 任务信息

- 序号：33
- 任务编号：TASK-20260827174614-3eda97c4
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：阿里巴巴联合多所高校提出Skill Self-Play框架，实现大模型自进化中任务多样性与验证可靠性的平衡技术线索
- 任务来源：[https://arxiv.org/pdf/2607.22529](https://arxiv.org/pdf/2607.22529)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释可演化技能库、双流出题、有效性门控、学习边界、共同进化、实验结果和落地边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Skill Self-Play 论文](https://arxiv.org/abs/2607.22529)：用于支撑方法定义、训练协议、主实验、消融、数据循环诊断和计算开销口径。
- [Qwen-Applications/skill-self-play](https://github.com/Qwen-Applications/skill-self-play)：用于核对公开实现、运行流程、依赖与复现边界。

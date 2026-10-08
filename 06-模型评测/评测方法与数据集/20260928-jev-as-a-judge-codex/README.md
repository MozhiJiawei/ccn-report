# JEV-as-a-Judge

## 一句话总结

CMU 团队于2026年9月发布的 arXiv v1 提出 JEV-as-a-Judge 低成本判官与固定置信度级联，让容易判断的样本由仅输出标签概率的模型处理、疑难样本升级强判官；其单次费用为对照判官的0.36%，级联在该版本实验中保留对照99%的准确率。

## 任务信息

- 序号：171
- 任务编号：DSH-20260924-020
- 热点编号：HS-20260924-dsh-tech-insight
- 周期：2026-W39
- 指定分类：由 AI 自动分类
- 实际归档分类：06-模型评测/评测方法与数据集
- 归类依据：主要贡献是模型判官的评测方法与置信度分流，不是通用模型本体或 Agent 工作流。
- 任务正文：📌CMU 团队发表 JEV-as-a-Judge：成本仅 SOTA 判官 0.36%，级联策略保 99% 准确率
原文标题：JEV-as-a-Judge: Accept When Confident, Escalate When Unsure
元信息：战略 · 2026/09/24 · 编号 #20 · 0.36%；Comparing jev-as-a-judge with sixteen generative a
要点：
- 与十六个生成式与奖励模型判官对比，并经盲法人类裁决，JEV-as-a-Judge 在普通偏好与证据可核验的事实性任务上距 SOTA LLM 判官（最强对照）仅 3 个百分点以内，费用为对照的 0.36%Comparing jev-as-a-judge with sixteen generative and reward-model judges, with blinded human adjudication, we find it within three percentage points of a state-of-the-art LLM judge, our strongest comparator, on ordinary preference and evidence-grounded factuality at 0.36% of the comparator's fee
- 采用冻结级联策略——接受高置信判定、转交不确定样本——以更低成本保留对照 99% 准确率A frozen cascade that accepts confident verdicts and escalates uncertain ones retains 99% of the comparator's accuracy at lower cost
技术效果：效果 · 基准性能：基准性能：据 arXiv:2609.26550：JEV 在普通偏好与证据可核验的事实性上距 SOTA LLM 判官仅 3 个百分点以内，成本为其 0.36%；据 arXiv:2609.26550：在 RewardBench 上 JEV 得 92.2% vs GPT-6 93.5%（配对差 −1.25，95% 簇区间 [−3.8, 1.5]），在 HaluEval 上 JEV 得 87.5% vs 86.7%（+0.83，95% 区间 [−1.25, 2.92]）；据 arXiv:2609.26550：冻结级联（接受高置信判定、转交不确定样本）保留判官 99% 准确率同时降低成本
背景补充：据 arXiv:2609.26550：论文由 CMU 团队（Yubo Li / Yidi Miao / Ramayya Krishnan / Rema Padman）2026/09/21 发表，比较对象包含十六个生成式与奖励模型判官并采用盲法人类裁决；JEV 差距集中在「需核验推导或抗住长篇错误答案」的低置信判定上。
源链接：https://arxiv.org/abs/2609.26550
- 任务来源：[原任务来源](https://arxiv.org/abs/2609.26550)

## 交付件说明

- [JEV-as-a-Judge.html](./JEV-as-a-Judge.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [JEV-as-a-Judge.pptx](./JEV-as-a-Judge.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [JEV-as-a-Judge arXiv v1](https://arxiv.org/abs/2609.26550v1)：用于核对任务引用的0.36%费用、99%级联准确率及实验边界。
- [JEV-as-a-Judge arXiv v4](https://arxiv.org/abs/2609.26550v4)：用于说明2026年10月修订后的41%费用与+0.9个百分点结论，避免与v1混用。

# Branch2Skill：用推理树提炼技能演化证据

## 一句话总结

Branch2Skill 是 2026 年 8 月发布的推理树技能演化框架，它在固定技能与搜索预算下用 MCTS 构建分支、沿精英路径比较共享前缀的同父兄弟决策，再通过可审计的新增/替换/删除补丁和验证集门接受或回滚更新，在 6 个基准、GPT-5.5 目标模型的论文汇总设置中相对 SkillOpt 将技能演化 token 从 526.7M 降至 141.3M（减少 73.2%）并把累计增益由 117.8 提高到 128.7，用于把一次搜索的替代尝试转成多步局部监督。

## 任务信息

- 序号：31
- 任务编号：TASK-20260827174457-9044a8e7
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：Branch2Skill框架利用推理树提升技能进化效率，token减少73.2%技术线索
- 任务来源：[https://arxiv.org/abs/2608.08677](https://arxiv.org/abs/2608.08677)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释推理树、同父兄弟证据、技能补丁、性能/迁移结果与成本边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Branch2Skill: Efficient Skill Evolution Through Reasoning Trees](https://arxiv.org/abs/2608.08677)：用于支撑 MCTS 推理树、共享前缀兄弟对照、技能补丁与验证回滚方法，以及相对 SkillOpt 的 token、累计增益和效率实验口径。


# JevProbe-程序决策劫持

## 一句话总结

2026年10月13日论文v1发布的JevProbe是面向开源Jev应用的程序决策劫持评估框架，通过追踪可达外部上下文、结构化判断和程序消费边界，在228个应用的2,273个案例中测出1,853次决策翻转（81.5%），用于识别格式合法判断引发的潜在下游安全风险。

## 任务信息

- 序号：271
- 任务编号：TASK-20261022153532-ed669e09
- 热点编号：HS-20261022-article1792654532739516
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：07-AI安全、可信与治理/AI系统攻防
- 归类依据：category原值null，依据全文自动归07/AI系统攻防：主贡献是低信任上下文攻击的可达性、结构化判断导致的程序决策翻转及潜在安全后果评估；02评测与可观测仅次要关联，无指定分类冲突。任务线索81.5%应用覆盖已按全文纠正为1853/2273案例率。
- 任务正文：JevProbe揭示Jev应用程序决策劫持，228个应用中81.5%出现决策翻转技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.18612)

## 交付件说明

- [JevProbe-程序决策劫持.html](./JevProbe-程序决策劫持.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [JevProbe-程序决策劫持.pptx](./JevProbe-程序决策劫持.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Nudge the Judge: Uncovering Program Decision Hijacking in Real-World Jev Applications](https://arxiv.org/abs/2610.18612v1)：固定2026-10-13 v1，支撑威胁模型、consumer决策翻转、Table2总体DFR、Table4共享子集比较及潜在安全后果。
- [JevProbe官方代码与JevProbeBench固定commit](https://github.com/xiaoxiaohg8d/JevProbe-/tree/9cec1be6ee57cc9872626222ba99739c8fcca610)：支撑冻结single-pass预算、影响判定门、精选Bench cap10/flips-first、分母及actual_damage_observed=null边界。

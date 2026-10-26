# FIBS-激活欺骗探针

## 一句话总结

2026年10月20日修订的Telling FIBS v4通过多层模型激活训练欺骗探针，在BashArena的Qwen3.5-397B-A17B同一步骤评估中，EFC相对Haiku5.5文本监控将AUROC由97.6%提升至98.0%，并将样本内1%误报率下的召回率由35%提升至73%，为智能体破坏监测提供需白盒权限与阈值校准的补充信号。

## 任务信息

- 序号：246
- 任务编号：TASK-20261021215122-2e49928e
- 热点编号：HS-20261021-article1792590683399025
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：07-AI安全、可信与治理/AI系统攻防
- 归类依据：category=null，自动归类；主贡献是LLM智能体欺骗/破坏检测，归AI系统攻防。02评测与可观测、06评测方法与数据集为次关联，07模型安全与可控不及具体Agent安全监测直接；无指定分类冲突。任务98.8%为v1旧数字；v4元数据98.3与PDF98.7未协调，主证据采用稳定Table9。
- 任务正文：探针在 SHADE-Arena 实现 98.8% AUC 检测 LLM 智能体欺骗与破坏技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.12445)

## 交付件说明

- [FIBS-激活欺骗探针.html](./FIBS-激活欺骗探针.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [FIBS-激活欺骗探针.pptx](./FIBS-激活欺骗探针.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Telling FIBS — arXiv v4](https://arxiv.org/abs/2610.12445v4)：2026-10-20论文版本、方法、训练数据、实验及限制；Table9精确BashArena配置；保留SHADE元数据与PDF冲突。
- [fibs-probes 官方实现固定提交](https://github.com/AlignmentResearch/fibs-probes/tree/6cae61deed78157021bf141c69f626881bbd638d)：官方推理架构和白盒激活输入契约；网页核验，未声称复现实验。

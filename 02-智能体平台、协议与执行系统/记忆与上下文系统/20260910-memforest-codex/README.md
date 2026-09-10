# MemForest

## 一句话总结

2026年9月8日发布的MemForest v1通过事件树划分和渐进合并压缩50%的历史记忆节点，使Mem0在未启用锚点检索时保留97.1%的原始平均性能，并在启用锚点检索的另一设置下取得1.89倍平均检索加速，为长期Agent记忆管理提供可复核的压缩方法。

## 任务信息

- 序号：114
- 任务编号：TASK-20260910205158-0534cb7b
- 热点编号：HS-20260910-article1789044718290398
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：任务category为null；已加载分类总则和02、03细则，主要改变对象为Agent历史记忆组织、压缩与检索，唯一主归属为记忆与上下文系统；检索加速并非模型计算或Serving加速，无指定分类差异。
- 任务正文：MemForest框架压缩Agent记忆50%并保持97%以上性能，实现近2倍检索加速技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.08273)

## 交付件说明

- [MemForest.html](./MemForest.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MemForest.pptx](./MemForest.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

论文v1作者实验，尚无独立复现；97.1%和99.7%为各自基线的相对平均性能保留率，不是准确率；50%为记忆节点压缩条件，不保证字节存储减半；1.89倍和2.24倍为检索阶段加速，不是端到端问答加速；合并存在额外LLM调用与信息损失风险。 摘要性能保留率为无AGPR设置，检索加速为启用AGPR设置；T-Time为每个query总检索耗时，各数据集加速倍数取平均。

## 引用信息源说明

- [MemForest: Efficient Agent Memory Management via EventTree Partitioning and Progressive Merging](https://arxiv.org/abs/2609.08273)：原始论文v1，支撑方法、实验条件、性能保留率、时延及局限性

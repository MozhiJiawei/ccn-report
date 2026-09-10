# CreaMem

## 一句话总结

CreaMem是2026年9月8日arXiv v1提出的个性化Agent长期记忆架构，通过生活、工作、兴趣分区和事件与特质双重编码，在GPT-4o-mini主实验中将LoCoMo的4o-Judge准确率提高至54.61%，较表内最强基线HippoRAG 2高8.99个百分点。

## 任务信息

- 序号：115
- 任务编号：TASK-20260910205216-904de9f2
- 热点编号：HS-20260910-article1789044736429484
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：主要改变对象为Agent长期记忆的组织、抽取和检索，直接归属记忆与上下文系统；category为null，自动分类，无指定值冲突。
- 任务正文：CreaMem场景感知记忆架构通过生活场景分区减少检索干扰并提升多跳推理技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.08550)

## 交付件说明

- [CreaMem.html](./CreaMem.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [CreaMem.pptx](./CreaMem.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

固定三场景分类不保证跨用户或专业领域泛化；主实验token数接近但并非严格相同；消融使用Gemini-3并关闭Core和二次检索，不能与GPT-4o-mini主表直接混比；平均查询延迟2.9秒高于A-Mem的1.98秒；写入成本未统一核算，仍会漏检关联证据或生成时无法组合证据。 论文Table1与附录Table3部分基线总体分数不同，提升仅按Table1计算；附录抽取审计存在6.4–9.6%的不支持中心陈述。

## 引用信息源说明

- [CreaMem: A Scene-Aware Memory Architecture for Personalized Agents](https://arxiv.org/abs/2609.08550)：唯一原始论文；方法、实验、图表、失效案例与局限，v1 2026-09-08

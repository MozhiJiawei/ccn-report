# WikiSkill-持久知识演化

## 一句话总结

Google Research等在2026年8月发布的WikiSkill论文v1通过在执行轨迹与可执行技能之间维护持久Wiki知识层，让智能体在不更新模型参数的情况下积累经验并以验证集门控演化技能，在五类基准和五个模型的论文测试中将Qwen-3.6-27B平均得分从39.4提高至63.3，为可复用技能开发提供可追溯的经验积累机制。

## 任务信息

- 序号：90
- 任务编号：TASK-20260910151910-31b06187
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：指定分类为null，由AI自动分类；核心贡献是在不可变执行轨迹与技能间新增持续累积的Wiki知识层，组织失败模式、成功策略与修改历史，并在技能回滚时保留经验，主改进对象为经验记忆及上下文组织，因此归入记忆与上下文系统；技能演化为下游用途，未引入新的工具执行器，也不更新模型参数。无调用方指定值差异。
- 任务正文：谷歌wiki skill
- 任务来源：[原始任务来源](https://arxiv.org/html/2608.27454v1)

## 交付件说明

- [WikiSkill-持久知识演化.html](./WikiSkill-持久知识演化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [WikiSkill-持久知识演化.pptx](./WikiSkill-持久知识演化.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

主结果为五模型×五基准、三次完整演化后的平均测试表现，非全部任务均提升；Wiki消融仅四任务，不能与五任务均值混用；训练/验证/测试分离，验证集反复门控且仅10–40项，技能全文注入不评估检索触发；O(1)仅为优化器API调用数对训练样本数的复杂度，不包括rollout、验证、token、时延或总费用；跨模型迁移可能负向；论文v1不等同已部署Google产品。

## 引用信息源说明

- [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution（arXiv:2608.27454v1）](https://arxiv.org/html/2608.27454v1)：唯一一手论文；支撑三层架构、门控与回滚、主实验、消融、数据划分及优化器API调用复杂度。
- [WikiSkill v1 原始PDF](https://arxiv.org/pdf/2608.27454v1)：同一论文PDF版本；用于GROBID与Docling结构解析、提取方法原图与实验原表并核对页码。

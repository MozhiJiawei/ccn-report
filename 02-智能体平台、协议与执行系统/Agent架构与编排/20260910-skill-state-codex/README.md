# SKILL.state

## 一句话总结

SKILL.state（arXiv:2608.26263v3，2026年9月2日）是Google LLC与Purdue University作者提出的长程Agent技能运行时架构，以固定技能规范、显式可变状态和最新观测驱动每步执行，在Gemini-3-Flash的InterCode CTF评测中达到54.2% pass@1，较最强已报基线提高7.8个百分点。

## 任务信息

- 序号：91
- 任务编号：TASK-20260910151954-6b52082e
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：主要改变对象是技能运行时的状态转移与执行语义，匹配Agent架构与编排的运行时状态管理；记忆与上下文为次要关联，不是参数训练或工具执行器改进。category为null，无指定值冲突。
- 任务正文：谷歌skill.state
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.26263)

## 交付件说明

- [SKILL.state.html](./SKILL.state.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [SKILL.state.pptx](./SKILL.state.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

作者报告的基准结果，未独立复现；常数上下文依赖状态与观测有界；schema遗漏的信息可能无法恢复；Retail平均prompt高于基线；Table5的tokens/characters预算单位标注不一致；不是Google官方产品发布，多Agent并发未实验验证。

## 引用信息源说明

- [SKILL.state: Scalable Long-Horizon Agent Skills（v3）](https://arxiv.org/abs/2608.26263v3)：唯一批准一手来源；支撑作者机构、状态转移架构、复杂度条件、仓库与公开交互基准结果以及局限性。

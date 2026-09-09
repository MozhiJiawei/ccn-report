# TRIAGE

## 一句话总结

TRIAGE 是面向重复工具任务的三层智能体路由框架，2026 年 9 月 1 日 arXiv v1 将成功执行轨迹组织为直接复用、参数化 Skill 与完整 ReAct 三条路径，在构造的 1,007 条 SQL 查询实验中报告 token 总量由 199,782 降至 75,238，为稳定重复工作负载减少模型调用提供依据，而跨域零 token 执行与普遍语义正确性仍待验证。

## 任务信息

- 序号：60
- 任务编号：TASK-20260908172744-1fad62b1
- 热点编号：HS-20260901-article123457
- 周期：2026-W36
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：主要贡献是根据历史轨迹和 Skill 条件决定任务执行路径的三层路由与回退编排；轨迹记忆是支撑机制，未改变模型推理内核。
- 任务正文：TRIAGE三层路由框架通过轨迹复用实现LLM智能体零token成本执行
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.01428)

## 交付件说明

- [TRIAGE.html](./TRIAGE.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [TRIAGE.pptx](./TRIAGE.pptx)：基于已验收来源理解报告的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution](https://arxiv.org/abs/2609.01428v1)：支撑三层路由、轨迹到 Skill 的提取机制、SQL 和 ToolBench 实验；明确二判调用成本、ToolBench L2 的模型调用、执行成功与语义正确性差别及表文口径冲突。

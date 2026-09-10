# WorkSwarm-永续会话

## 一句话总结

截至2026年9月10日，WorkSwarm在openJiuwen官方仓库提交029c76a的永续会话实现中，以追加式原始记录、后台语义抽取和游标一致的上下文替换延续项目约定，并提供25个组件×8阶段、含5个隐藏冲突探针的200任务验收框架，但本轮未取得对应运行结果。

## 任务信息

- 序号：118
- 任务编号：TASK-20260910205326-0788424b
- 热点编号：HS-20260910-article1789044806613456
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：主要改变对象为外部工作记忆、原始证据追溯和跨轮上下文生命周期；Extractor与Builder分工服务于记忆系统，验收驱动为辅助证据，故归记忆与上下文系统。category为null，无指定分类冲突。
- 任务正文：华为openJiuwen推出WorkSwarm永续会话，Agent长程任务200轮全部完成技术线索
- 任务来源：[原始任务来源](https://www.jiqizhixin.com/articles/2026-09-08-6?source=rss)

## 交付件说明

- [WorkSwarm-永续会话.html](./WorkSwarm-永续会话.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [WorkSwarm-永续会话.pptx](./WorkSwarm-永续会话.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

未取得公开的对应proof.json或独立复现结果；任务线索中的200/200、54次整理、189轮多人协作均不作为已证实实测指标。源码存在与验收条件不代表实验成功，也不保证抽取语义无遗漏。

## 引用信息源说明

- [Eternal Conversation Memory 官方实现说明](https://github.com/openJiuwen-ai/jiuwenswarm/blob/029c76a64d4b2c754ae29aa5e4e8985f80d5673f/.doc_project_maintainer/project/flows/eternal-conversation-memory.md)：Raw History、Extractor/Builder职责、游标替换与恢复机制
- [永续会话200任务官方验收驱动](https://github.com/openJiuwen-ai/jiuwenswarm/blob/029c76a64d4b2c754ae29aa5e4e8985f80d5673f/scripts/acceptance/eternal_conversation_200.py)：真实模型配置、逐任务门禁、hash链校验与proof输出定义
- [200任务工作负载定义](https://github.com/openJiuwen-ai/jiuwenswarm/blob/029c76a64d4b2c754ae29aa5e4e8985f80d5673f/scripts/acceptance/eternal_conversation_200_workload.py)：静态核实25组件×8阶段、5个冲突探针
- [WorkSwarm 官方产品页](https://www.openjiuwen.com/workswarm)：产品定位、上下文瘦身和分层记忆能力

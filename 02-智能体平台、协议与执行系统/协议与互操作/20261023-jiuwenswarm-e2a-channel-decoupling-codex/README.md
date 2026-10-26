# JiuwenSwarm-E2A

## 一句话总结

截至2026年10月23日，JiuwenSwarm以Gateway适配外部渠道、以E2A信封统一内部请求及流式响应，将任务交给AgentServer执行并向原渠道返回结果，使渠道接入与任务执行形成清晰的协议边界。

## 任务信息

- 序号：261
- 任务编号：TASK-20261021222617-b96dc9d3
- 热点编号：HS-20261021-article1792592777896284
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/协议与互操作
- 归类依据：API category=null，自动分类。正文主问题是外部渠道经Gateway转换为E2A统一信封并映射返回，主要改变对象为Agent协议和互操作，因此归02/协议与互操作；多Agent编排仅框架背景，不归Agent架构与编排；没有正式标准工作项或生态治理贡献，不归11。无指定分类差异。
- 任务正文：华为开源 JiuwenSwarm 多智能体框架，以 E2A 协议解耦外部渠道技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/gdia4ujt72z9yxbcf9ozlk4v9)

## 交付件说明

- [JiuwenSwarm-E2A.html](./JiuwenSwarm-E2A.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [JiuwenSwarm-E2A.pptx](./JiuwenSwarm-E2A.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [JiuwenSwarm官方README](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/README_CN.md)：项目定位、多Agent协作与多端接入背景。
- [E2A协议说明](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/docs/zh/E2A-protocol.md)：内部信封字段、响应顺序与结束和成功的语义区分。
- [A2A集成指南](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/docs/en/A2A.md)：外部入站A2A到Gateway、Message、E2A、AgentServer的映射与出站缺口。
- [E2A models兼容转发源码](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/jiuwenswarm/common/e2a/models.py)：核心实现已迁到openjiuwen_protocol，纠正文档真源路径漂移。
- [项目依赖锁定](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/pyproject.toml)：独立协议包及edfdae9a8a876b7a15dbf6bce501b929d235b6dc版本身份。
- [A2AChannel源码](https://github.com/openJiuwen-ai/jiuwenswarm/blob/d32f11029465676e50d2aa066064c6dfa3729eb0/jiuwenswarm/gateway/channel_manager/protocol/a2a/a2a_connect.py)：默认enabled=false及可选依赖配置边界。

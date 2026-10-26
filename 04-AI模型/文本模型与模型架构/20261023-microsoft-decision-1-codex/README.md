# Decision-1

## 一句话总结

2026年10月9日发布的Microsoft-Decision-1是微软基于Qwen3.5-9B后训练的文本决策评分模型，面向Foundry及集成应用以固定选项概率支持分类、路由与评分，在微软36基准（147,137题）比较中取得83.5%平均得分、Foundry同区域测试85ms中位延迟，为高频结构化判断提供低延迟模型选项。

## 任务信息

- 序号：255
- 任务编号：TASK-20261021221229-b5e6ca01
- 热点编号：HS-20261021-article1792591949897631
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：category=null，已读取分类总则与04/02/03细则。正文主要对象是专用文本决策模型的发布、输出接口和模型能力，归04-AI模型/文本模型与模型架构；路由是应用用途而非Agent编排系统，85ms是结果而非Serving优化方法。与指定约束无判断差异。
- 任务正文：微软发布Decision-1决策模型，基于Qwen3.5-9B，83.5%准确率85ms延迟技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/b2p5q0fcdxo2gy7drxhseo2g0)

## 交付件说明

- [Decision-1.html](./Decision-1.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Decision-1.pptx](./Decision-1.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Introducing Microsoft-Decision-1](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)：支撑2026-10-09发布、Qwen3.5-9B后训练、固定选项单次评分，以及厂商36基准、延迟、校准和扰动结果及脚注边界。
- [Deploy and use Microsoft-Decision-1 in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)：支撑state与noul/choice/score接口语义、Foundry部署、校准局限和cannot tell建议，不承诺内建拒答保证。
- [Microsoft Decision-1 now available on AI Gateway](https://vercel.com/changelog/microsoft-decision-1-now-available-on-ai-gateway)：支撑2026-10-09 Gateway接入、共享输入多问题和无独立Azure部署要求，仅作集成佐证，不作独立性能验证。

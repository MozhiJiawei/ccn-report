# Decision-1-结构化决策

## 一句话总结

微软于2026年10月9日发布的Decision-1是面向应用分类、路由与评分的Qwen3.5-9B后训练文本决策模型，以单次评分返回固定选项概率，在厂商36基准评测中取得83.5%平均得分，并在Foundry同区域测得85毫秒p50延迟。

## 任务信息

- 序号：279
- 任务编号：TASK-20261026144914-3519b34b
- 热点编号：HS-20261026-article1792997355134057
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：指定分类为null，按报告主贡献自动归类：对象是后训练并发布的纯文本决策模型本体，Agent控制为下游应用，85ms为模型效果而非独立Serving优化；与02-Agent架构候选比较后，04文本模型更匹配。
- 任务正文：微软发布Decision-1决策模型，基于Qwen3.5-9B，83.5%准确率85ms延迟技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/b2p5q0fcdxo2gy7drxhseo2g0)

## 交付件说明

- [Decision-1-结构化决策.html](./Decision-1-结构化决策.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Decision-1-结构化决策.pptx](./Decision-1-结构化决策.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Introducing Microsoft-Decision-1, our model for fast decision-making](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)：支撑发布时间、Qwen3.5-9B后训练、单次评分、厂商基准83.5%与Foundry同区85ms及证据边界。
- [Deploy and use Microsoft-Decision-1 in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-microsoft-decision)：支撑state与三类typed questions、API接入、应用阈值与本地评测建议。
- [Microsoft-Decision-1 official model card](https://ai.azure.com/catalog/models/Microsoft-Decision-1?publisher=microsoft)：支撑32768上下文、文本输入JSON输出、Preview状态（10月26日核对）与范围边界。

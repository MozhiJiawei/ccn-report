# Sparrow-2

## 一句话总结

Tavus于2026年8月27日发布的Sparrow-2是面向实时语音代理的音频原生会话理解模型，通过联合建模语义、韵律、说话人及背景声场决定何时听、等待或发言，在截至2026年9月10日官方公开的TurnBench开发集初步评测中取得92.4%的回合结束召回与97.4%的打断召回，用于改善自然轮次交接。

## 任务信息

- 序号：84
- 任务编号：TASK-20260910145214-327da3da
- 热点编号：HS-20260910-article1789023134602381
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：正式研究核心是音频原生流式会话理解模型及其编码器、六层因果Transformer与会话状态联合建模；虽用于Tavus视频会话产品，但Sparrow-2本体输入为音频，不因平台含视频改归多模态或AI应用。
- 任务正文：Tavus 推出 Sparrow-2，语音 AI 对话时机失败率降至 2.1%技术线索
- 任务来源：[原始任务来源](https://www.me.news/news/308388)

## 交付件说明

- [Sparrow-2.html](./Sparrow-2.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Sparrow-2.pptx](./Sparrow-2.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

当前官方正文不能复核任务历史2.1%指标；7.6%为回合结束未触发比例，不是总体对话失败率。结果为官方TurnBench dev初步自报，非私有test或独立复现；7ms计算耗时不是端到端响应时延。

## 引用信息源说明

- [Sparrow-2原始技术来源](https://www.tavus.io/blog/sparrow-2)：支持技术机制、实验设置、量化结果和证据边界。

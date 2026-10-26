# Decision3.0

## 一句话总结

截至2026年10月23日核验，Decision 3.0旗舰d3是vLLM Semantic Router开放的多模态决策模型，将文本、图片和视频中的预设问题转为候选答案概率，并在单张MI325X、AutoModel温态单请求1问条件下报告54.4毫秒文本中位时延。

## 任务信息

- 序号：254
- 任务编号：TASK-20261021221134-a6c78e23
- 热点编号：HS-20261021-article1792591894733750
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/多模态模型与模型架构
- 归类依据：指定分类原值null，按正式全文自动归类。核心交付是开放多模态决策模型本体，输入覆盖图像与视频，故归04-AI模型/多模态模型与模型架构。已对照03请求与调度与02 Agent架构细则：路由和工作流只是使用场景，正文并非Serving队列调度或Agent执行运行时。无指定值差异。报道0.3.1、模型卡引用0.3.2和当前0.4.1分开展示，历史榜一不表述为当前排名，亦未混入d3-turbo估算。
- 任务正文：vLLM Semantic Router开源Decision 3.0决策模型，d3登顶Jev决策榜技术线索
- 任务来源：[原始任务来源](https://zhidx.com/p/600073.html)

## 交付件说明

- [Decision3.0.html](./Decision3.0.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Decision3.0.pptx](./Decision3.0.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [d3官方模型卡（固定revision）](https://huggingface.co/vllm-sr/d3/blob/20f37b9a892acc13d4b07a4f3c4f11b2518c615c/README.md)：支撑多模态输入、Choice/YesNo/Score、每问题独立forward、基座与许可、历史0.3.2成绩及速度测试条件。
- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index)：核验2026-10-22更新的0.4.1榜单、d3 v3.1.0条目与Full score定义，限定当前与历史版本边界。
- [vLLM Semantic Router官方仓库（固定commit）](https://github.com/vllm-project/semantic-router/blob/18e71708fa534aac656644a173348ca6596b1beb/README.md)：支撑harness保留Agent流程、工具和状态而Router选择配置后端的系统职责边界。

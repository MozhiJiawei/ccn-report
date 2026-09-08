# AgentSysBench：智能体工作负载与服务系统分析

## 一句话总结

AgentSysBench 是 2026 年 8 月 15 日发布的智能体服务工作负载基准与统一观测框架，它覆盖 10 类应用、4,641 个受控请求及 24 小时内 178,799 个生产会话，用于刻画模型、工具、状态和通信的全链路瓶颈，并在 Dynamic RAG、相同 GPU 数和 0.5×/0.7×/0.9× 峰值吞吐负载的概念验证中通过任务拆分把平均延迟分别降低 40%/38%/29%。

## 任务信息

- 序号：20
- 任务编号：TASK-20260827150659-bda2d70e
- 热点编号：HS-20260815-article135718
- 周期：2026-W33
- 任务正文：AgentSysBench揭示智能体工作负载特性，任务感知服务降低延迟29-40%
- 任务来源：[https://arxiv.org/abs/2608.15127](https://arxiv.org/abs/2608.15127)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 AgentSysBench 的工作负载模型、测量框架、系统发现与证据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](https://arxiv.org/abs/2608.15127)：用于支撑 10 类应用的统一观测框架、受控与生产轨迹规模、六类工作负载特征，以及任务拆分服务的延迟实验边界。


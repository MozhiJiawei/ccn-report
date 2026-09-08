# CASCADE：SLO 感知的延迟预算调度与缓存协同

## 一句话总结

CASCADE 是 2026 年 8 月 6 日发布的 LLM 推理服务调度框架，它以“服务级目标上限减预测剩余服务时间”计算逐请求延迟预算，并让排序、分层 KV 恢复和抢占共享同一预算信号，在论文评估的 3 种大模型与 10 类生产派生 traces 中相对 vLLM 先来先服务基线最高实现 2.4 倍 SLO 内有效吞吐并将 SLO 违约率最多降低 40%，用于在不同请求紧迫度下协调计算和缓存搬运成本。

## 任务信息

- 序号：25
- 任务编号：TASK-20260827163624-8d91b6ca
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：Cascade调度器利用SLO感知延迟预算，将LLM推理goodput提升2.4倍技术线索
- 任务来源：[https://arxiv.org/abs/2608.06557](https://arxiv.org/abs/2608.06557)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释延迟预算、调度与 KV 协同机制、性能与公平性证据和外推边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Cascade: Exploiting SLO-Aware Latency Budget for Fair and High Goodput LLM Inference Serving](https://arxiv.org/abs/2608.06557)：用于支撑逐请求延迟预算、双层队列、KV 预取与抢占机制，以及多模型、多 traces 下的 goodput、SLO 违约与公平性实验边界。


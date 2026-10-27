# NIXL-Push-异步KV传输

## 一句话总结

vLLM于2026年10月14日公布面向P/D分离推理的NixlPushConnector，通过Decode提前登记目的KV块与Prefill后台线程提交WRITE减少协调和主循环阻塞，在Qwen3-32B、1P1D、H200/EFA、128输出token且Decode前缀缓存关闭的官方测试中，于8 QPS与16k输入下将TTFT从约1744 ms降至540 ms（官方概括最高约3倍改善），适用于可提前选定Decode实例的低延迟服务。

## 任务信息

- 序号：294
- 任务编号：TASK-20261026153432-6ae84633
- 热点编号：HS-20261026-article1793000073057508
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：直接改进PD分离中KV缓存的目的块登记、异步请求配对和传输提交；PD部署与H200/EFA是应用和实验背景，非云资源管理主体。 无指定分类冲突（null自动分类）；未选择推理部署，因为优化直接作用于KV传输协议与线程。
- 任务正文：vLLM 推出推送式 NIXL KV 传输，TTFT 最高改善 3 倍技术线索
- 任务来源：[原始任务来源](https://vllm.ai/blog/2026-10-14-nixl-push-connector)

## 交付件说明

- [NIXL-Push-异步KV传输.html](./NIXL-Push-异步KV传输.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NIXL-Push-异步KV传输.pptx](./NIXL-Push-异步KV传输.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Push-Based KV Transfer to Improve TTFT and TPOT for Disaggregated Inference in vLLM](https://vllm.ai/blog/2026-10-14-nixl-push-connector)：2026-10-14发布；协议/线程架构、官方6张原图、1P1D基准及复现环境、提前选D与单向KV边界。

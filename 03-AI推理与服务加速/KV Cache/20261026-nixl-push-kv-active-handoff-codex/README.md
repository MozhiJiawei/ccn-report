# NIXL-Push-KV主动交接

## 一句话总结

vLLM于2026年10月14日公布NIXL Push KV传输连接器，通过Decode提前登记目标块、Prefill后台WRITE及双事件就绪匹配缩短P/D分离推理交接路径，在Qwen3-32B、1P1D、H200/EFA官方测试中相对Pull最高改善约3倍TTFT与30% TPOT，收益随负载与配置变化。

## 任务信息

- 序号：293
- 任务编号：TASK-20261026153432-34c877df
- 热点编号：HS-20261026-article1793000072391672
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：API分类为null，自动分类；直接贡献为KV缓存目的块登记、双事件匹配、WRITE及后台传输准备机制，PD分离是部署环境而非新拓扑设计，依据03细则KV机制归KV Cache。无指定分类差异。
- 任务正文：vLLM 推出推送式 NIXL KV 传输，TTFT 最高改善 3 倍技术线索
- 任务来源：[原始任务来源](https://vllm.ai/blog/2026-10-14-nixl-push-connector)

## 交付件说明

- [NIXL-Push-KV主动交接.html](./NIXL-Push-KV主动交接.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NIXL-Push-KV主动交接.pptx](./NIXL-Push-KV主动交接.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Push-Based KV Transfer to Improve TTFT and TPOT for Disaggregated Inference in vLLM](https://vllm.ai/blog/2026-10-14-nixl-push-connector)：唯一获批一手来源，支撑协议、线程、原始6图、实验条件、性能及提前选D与双向传输边界。

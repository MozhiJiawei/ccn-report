# DeferKV-延迟淘汰

## 一句话总结

2026年10月5日发布的DeferKV v1是面向长上下文大模型推理的一次性KV缓存压缩方法，通过将淘汰推迟到处理首个生成token时并融合真实解码注意力，无需额外训练，在Llama-3.1-8B、每层1024个prompt KV位置预算下将RULER的11任务与4K至128K六长度平均准确率从最强压缩基线LAQ的75.31提高至81.36，相对提升8.03%。

## 任务信息

- 序号：290
- 任务编号：TASK-20261026152221-0a9bcb3b
- 热点编号：HS-20261026-article1792999341496182
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：API分类为null，由AI自动分类；正文主要贡献是一次性KV缓存淘汰时机与prompt KV重要性估计，首个decode提供观测信号，未改变token采样或投机生成算法，依03细则“KV机制归KV Cache”归入该二级，与指定值无差异。
- 任务正文：DeferKV 把 KV 缓存淘汰推迟到首个解码步以提升长上下文性能技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.06286)

## 交付件说明

- [DeferKV-延迟淘汰.html](./DeferKV-延迟淘汰.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [DeferKV-延迟淘汰.pptx](./DeferKV-延迟淘汰.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [DeferKV: Rethinking Eviction Timing for One-Shot KV Cache Compression (arXiv:2610.06286v1)](https://arxiv.org/abs/2610.06286v1)：唯一一手来源，支撑真实首decode时序、时间加权与每层预算机制、LongBench/RULER指标及相对分母、效率配置、峰值显存与质量损失边界。

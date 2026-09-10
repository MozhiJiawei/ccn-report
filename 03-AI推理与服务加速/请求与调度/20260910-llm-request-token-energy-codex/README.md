# LLM-请求与Token能耗

## 一句话总结

2026年8月28日arXiv v1论文对H100/H200上的LLM推理建立请求窗口与单位token双口径能耗表征，在H200的Llama-3.2-1B、batch16及4K上下文下，输出10增至512个token使7.46降至0.72 J/token而整批窗口能耗由1.19升至5.93 kJ，说明节能Serving须同时评估绝对能耗与平均效率。

## 任务信息

- 序号：78
- 任务编号：ISSUE36-20260910-002
- 热点编号：HS-20260910-llm-inference-energy
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/请求与调度
- 归类依据：直接研究推理请求形状、输出长度和batching对能耗的影响，服务请求与调度是主要应用对象；不是数据中心供电设施或通用软件成本治理。
- 任务正文：卡内基梅隆大学研究揭示LLM推理能耗真相：每Token能耗降低不代表总能耗减少技术线索

线索来源：https://github.com/MozhiJiawei/Mozhi-s-AgentWorkspace/issues/36
Issue 所附来源：http://mp.weixin.qq.com/s?__biz=MzAxMjYyMzcwNA==&mid=2247494264&idx=1&sn=11fc998086d92d58ca86846d8241a338&chksm=9aa5f102d7e0680e075e73b68271bb5b2b53beb491eb6b7dac8096786af0a6b16be74c3bb4c5&scene=0&xtrack=1#rd
论文主来源：https://arxiv.org/abs/2608.28044
来源核对备注：机构与核心结论匹配；微信报道触发验证，尚未核实报道内论文链接。单位 Token 能耗与整批推理窗口能耗需区分。
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.28044)

## 交付件说明

- [LLM-请求与Token能耗.html](./LLM-请求与Token能耗.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LLM-请求与Token能耗.pptx](./LLM-请求与Token能耗.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

证据边界：kJ为整批推理窗口而非单请求，NVML测量不代表整机或机房能耗；跨H100/H200的平台差异不能单归因于显存。恢复后XML与12图校验通过，图6和表VIII/IX未导出的缺口已披露。

## 引用信息源说明

- [Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms](https://arxiv.org/abs/2608.28044v1)：支持双口径能耗模型、H100/H200实验、批处理/上下文/输出长度的作用与测量边界。

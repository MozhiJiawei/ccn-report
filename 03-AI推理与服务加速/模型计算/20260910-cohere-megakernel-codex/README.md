# Cohere-Megakernel

## 一句话总结

Cohere 于2026年9月8日发布面向 North Mini Code 的开源 Megakernel 推理研究系统，将解码前向计算融合为常驻 GPU 内核，在单张 H100、BF16 条件下实现 BS=1 解码吞吐292 token/s（vLLM v0.24的1.58倍），BS=8端到端服务实验中平均解码吞吐提升至1.25–1.41倍。

## 任务信息

- 序号：112
- 任务编号：TASK-20260910205048-4a7bc0b0
- 热点编号：HS-20260910-article1789044648950811
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：指定分类为null，由AI自动分类；主要贡献是持久CUDA内核中的tile级算子融合、细粒度依赖同步和权重预取，归模型计算。decode为执行阶段，未改变采样或投机解码算法；连续批处理为配套服务能力，因此不归解码或请求与调度。无指定值差异。
- 任务正文：Cohere 发布基于 decode megakernel 的开源 LLM 推理服务系统，性能最高比 vLLM 快 1.58x技术线索
- 任务来源：[原始任务来源](https://x.com/cohere/status/2097410772355666393)

## 交付件说明

- [Cohere-Megakernel.html](./Cohere-Megakernel.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Cohere-Megakernel.pptx](./Cohere-Megakernel.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

早期研究发行，当前仅North Mini Code、单H100/SM90a、BF16、batch 1–8，CUDA13+、Python3.12+、Linux；prefill仍为独立PyTorch算子且暂停decode；1.58倍仅BS=1 decode-only，BS=8完整服务负载的平均decode吞吐为1.25–1.41倍；属于作者报告，未独立复现。 完整服务实验的加速指标为平均解码吞吐，输出token数不同，不能等同wall-clock延迟缩短；官方SciCode行711/560约1.27倍却标1.37倍，待作者确认。

## 引用信息源说明

- [Inside the megakernel serving engine for North Mini Code](https://cohere.com/blog/megakernels)：官方技术博客，支撑2026-09-08发布、持久内核机制、原始图示与性能数据
- [cohere-ai/cohere-megakernel](https://github.com/cohere-ai/cohere-megakernel)：官方代码仓库，支撑实现、复现配置、版本对照和研究发行限制

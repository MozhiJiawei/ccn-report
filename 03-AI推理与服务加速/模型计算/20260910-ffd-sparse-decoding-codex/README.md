# FFD-长上下文稀疏解码

## 一句话总结

2026年8月31日arXiv v1论文提出FFD，以低比特Key粗扫、top-δ筛选和GPU内核融合减少长上下文解码的数据搬运，在RTX 4090单batch微基准报告最高11.63倍内核加速，为Llama/Qwen GQA模型提供需结合任务质量校准的稀疏解码路径。

## 任务信息

- 序号：79
- 任务编号：ISSUE36-20260910-003
- 热点编号：HS-20260910-faster-flash-decoding
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：优化现有GPU上的稀疏attention算子及执行路径，主要贡献归模型计算；不改变采样策略，也不提出新芯片架构。
- 任务正文：FFD通过硬件-算法协同设计实现长上下文解码11.6倍加速技术线索

线索来源：https://github.com/MozhiJiawei/Mozhi-s-AgentWorkspace/issues/36
Issue 所附来源：https://arxiv.org/abs/2609.00097
论文主来源：https://arxiv.org/abs/2609.00097
来源核对备注：Issue 原始论文链接完全一致。11.6 倍为内核级加速，端到端吞吐提升为 2.37 倍。
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.00097)

## 交付件说明

- [FFD-长上下文稀疏解码.html](./FFD-长上下文稀疏解码.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [FFD-长上下文稀疏解码.pptx](./FFD-长上下文稀疏解码.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

证据边界：11.63倍为内核峰值；正文最高2.37倍端到端加速与图4柱标存在不一致。RULER测评有分数下降，不能称无损；256K仅为内核微基准范围。解析保留完整GROBID、部分Docling产物及原始PDF图表，未声称完整Docling解析成功。

## 引用信息源说明

- [Faster Than Flash: Exploiting Attention Sparsity for Efficient Long-Context Decoding](https://arxiv.org/abs/2609.00097v1)：支持FFD机制、内核与端到端速度、RULER/LongBench质量、消融及正文与图4数值差异。

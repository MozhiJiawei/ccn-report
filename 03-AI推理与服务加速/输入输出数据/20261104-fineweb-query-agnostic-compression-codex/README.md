# FineWeb任务无关文本压缩

## 一句话总结

2025年12月25日 arXiv v1 的 FineWeb 实验以已有指令模型在不接收问题的情况下将15k–28k token网页压为可读摘要，再由预测器接收问题和摘要，在100篇网页的合成任务上观察到较大压缩器降低答案困惑度但增加计算量，未给出该分支精确压缩长度曲线。

## 任务信息

- 序号：333
- 任务编号：iclr2026-isFHz8qf20
- 热点编号：context-compression
- 周期：2026-W45
- 指定分类：03-AI推理与服务加速/输入输出数据
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：严格遵循指定二级。报告聚焦FineWeb query-agnostic原始网页输入压缩，直接改变下游输入文本；整篇论文含任务相关压缩与记忆摘要，但本报告限定分支，分类判断无差异。
- 任务正文：论文：Agentic Collaboration as an Information Bottleneck Problem。arXiv 2512.21720v1 页面标题：An Information Theoretic Perspective on Agentic System Design。

本次选题聚焦上下文压缩中的第一类：语义无关硬压缩，具体指任务/问题无关（query-agnostic）的原文上下文压缩。重点分析 FineWeb 实验：压缩器只接收原始网页文本，不接收下游问题，输出可读文本；下游预测器随后接收问题与压缩文本。核对压缩器提示词、实验设置、压缩长度与下游效果/成本的实证关系。

范围边界：不要将 WildChat 对话记忆摘要实验归入此类；区分 query-specific 与 query-agnostic 两种分支。不要将整篇论文或所有实验笼统视为任务无关压缩，也不要把对已有模型的信息效率与缩放关系研究表述为提出了专门的新压缩算法。报告应以论文原文及实验证据为准，明确该分支对第一类上下文压缩的适用范围。

重点原文：
压缩器提示词 C.1：https://arxiv.org/html/2512.21720v1#A3.SS1
下游预测器提示词 C.2：https://arxiv.org/html/2512.21720v1#A3.SS2
FineWeb 实验设置 D.1.5：https://arxiv.org/html/2512.21720v1#A4.SS1.SSS5
FineWeb 结果 E.1.3：https://arxiv.org/html/2512.21720v1#A5.SS1.SSS3
会议来源：https://openreview.net/forum?id=isFHz8qf20
- 任务来源：[原始任务来源](https://arxiv.org/html/2512.21720v1#A5.SS1.SSS2)

## 交付件说明

- [FineWeb任务无关文本压缩.html](./FineWeb任务无关文本压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [FineWeb任务无关文本压缩.pptx](./FineWeb任务无关文本压缩.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [An Information Theoretic Perspective on Agentic System Design — arXiv:2512.21720v1](https://arxiv.org/html/2512.21720v1)：C.1/C.2核对问题输入位置与纯文本摘要；D.1.5核对FineWeb 100篇15k–28k tokens、每篇2抽取+3创作的合成任务；D.2核对4096输出cap；E.1.3/Figure12支持PPL与GFLOPs趋势、图注坐标冲突及长度证据边界。。

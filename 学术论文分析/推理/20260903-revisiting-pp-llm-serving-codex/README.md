# 重访 LLM Serving 流水线并行

## 一句话总结

截至 OSDI 2026 论文版本，该研究以动态 prefill 分块和 decode 延迟调度降低在线 LLM 流水线气泡，在 4×A100 PCIe 实验中使 SLO goodput 相对固定流水线和张量并行显著提升。

## 任务信息

- 序号：54
- 任务编号：`PPTRANS-20260902-020`
- 热点编号：PP推理传输优化｜无损/严格等价
- 周期：2026-09
- 任务正文：方法类别：无损/严格等价
论文名：Revisiting Pipeline Parallelism for LLM Serving
摘要：重新评估在线 LLM 服务中的 PP，指出预填充和解码负载变化会放大阶段间计算不均衡。论文通过动态调整 chunk 大小以及延迟调度、跨阶段再平衡解码负载来减少流水线气泡，并在 SGLang 上证明其 PP 配置可优于 TP。它主要优化 PP 调度而非传输字节数，但属于顶会系统工作，可作为传输优化方案的关键对照基线。
- 任务来源：[https://www.usenix.org/conference/osdi26/presentation/hwang](https://www.usenix.org/conference/osdi26/presentation/hwang)

## 交付件说明

- [LLM-Serving-动态流水线调度.html](./LLM-Serving-动态流水线调度.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LLM-Serving-动态流水线调度.pptx](./LLM-Serving-动态流水线调度.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [OSDI 2026 原始论文](https://www.usenix.org/system/files/osdi26-hwang.pdf)：用于支撑动态调度方法、实验设置和量化结果。
- [USENIX 官方论文页](https://www.usenix.org/conference/osdi26/presentation/hwang)：用于支撑正式发表信息与作者元数据。

# 稠密 LLM 并行化策略评测

## 一句话总结

截至 2026 年 3 月论文版本，该研究在指定硬件、模型与应用负载上实证比较稠密 LLM 的张量、流水线及其他并行化策略，为按瓶颈选择部署方案提供量化基线。

## 任务信息

- 序号：51
- 任务编号：`PPTRANS-20260902-017`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks
摘要：系统评测 Llama-3.1-70B/405B 的批处理和并行配置，刻画 TP、PP 及混合并行对延迟—吞吐权衡的影响。结论显示 TP 更适合延迟目标，PP 更适合吞吐目标；论文虽未提出新的传输压缩机制，但为判断何时值得用 PP、何时网络通信会成为瓶颈提供了高价值实证基线。
- 任务来源：[https://arxiv.org/abs/2603.05692](https://arxiv.org/abs/2603.05692)

## 交付件说明

- [Dense-LLM-并行策略.html](./Dense-LLM-并行策略.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Dense-LLM-并行策略.pptx](./Dense-LLM-并行策略.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [稠密 LLM 并行化原始论文](https://arxiv.org/abs/2603.05692)：用于支撑策略比较、瓶颈分析和实证结果。

# SelfCompact

## 一句话总结

2026年7月10日arXiv v2公布的SelfCompact让同一语言模型依据结构化判据生成摘要并替换累积历史，无需微调，在BrowseComp-Plus的GLM-4.7-Flash实验中将准确率由45.6%提升至54.1%，论文单率每题成本由0.12美元降至0.04美元。

## 任务信息

- 序号：296
- 任务编号：neurips2026-21IUMTFqTe
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：API分类null；主贡献是结构感知的Agent历史压实与状态接续，归记忆与上下文系统。03/输入输出数据是次关联，未提出prefill token剪枝算子；无指定分类差异。
- 任务正文：Self-Compacting Language Model Agents
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：自调用compaction工具与结构敏感触发rubric
压缩对象：已生成的长推理与工具调用轨迹，即后续生成的历史上下文
方法线索（既有摘要）：提供模型自行调用的内联compaction工具与调用时机rubric，在子任务完成或轨迹收敛时压实历史。
2026-11-03独立复核的纳入依据：主审保留：累积的推理/工具调用历史引发context rot，SelfCompact提供内联压实工具与调用时机规则，比较对象为固定间隔历史摘要。核心操作是上下文压实而非要求输出短CoT；具体替换接口仍为摘要级限制。
证据边界：每题cost不等于输入token压缩率；工具实现与摘要质量边界需正文核实。；本轮复核：工具具体输出与原历史替换接口、输入和输出成本拆分仍需正文核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/155897)

## 交付件说明

- [SelfCompact.html](./SelfCompact.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [SelfCompact.pptx](./SelfCompact.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Self-Compacting Language Model Agents](https://arxiv.org/html/2606.23525v2)：历史hard reset、触发rubric、表4性能及附录C/D成本分项。
- [SelfCompact official code](https://github.com/tianjianl/selfcompact)：四消息历史替换、C1/C2/C3/N1门控、固定commit计费与论文差异。
- [Apple Machine Learning Research](https://machinelearning.apple.com/research/self-compacting-language-agents)：作者机构来源与方法定位。

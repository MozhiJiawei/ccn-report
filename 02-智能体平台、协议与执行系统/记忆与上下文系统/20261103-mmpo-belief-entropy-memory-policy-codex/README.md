# MMPO-信念熵记忆策略优化

## 一句话总结

2026年5月28日发布的arXiv:2605.30159v1中，MMPO为长时程LLM智能体递归摘要策略加入信念熵中间奖励，在Qwen2.5-7B的RULER-HotpotQA 56K设置下将准确率从80.47%提升至82.98%，其额外训练探测在该模型上带来约12%的训练时间开销。

## 任务信息

- 序号：297
- 任务编号：neurips2026-26CTl3jZo9
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：API category=null；按2026-11-03人类审阅表，将主归属调整为智能体记忆与上下文系统：研究对象是长时程智能体的递归摘要记忆及其信念保持。Belief Entropy奖励与PPO参数优化作为实现手段保留训练相关性；不改变论文确有参数训练及约12%额外训练开销的事实。
- 任务正文：Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：belief entropy监督的递归摘要策略优化
压缩对象：长交互轨迹的递归摘要记忆
方法线索（既有摘要）：用Belief Entropy为记忆策略提供中间监督，惩罚导致任务状态认知不确定的摘要。
2026-11-03独立复核的纳入依据：主审保留：摘要明确将交互轨迹递归概括为compact memory，方法优化中间摘要的信念保持；属于历史上下文摘要质量优化。无需以具体token压缩率为纳入门槛，但不把1.75M上下文性能写成压缩率。
证据边界：97.1%性能的参照口径摘要不细述；未给压缩token预算及probe代价。；本轮复核：具体递归摘要替换接口和输入token节省尚未验证；不要将大上下文性能直接表述为token压缩率。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/155887)

## 交付件说明

- [MMPO-信念熵记忆策略优化.html](./MMPO-信念熵记忆策略优化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MMPO-信念熵记忆策略优化.pptx](./MMPO-信念熵记忆策略优化.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/html/2605.30159v1)：方法、递归摘要接口、实验表格与附录成本。
- [NeurIPS 2026 Poster](https://neurips.cc/virtual/2026/poster/155887)：会议身份与摘要，97.1%仅作为未解释摘要口径记录。

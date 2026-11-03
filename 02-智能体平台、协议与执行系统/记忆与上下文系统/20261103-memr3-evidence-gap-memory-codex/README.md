# MemR3-证据缺口记忆

## 一句话总结

MemR3是一个以可读证据—缺口状态替代累积检索历史、在检索/反思/回答间闭环决策的对话记忆控制器，arXiv v1（2025-12-23）在LoCoMo的GPT-4.1-mini RAG配置中将LLM裁判分数从79.46%提高到86.75%，2026会议摘要另称长对话查询仅用full-context的1%–5% tokens，后者尚未获得会议正文核验。

## 任务信息

- 序号：307
- 任务编号：neurips2026-o9MB6dPOa4
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：主要改变对象为对话记忆检索与上下文状态：将原始检索历史整合为evidence-gap可读状态，并路由retrieve/reflect/answer。相比03/输入输出数据，其核心贡献是后端无关记忆控制器而非模型prefill或Serving加速；不改变模型本体，排除04。指定分类为null，自动分类，无调用方约束差异。
- 任务正文：Knowing What is Missing: Efficient Conversational Memory via Explicit Evidence-Gap Tracking
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：显式证据缺口状态与检索历史屏蔽
压缩对象：多轮检索累积的文本片段及查询时历史上下文
方法线索（既有摘要）：将新检索片段整合进证据缺口状态，再从后续prompt屏蔽原片段，以紧凑进度摘要承载信息。
2026-11-03独立复核的纳入依据：能从摘要直接确认原输入历史被短状态摘要替代，不是仅缩小离线记忆库。
证据边界：1%–5%指相对full-context查询tokens；摘要未给延迟和摘要维护成本。；本轮复核：状态序列格式、摘要维护代价及各项成本在正文中仍需核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/149691)

## 交付件说明

- [MemR3-证据缺口记忆.html](./MemR3-证据缺口记忆.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MemR3-证据缺口记忆.pptx](./MemR3-证据缺口记忆.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Knowing What is Missing: Efficient Conversational Memory via Explicit Evidence-Gap Tracking](https://neurips.cc/virtual/2026/poster/149691)：2026新题、作者、官方项目身份与LongMemEval_s的1%–5%摘要主张。
- [MemR3: Memory Retrieval via Reflective Reasoning for LLM Agents (arXiv v1, 2025-12-23)](https://arxiv.org/abs/2512.20237)：v1机制、LoCoMo表1/表2结果及迭代预算局限。
- [MemR3 official repository](https://github.com/mbzuai-ai4bio/memr3)：2026-11-03 main快照f2b656bd的JSON状态、原片段缓冲清理/检索mask、token与时延计数边界。

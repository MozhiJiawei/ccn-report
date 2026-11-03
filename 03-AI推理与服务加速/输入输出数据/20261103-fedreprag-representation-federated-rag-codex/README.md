# FedRepRAG-联邦检索表示压缩

## 一句话总结

FedRepRAG（arXiv 2609.22162v1，来源页面标注2026年8月26日）以协同训练的两层投影器将每条检索文档嵌入转为一个冻结生成器可读的表示token，在β=0.1的PubMedQA实验中将检索上下文从1194.05降至3 tokens、计算量从21095.27降至1583.70 GFLOPs/query，准确率59.40%高于直接推理54.00%但低于原文检索82.20%，实现跨客户端知识输入压缩且不提供端到端形式化隐私保证。

## 任务信息

- 序号：306
- 任务编号：neurips2026-lKq7IpwC03
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：category为null，按正式正文自动归类。主改变对象为生成器的检索输入表示，将原文输入替换为紧凑表示token，匹配03输入输出数据；02记忆与上下文系统的Agent生命周期不是主体，07隐私为次要关联且仍存在表示泄露。没有与指定分类的差异。
- 任务正文：Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：检索embedding的latent通信及投影
压缩对象：分布式RAG中原本交换的原始检索文本上下文
方法线索（既有摘要）：仅交换压缩latent representations，以轻量投影器映射检索embedding到冻结LLM/VLM特征空间后整合知识。
2026-11-03独立复核的纳入依据：这不是普通通信编码或只压储存；压缩后的语义表示实际承担生成模型知识输入，可保留其文本QA分支。
证据边界：压缩率、隐私形式保证与投影训练成本未说明。；本轮复核：文本QA和VQA须分开记录；latent数量、输入token口径和投影训练成本需正文核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/150023)

## 交付件说明

- [FedRepRAG-联邦检索表示压缩.html](./FedRepRAG-联邦检索表示压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [FedRepRAG-联邦检索表示压缩.pptx](./FedRepRAG-联邦检索表示压缩.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Beyond Raw Context Transfer: Representation-based Federated Retrieval-Augmented Generation（arXiv v1）](https://arxiv.org/abs/2609.22162v1)：方法接口、QA/VQA实验、训练开销和表示泄露边界；唯一v1及来源日期原样记录。
- [NeurIPS 2026 Poster: Beyond Raw Context Transfer](https://neurips.cc/virtual/2026/poster/150023)：会议身份、作者和任务摘要；与arXiv隐私措辞差异已记录。

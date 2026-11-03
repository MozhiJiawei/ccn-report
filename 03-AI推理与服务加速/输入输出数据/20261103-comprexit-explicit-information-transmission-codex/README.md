# ComprExIT-显式信息传输

## 一句话总结

ComprExIT在2026年6月18日更新的arXiv v4中，通过跨层特征门控和锚点到槽位的全局传输实现4×软上下文压缩，在六个域内QA数据集上将1B模型平均F1由56.16提升至66.55（相对ICAE+18.5%），512-token压缩耗时由0.43降至0.18秒，端到端由10.59降至10.01秒。

## 任务信息

- 序号：304
- 任务编号：neurips2026-UmwQ35aBP0
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：冻结LLM的全文特征聚合成更少连续槽位，主要贡献为推理输入表示压缩；与04模型本体架构比较后选择03输入输出数据。指定分类null，无约束差异。
- 任务正文：Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：多层特征选择+anchor-to-slot显式信息传输
压缩对象：长文本上下文在冻结LLM多层中的特征表示
方法线索（既有摘要）：自适应选择跨层特征，以全局协调的anchor-to-slot传输计划将信息聚合到compression slots。
2026-11-03独立复核的纳入依据：保持用户已认可的ComprExIT Golden Standard，明确属于软表示压缩。
证据边界：加速数字指压缩过程而非端到端推理；未报具体slot数量和压缩率。；本轮复核：当前用户相关性已认可；具体压缩比和实验代价仍须区分摘要与正文验证状态。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/152205)

## 交付件说明

- [ComprExIT-显式信息传输.html](./ComprExIT-显式信息传输.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [ComprExIT-显式信息传输.pptx](./ComprExIT-显式信息传输.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Fix the Structural Bottleneck: Context Compression via Explicit Information Transmission (arXiv v4, 2026-06-18)](https://arxiv.org/abs/2602.03784v4)：方法、压缩比、质量、分阶段时延、训练配置与证据边界（全文Figures1–2、Tables1/3/9）。
- [NeurIPS 2026 Poster](https://neurips.cc/virtual/2026/poster/152205)：题名作者及会议Poster身份，与v4摘要相互核对。

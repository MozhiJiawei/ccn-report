# MEGA-增益感知证据选择

## 一句话总结

截至2026年11月3日作者项目页，MEGA面向医学证据问答，通过冻结模型的隐藏态效用评分和显式token预算下的FPTAS选择紧凑证据子集，作者报告在3种生成骨干、5种医学RAG基线上相对次优方案平均提升8.8%答案质量与38.8%证据F1以改善答题和证据支持，原论文PDF与端到端复现尚未核验。

## 任务信息

- 序号：303
- 任务编号：neurips2026-PsPjtMRFBs
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：MEGA直接在显式token预算下选择送入生成模型的检索证据snippet子集，医学QA为验证场景；主要改变对象是推理输入裁剪。
- 任务正文：Less Evidence, Better Answering: Gain-Aware Minimal Evidence Subset Selection for Medical QA
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：信息增益驱动预算证据子集选择
压缩对象：检索后候选证据片段组成的QA上下文
方法线索（既有摘要）：冻结LLM的hidden-state信息增益评分估计新增答题信息，再在显式token预算下求取紧凑证据子集。
2026-11-03独立复核的纳入依据：按新增答案信息而非单条相关性裁去上下文片段，与COMI的信息价值/去冗余方向相近，删除粒度是snippet。
证据边界：未报告具体token压缩率和不同budget的性能曲线。；本轮复核：证据子集送入生成模型的确切格式及输入token减少幅度需正文核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/152857)

## 交付件说明

- [MEGA-增益感知证据选择.html](./MEGA-增益感知证据选择.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MEGA-增益感知证据选择.pptx](./MEGA-增益感知证据选择.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Less Evidence, Better Answering — MEGA官方项目](https://mega-evidenceqa.github.io/)：方法流程、4种IGS代理、FPTAS目标边界、原始图、全部18行结果CSV与指标条件。
- [NeurIPS 2026官方Poster](https://neurips.cc/virtual/2026/poster/152857)：论文题名、作者、会议身份、摘要及项目链接。
- [MEGA官方Release status](https://github.com/mega-evidenceqa/MEGA/blob/main/docs/RELEASE_STATUS.md)：公开代码与最终论文版本的差异，FPTAS及CRC发布和复现边界。

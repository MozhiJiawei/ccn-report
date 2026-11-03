# LTV-线性任务向量

## 一句话总结

2026年5月20日公开的LTV（arXiv:2605.20730v1）以闭式岭回归拟合可复用映射，在推理时用随查询生成的隐藏态任务向量替代ICL演示输入，使Llama-3.1-8B八分类平均准确率达到75.46%，单样本在线耗时由完整ICL的0.2238秒降至0.0226秒，但需42.664秒预抽取且准确率低于完整ICL的82.66%。

## 任务信息

- 序号：302
- 任务编号：neurips2026-PRjQ0E5e0e
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：category=null自动判断；LTV在线用隐藏表示替代重复ICL演示输入，03细则输入输出数据承接输入表示处理。未改变模型本体架构，排除04；不更新LLM权重，外部岭回归是压缩实现，排除05；虽提出d_NTP质量指标，主贡献还包括可用的输入压缩机制，故不归06。无指定分类差异。
- 任务正文：Distributional Alignment as a Criterion for Designing Task Vectors in In-Context Learning
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：闭式线性ICL任务向量
压缩对象：ICL中随上下文增长的文本示例序列
方法线索（既有摘要）：将demonstrations压为紧凑hidden-state task vector；用闭式回归映射估计示例效应，最小化与ICL的预测分布差异。
2026-11-03独立复核的纳入依据：文本示例被紧凑隐藏表示替代，属于与ComprExIT相近的软表示压缩；不将其说成删除可读prompt token。
证据边界：摘要未报压缩率/具体延迟数字；向量是任务级演示影响而非逐文档重建。；本轮复核：向量注入位置、单次抽取成本及跨query摊销方式需正文核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/152916)

## 交付件说明

- [LTV-线性任务向量.html](./LTV-线性任务向量.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LTV-线性任务向量.pptx](./LTV-线性任务向量.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Distributional Alignment as a Criterion for Designing Task Vectors in In-Context Learning](https://arxiv.org/abs/2605.20730v1)：方法公式、最后层注入、八分类实验、抽取及推理时延和边界。
- [LTV官方实现](https://github.com/Jii111/LTV)：官方性、闭式岭回归实现、基准和实验入口；HEAD e826e13d23c99986137d139f6259e2d73fda95fe。
- [NeurIPS 2026 Poster](https://neurips.cc/virtual/2026/poster/152916)：会议身份与任务来源。

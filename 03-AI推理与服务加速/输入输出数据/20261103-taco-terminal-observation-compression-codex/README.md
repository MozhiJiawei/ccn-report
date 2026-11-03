# TACO-终端观测压缩

## 一句话总结

TACO（arXiv:2604.19572v3，2026年5月15日）通过自演化结构化规则压缩终端Agent后续输入中的冗余观察文本，在MiniMax-M2.5六基准实验中使端到端总token减少2.7%–27.0%且成功率持平或提升，适合高日志量终端工作流。

## 任务信息

- 序号：301
- 任务编号：neurips2026-MMhankfnpV
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：category原值null，自动归类。读取总则及02/03细则后，主要改变对象是进入模型下一轮prompt的终端观察文本，直接命中03的输入裁剪；02记忆与上下文系统虽相关，但规则池复用是辅助机制。无调用方指定分类，因而不存在与指定值差异。
- 任务正文：A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：自演化终端观测规则压缩
压缩对象：送入CLI agent上下文的终端执行观察文本
方法线索（既有摘要）：从交互轨迹发现、演化并复用压缩规则，过滤冗余终端观察，同时保留精确任务证据。
2026-11-03独立复核的纳入依据：具体被删除的是进入后续上下文的冗余工具观察文本，有可辨认的输入压缩链条。
证据边界：终端观测具有异质结构和精确证据要求；摘要未列具体模型和压缩时间。；本轮复核：规则执行前后的输入token计数、压缩器代价和保真边界需正文核实；摘要总token收益不能全当输入收益。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/153290)

## 交付件说明

- [TACO-终端观测压缩.html](./TACO-终端观测压缩.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [TACO-终端观测压缩.pptx](./TACO-终端观测压缩.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression (arXiv v3)](https://arxiv.org/abs/2604.19572v3)：规则机制、实验表1–6、附录J辅助token开销及附录M保真边界。
- [NeurIPS 2026 Poster: A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://neurips.cc/virtual/2026/poster/153290)：会议Poster身份和摘要交叉核对；作者列表与v3有差异。

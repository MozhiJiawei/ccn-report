# Bayes充分压缩-接收者通信选择

## 一句话总结

arXiv 2610.03769v1（2026年9月29日）中的Bayes-Sufficient Compression研究用接收者可利用增益减去协议税来选择多智能体间不发送、短消息或原上下文通信，在默认Qwen接收协议下使ContextBench下一步对象与动作联合准确率从63.3%升至77.5%，同时揭示ToolSandbox从88.9%降至65.3%的失效条件。

## 任务信息

- 序号：298
- 任务编号：neurips2026-4MClMQl04u
- 热点编号：NeurIPS2026-文本语义压缩
- 周期：202611
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：category为null，自动归类；主问题是上下文不对称主Agent与执行子Agent的协作通信动作决策，改变Agent协作编排。协议税不是互操作协议标准，故优于协议与互操作；没有模型本体改动，故不归AI模型。
- 任务正文：Bayes-Sufficient Compression Is Not Enough: How Communication Helps in Multi-Agent Systems?
会议：NeurIPS 2026（主会录用，Poster）。
调研方向：文本语义压缩与token剪枝；不限于PP推理。
方法类型：上下文压缩通信的分析研究与动作选择；非新token剪枝算法
压缩对象：主agent向执行子agent传递的原始上下文
方法线索（既有摘要）：以短压缩消息替代原上下文传递，比较压缩消息、原始上下文和不发送消息，并按下游增益与协议成本选择。
2026-11-03独立复核的纳入依据：主审保留为上下文压缩分析研究：明确比较短压缩消息替代raw context的收益与失败条件，压缩语义在受限接收者中的可用性是直接研究对象。不是新token剪枝算法，未验证独立的token压缩率或加速率。
证据边界：压缩可能因decoder mismatch或协议负担损害任务；未给统一压缩率。；本轮复核：短消息生成过程、实际输入长度及与COMI类压缩方法的差别需后续正文核实。
后续调研重点：说明输入/上下文如何被删除、合并或用紧凑语义表示替代，核实质量与效率指标及训练开销；区分记忆库规模、输入token数量、总token消耗和推理加速。
当前纳入为摘要级筛选判断，不代表正文实验已核验；压缩分析研究须与新剪枝算法区分。
- 任务来源：[原始任务来源](https://neurips.cc/virtual/2026/poster/155601)

## 交付件说明

- [Bayes充分压缩-接收者通信选择.html](./Bayes充分压缩-接收者通信选择.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Bayes充分压缩-接收者通信选择.pptx](./Bayes充分压缩-接收者通信选择.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [NeurIPS 2026 官方论文页](https://neurips.cc/virtual/2026/poster/155601)：确认论文、作者、会议及官方摘要中的双向通信效应。
- [Bayes-Sufficient Compression Is Not Enough: How Does Communication Help Multi-Agent Systems? (arXiv v1)](https://arxiv.org/abs/2610.03769)：支撑接收者相对协调理论、128-token消息协议、六基准实验、分阶段错误诊断及选择器成本口径。

# AgentMemRec

## 一句话总结

2026年10月26日v1论文提出的AgentMemRec是将智能体长期记忆选择建模为预算化列表推荐的召回—排序—填充系统，在LongMemEval-S跨至少两会话的209道测试题和2400至2700 token预算下以零选择阶段LLM调用达到80.7%的Qwen3-32B答题准确率。

## 任务信息

- 序号：328
- 任务编号：TASK-20261104090535-bde00eee
- 热点编号：HS-20261104-article1793754336018464
- 周期：2026-W45
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：指定分类为null，按正文自动分类。AgentMemRec主要改变长期记忆的候选召回、相关性排序和token预算下的上下文构建，直接命中记忆与上下文系统；评测是验证而非主要交付对象，不归评测与可观测。无指定值冲突。
- 任务正文：AgentMemRec 把智能体长期记忆形式化为预算化列表推荐，无需 LLM 调用即超越多种记忆方法快报
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.34673)

## 交付件说明

- [AgentMemRec.html](./AgentMemRec.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [AgentMemRec.pptx](./AgentMemRec.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Agent Memory as Recommendation: Recommender-System Design for Long-Term Memory of LLM Agents](https://arxiv.org/abs/2610.34673)：v1论文的方法、LongMemEval及LoCoMo实验、证据完整率、选择GPU成本和适用边界。

# Fork-Think with Confidence

本报告解读 Fork-Think 的适用场景、机制、实验收益与工程边界。

核心场景是复杂问题的测试时多路径推理：传统 Parallel Thinking 从头生成多条完整推理路径，再通过多数投票等方式聚合答案；Fork-Think 复用一条共享 seed path，在低置信度位置分叉生成多条 continuation，从而减少重复前缀的 token 与运行时间成本。

## 来源

- Fork-Think with Confidence
- arXiv: https://arxiv.org/abs/2606.31484

## 阅读边界

- 论文报告的 token 降幅为 7%–30%，运行时间降幅为 38%–57%；这是特定实验条件下的结果。
- 该机制不是多 Agent 任务分工、训练方法或单纯提示词技巧。
- 适用通常需要多路径推理、答案聚合、token 级置信度信号以及前缀/KV 复用能力。

归档日期：2026-07-15  
生成者：Codex

# Akashic：面向长期记忆型 Agent 的推理服务系统

## 报告定位

本报告面向不了解 Agent Memory 的技术读者，解释 Akashic 如何同时优化长期记忆的语义组织与物理存储局部性。

Akashic 不是传统的模型算子、量化或 KV Cache 优化，也不只是记忆准确率算法。它处理的是长期运行 Agent 的记忆服务问题：在推理请求到来时，从持续增长的外部记忆中选择相关 chunk，并以较低的维护与读取开销将其注入模型上下文。

## 核心机制

- MemAttention 将历史组织为有界 chunk，并在压缩维护和请求召回时使用模型驱动的语义匹配。
- 默认召回当前 `user_id`、`session_id` 命名空间内最相关的 5 个 chunk，读取完整记录后按时间顺序拼入推理上下文。
- Memory Manager 将可能共同召回的 chunk 物理共置，降低随机读取、读放大与冷缓存延迟。

## 唯一来源

- Yang Liu et al., *Akashic: A Low-Overhead LLM Inference Service with MemAttention*, arXiv:2607.05708v1, 2026-07-07.
- https://arxiv.org/abs/2607.05708

## 归档内容

- `report/index.html`：使用 SingleFile 导出的 dependency-free HTML，可离线打开。

## 证据边界

- 报告仅使用 Akashic 原始论文，不引用二手解读作为核心证据。
- 性能提升为论文在指定模型、硬件、负载与基线下报告的结果，尚未独立复现。
- 论文明确描述基于 metadata 的模型驱动 Top-5 选择，但没有充分说明超大候选池下是否存在 ANN 粗召回或候选规模上限。

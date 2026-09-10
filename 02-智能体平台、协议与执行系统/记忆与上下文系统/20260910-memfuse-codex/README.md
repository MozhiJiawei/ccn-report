# MemFuse

## 一句话总结

MemFuse 是小米与南京大学在 2026 年 8 月 19 日 arXiv v1 论文中提出的智能体多来源记忆系统，通过保留原子事件来源、组织融合记忆与关系图检索来拼接分散证据，并在含 6 个合成场景、7,823 个事件和 357 道问题的 MemFuseBench 上取得三种模型设置下参评 top-k 记忆与检索系统最高的 Overall 分数，为跨应用、设备和用户的碎片语义事件问答提供可追溯证据。

## 任务信息

- 序号：87
- 任务编号：TASK-20260910151559-0996357e
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：系统主要改变智能体对碎片语义事件的存储、融合与可追溯检索；MemFuseBench 是配套基准贡献，可作为次要关联标签，不改变主要系统对象的归属。
- 任务正文：MemFuse
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.18704)

## 交付件说明

- [MemFuse.html](./MemFuse.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MemFuse.pptx](./MemFuse.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

合成语义事件不等于真实设备多模态验证；top-20条目非等token或时延预算，正文与附录条目组成表述有差异。GPT设置仅比最强其他top-k系统高0.0024，GPT/Gemini全上下文得分更高；推理token高于Naive RAG。Docling附录页警告保留，最终8张图表校验通过。

## 引用信息源说明

- [MemFuse原始技术来源](https://arxiv.org/abs/2608.18704v1)：支持技术机制、实验设置、量化结果和证据边界。

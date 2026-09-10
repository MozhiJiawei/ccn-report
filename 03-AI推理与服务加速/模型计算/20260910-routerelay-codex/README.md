# RouteRelay

## 一句话总结

2026年9月7日发布的RouteRelay v1是一种面向长上下文动态稀疏注意力的跨层路由元数据复用方法，通过近失与随机哨兵触发逐行重路由，在论文合成路由规模实验中保持100% top-k路由召回、仅计算完整路由38.4%–51.6%的评分对，但未融合CPU实现仍比完整路由慢约1.6–3.7倍。

## 任务信息

- 序号：110
- 任务编号：TASK-20260910205008-2a2c9dec
- 热点编号：HS-20260910-article1789044608981249
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：任务category为null，自动分类；比较03与04细则后归03-AI推理与服务加速/模型计算。直接优化对象是动态稀疏注意力的路由评分计算，未改变模型主干权重、层执行或当前层Q/K/V，亦非KV缓存共享或驱逐机制；无调用方分类差异。
- 任务正文：RouteRelay通过跨层路由元数据复用实现高效动态稀疏注意力技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.07306)

## 交付件说明

- [RouteRelay.html](./RouteRelay.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [RouteRelay.pptx](./RouteRelay.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

合成跨层漂移与路由级实验，未报告真实大模型任务准确率；路由召回不等于模型任务准确率；评分对减少不等于端到端推理加速；GPU融合执行为系统设计，未提供GPU端到端实测加速；未融合CPU实现所有测试规模均慢于完整路由。

## 引用信息源说明

- [RouteRelay: Event-Triggered Cross-Layer Route Reuse for Efficient Dynamic Sparse Attention](https://arxiv.org/abs/2609.07306)：原始论文v1，支撑方法、合成路由实验、CPU延迟和证据边界

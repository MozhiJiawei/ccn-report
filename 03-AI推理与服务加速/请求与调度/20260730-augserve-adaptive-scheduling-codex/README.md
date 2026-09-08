# AugServe：增强型 LLM 的自适应请求调度

本目录归档 AugServe 原始论文的 Source Understanding 正式报告。报告面向不了解该技术的技术读者，解释外部工具调用为什么会造成队头阻塞，以及 AugServe 如何通过状态感知排序和动态批容量改善有效吞吐量与首 Token 延迟。

## 一句话描述

AugServe 是一种面向工具增强型 LLM 在线推理的状态感知自适应调度框架，通过两阶段请求排序与动态 Token 批预算，在论文测试负载下将有效吞吐量提升最高 4.7 倍，并将首 Token 延迟（TTFT）降低最高 96.3%。

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile HTML，可离线打开，不依赖外部图片、CSS、JavaScript 或字体文件。

## 唯一主证据

- 论文：**AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving**
- arXiv：https://arxiv.org/abs/2512.04013
- 版本边界：arXiv 预印本，报告结论以论文披露的模型、硬件、负载、基线和 SLO 为限。

## 核心证据边界

- 本报告仅使用 AugServe 原始论文，不包含独立同类方案报告。
- `4.7×` 和 `96.3%` 均受具体基线、测试负载和统计口径约束，不应泛化为所有部署环境下的固定收益。
- effective throughput 指满足延迟 SLO 的请求处理能力，不等同于无约束的原始 tokens/s。

## 人工与质量状态

- Source Understanding：用户已批准归档。
- 论文图表解析：25/25 已索引。
- SingleFile 导出：成功。
- 独立视觉 QA：PASS，各项 4/4；未发现破图、裁切、遮挡或横向溢出。

归档日期：2026-07-30  
Creator：Codex

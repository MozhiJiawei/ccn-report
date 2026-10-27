# Saluki-27B-IQ2量化

## 一句话总结

Saluki 27B是Conway Research于2026年10月发布的Qwen3.8-27B混合低位量化模型，以标准IQ2-mix GGUF将约54 GB权重压缩到7.89 GB，在发布方冻结的120道工具调用子集上通过88题、原版84题，同时只保留原版正确84题中的76题，为本地工具助手提供需验证能力取舍的紧凑权重。

## 任务信息

- 序号：287
- 任务编号：TASK-20261026152151-8b077410
- 热点编号：HS-20261026-article1792999311898153
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：API指定null，自动分类。已比较03与04细则，核心是量化模型压缩和推理资源取舍，03/模型计算直接承接。模型发布及Agent工具调用是载体和评测能力，无新模型架构或Agent执行系统主贡献；无指定分类差异。
- 任务正文：Conway Research 发布 2-bit 量化 Saluki 27B，7.89 GB 工具调用反超原版技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/h7pvcekl9p3n51oifvbjufk16)

## 交付件说明

- [Saluki-27B-IQ2量化.html](./Saluki-27B-IQ2量化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Saluki-27B-IQ2量化.pptx](./Saluki-27B-IQ2量化.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Meet Underdog Saluki 27B（官方发布文章）](https://underdog.ai/saluki)：发布定位、120题评测集合交集、并行严格与宽松评分、preview和未公开流程边界。
- [ConwayResearch/Underdog-Saluki-27B-1.0（冻结模型卡）](https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0/blob/5acfd9218fa54731f237eea8b3243d430dd85a69/README.md)：IQ2-mix GGUF大小、标准llama.cpp、thinking配置、可选视觉附件、其他能力指标和限制。

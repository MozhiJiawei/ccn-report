# Saluki-27B-工具调用量化

## 一句话总结

截至2026年10月23日官方模型卡，ConwayResearch 的 Saluki 27B 1.0 是面向 llama.cpp 本地工具调用的 Qwen3.8-27B 低位量化 GGUF，将权重文件从约54 GB压缩为7.89 GB，并在发布者120题工具调用子集上通过88题、全尺寸基线通过84题，为端侧部署提供可验证但仍需实测能力与内存取舍的压缩制品。

## 任务信息

- 序号：243
- 任务编号：TASK-20261021213608-6602c0c8
- 热点编号：HS-20261021-article1792589769555643
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：指定分类null，按正式正文自动归类：主要技术贡献是低位权重压缩及推理能力取舍，属于模型计算；04-AI模型发布为次要关联，未采用。无指定分类差异。
- 任务正文：Conway Research 发布 2-bit 量化 Saluki 27B，7.89 GB 工具调用反超原版技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/h7pvcekl9p3n51oifvbjufk16)

## 交付件说明

- [Saluki-27B-工具调用量化.html](./Saluki-27B-工具调用量化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Saluki-27B-工具调用量化.pptx](./Saluki-27B-工具调用量化.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [ConwayResearch/Underdog-Saluki-27B-1.0](https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0)：Saluki 1.0权重文件、部署兼容、工具调用与并行工具调用设置和结果、数学退化及限制；发布者自报，未独立复现。
- [ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)：官方明确致谢的上游GSQ/RCO逐张量混合精度与预算搜索机制，不证明Saluki完整采用其流水线。

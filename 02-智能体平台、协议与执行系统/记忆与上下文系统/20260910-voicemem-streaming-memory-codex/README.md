# VoiceMem

## 一句话总结

VoiceMem（2026年8月26日论文v1）是面向实时语音智能体的流式记忆系统，通过事实索引与情感人格图联合检索，在作者LoCoMo实验的Top-5设置下取得91.2分、430个记忆token及134毫秒检索耗时，为有限上下文预算下的个性化交互提供记忆支持。

## 任务信息

- 序号：119
- 任务编号：TASK-20260910205339-461683ab
- 热点编号：HS-20260910-article1789044819529473
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：指定分类null，依据正式全文自动分类；论文§4.2明确主贡献为外部记忆的上层路由、双脑图组织与流式检索，底层MemSearch引擎可替换且默认Mem0，故归02记忆与上下文系统；已对照04模型细则，语音模型OPD适配是配套基础设施，并非双脑模型本体架构，无指定分类差异。
- 任务正文：颜水成团队发布VoiceMem，流式双脑架构实现实时交互记忆技术线索
- 任务来源：[原始任务来源](https://www.jiqizhixin.com/articles/2026-09-07-6?source=rss)

## 交付件说明

- [VoiceMem.html](./VoiceMem.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [VoiceMem.pptx](./VoiceMem.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

结果为作者报告，未独立复现；134ms仅为检索耗时，近零新增延迟依赖VAD期间并行计算，不是端到端语音响应SLA；人格平均增益1.89个百分点对应同GPT-4o-mini回答器，4.29个百分点对应微调回答器，不可混同；ChatMem-Bench为作者构建评测。

## 引用信息源说明

- [VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction v1](https://arxiv.org/abs/2608.26005v1)：原始论文，支撑双脑记忆结构、流式检索机制、实验设置与指标边界
- [VoiceMem official project](https://xzf-thu.github.io/VoiceMem/)：官方项目图示、训练流程与产品定位，2026-09-10抓取
- [VoiceMem repository at a450911](https://github.com/xzf-thu/VoiceMem/tree/a450911fc8cbb44c46d810aace2f3288bad287e4)：官方实现、可替换后端与开源范围，2026-09-10固定HEAD

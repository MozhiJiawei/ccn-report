# Hy-SimulMT

## 一句话总结

2026 年 10 月 26 日发布的 Hy-SimulMT 是腾讯混元面向会议、访谈等实时交流场景的中英双向语音翻译模型，可结合逐块语音和会话历史增量生成译文并外接 TTS 播报，在腾讯 RealSI 长音频评测中达到约 3 秒 StreamLAAL 流式翻译滞后。

## 任务信息

- 序号：324
- 任务编号：TASK-20261104090402-3f265246
- 热点编号：HS-20261104-article1793754242697288
- 周期：2026-W45
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：任务分类为 null。正文聚焦中英双向流式语音翻译模型及分块增量译文生成，符合话音模型子类的 S2TT 范围。RealSI 结果用于验证模型能力，分块和独立 TTS 用于解释公开部署链路。复核后保持原归类。
- 任务正文：腾讯混元开源同声传译模型Hy-SimulMT，实测响应约3秒快报
- 任务来源：[原始任务来源](https://aihot.news/items/badcpaha9fu3mtvz4s7odxrqd)

## 交付件说明

- [Hy-SimulMT.html](./Hy-SimulMT.html)：可离线打开的 SingleFile 来源理解报告。
- [Hy-SimulMT.pptx](./Hy-SimulMT.pptx)：一页式可编辑技术洞察汇报。

## 引用信息源说明

- [腾讯混元 Hy-SimulMT 官方中文 README（7efcb18）](https://github.com/Tencent-Hunyuan/Hy-SimulMT/blob/7efcb18c521a7025b37d4bc2230a1df8ade83950/README.zh-CN.md)：发布日、RealSI 原始散点图、StreamLAAL 与 GEMBA、人工小样本和公开权重列表。
- [腾讯混元 SimulInfer 中文技术文档（7efcb18）](https://github.com/Tencent-Hunyuan/Hy-SimulMT/blob/7efcb18c521a7025b37d4bc2230a1df8ade83950/SimulInfer/README.zh-CN.md)：标准和短分块规格、独立 TTS 及源音色条件。
- [腾讯混元 SimulInfer 会话实现（7efcb18）](https://github.com/Tencent-Hunyuan/Hy-SimulMT/blob/7efcb18c521a7025b37d4bc2230a1df8ade83950/SimulInfer/simulinfer/translation.py#L492-L534)：在会话历史中加入新音频块、仅在有新译文时提交，及等待后的补译分支。
- [腾讯混元 Hy-SimulMT-30B-A3B 官方模型卡（56c233d）](https://huggingface.co/tencent/Hy-SimulMT-30B-A3B/tree/56c233df75bf09e386aa6282b01730b461afc83f)：仅译文检查点，以及同提交配置声明的音频编码器和 MoE 主模型。

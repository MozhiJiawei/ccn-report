# MuseVoiceTranscribe

## 一句话总结

Meta于2026年9月1日发布的Muse Voice Transcribe是面向实时语音应用的流式感知模型，通过自适应听写延迟与专用标记统一完成转写、说话人归属和话语终点检测，训练覆盖70余种语言且其中25种已充分验证，并声明支持超过1小时音频和20余位说话人，以减少长对话处理的后处理环节。

## 任务信息

- 序号：109
- 任务编号：TASK-20260910204923-030e83a0
- 热点编号：HS-20260910-article1789044564117075
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：category为null，自动归类；主要贡献为流式ASR模型及其自适应延迟和联合任务机制，属于话音模型本体，应用工作流是次要用途；已比较04与01板块，无指定分类差异。
- 任务正文：Meta发布实时音频模型Muse Voice Transcribe，支持70+语言和20人说话人分离技术线索
- 任务来源：[原始任务来源](https://aihot.virxact.com/items/cmtpn9uou01fcrow73d4tf75y)

## 交付件说明

- [MuseVoiceTranscribe.html](./MuseVoiceTranscribe.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MuseVoiceTranscribe.pptx](./MuseVoiceTranscribe.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

70+训练语言不等于全部充分验证；80ms音频分块不等于端到端延迟；图中约0.16秒仅为End of Speech到最终转录；20+说话人不代表同时重叠发声保证或身份识别；WER 3.1%及跨AMI-IHM、AMI-SDM、VoxConverse平均DER 17.5%为2026-09-01官方图示，未经本次独立复测。

## 引用信息源说明

- [Introducing Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe)：Meta官方原始发布，支撑模型机制、语言验证范围、说话人能力与发布时间

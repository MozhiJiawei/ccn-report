# Nemotron-3-Diarization

## 一句话总结

NVIDIA 于2026年9月23日发布的开放权重 Nemotron 3 Diarization 是约1亿参数、支持最多8位说话人的音频说话人分离模型，可在流式或离线语音中输出匿名说话人活动与时间戳，并在 VoiceArena 初始英语评测中取得14.72% DER，为会议转写和语音智能体提供说话人归属。

## 任务信息

- 序号：169
- 任务编号：DSH-20260924-012
- 热点编号：HS-20260924-dsh-tech-insight
- 周期：2026-W39
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：主要贡献是语音说话人分离模型本体；Agent 场景只是应用，归入话音模型与模型架构。
- 任务正文：📌NVIDIA 开源 Nemotron 3 Diarization，语音智能体实时说话人追踪
原文标题：RT Andi Marafioti: Voice agents still don’t understand who’s speaking to them. That’s a huge gap compared with humans, hidden by all the “phone-ca...
元信息：战略 · 2026/09/23 · 编号 #12 · NVIDIA is open-sourcing Nemotron 3 Diarization: a
要点：
- NVIDIA is open-sourcing Nemotron 3 Diarization: a model that can reliably track speakers in live conversations, under a commercial-friendly license
- Kudos to the NVIDIA team for shipping useful tools for the whole community
技术效果：效果 · 推理强化：开源策略：据 @andimarafioti 转推：NVIDIA 开源 Nemotron 3 Diarization 模型，商业友好许可证，可实时追踪对话中说话人；模型已 Transformers 零日集成；作者用 Reachy Mini + speech-to-speech 在 DGX Spark 上以一秒语音块测试，称"质量很好"
背景补充：该模型补足语音智能体"谁在说话"识别短板，对应 Hugging Face 推出的级联 VAD→STT→LLM→TTS 语音智能体管线，Reachy Mini 现已可在本地运行（8GB 显存预算）。
源链接：https://x.com/huggingface/status/2102785799087628502
- 任务来源：[原任务来源](https://x.com/huggingface/status/2102785799087628502)

## 交付件说明

- [Nemotron-3-Diarization.html](./Nemotron-3-Diarization.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Nemotron-3-Diarization.pptx](./Nemotron-3-Diarization.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [NVIDIA：Know Who Spoke When](https://huggingface.co/blog/nvidia/nemotron-diarization)：用于核对模型结构、最多8位说话人、缓冲档位和VoiceArena初始DER口径。
- [NVIDIA Nemotron 3 Diarization 模型卡](https://huggingface.co/nvidia/Nemotron-3-Diarization)：用于核对权重许可、模型输入输出及部署限制。
- [Hugging Face Transformers：Nemotron 3 Diarization](https://huggingface.co/docs/transformers/main/model_doc/nemotron3_diarization)：用于核对接口和推理使用方式。

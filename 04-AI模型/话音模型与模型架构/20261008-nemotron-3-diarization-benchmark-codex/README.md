# Nemotron 3 Diarization：低延迟评测与部署边界

## 一句话总结

NVIDIA 的 Nemotron 3 Diarization 流式说话人分离模型可输出多达8位说话人的活动时间线；Baseten 在 AISHELL-4 上报告其1.04秒输入缓冲档 DER 为9.8%、单 RTX PRO 6000 优化部署达到500余路并发，但所引前代27.2%属离线档，且该数据集列于模型训练集，不能据此宣称同条件提升或独立泛化。

## 任务信息

- 序号：176
- 任务编号：DSH-20260924-057
- 热点编号：HS-20260924-dsh-tech-insight
- 周期：2026-W39
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：核心对象是 Nemotron 3 Diarization 的流式说话人跟踪模型、架构、精度与部署边界；本篇侧重 Baseten 的条件化评测，与 169 号的模型概览区分。
- 任务正文：📌NVIDIA 开源 Nemotron 3 Diarization 说话人分离，AISHELL-4 DER 9.8%
原文标题：Our new Nemotron 3 Diarization model + @pollenrobotics Reachi Mini + DGX Spark Great work Andi @huggingface 🙌
元信息：战略 · 2026/09/23 · 编号 #57 · Our new Nemotron 3 Diarization model + @pollenrobo
要点：
- NVIDIA 开源 Nemotron 3 Diarization 模型，可在实时对话中可靠追踪说话人Our new Nemotron 3 Diarization model + @pollenrobotics Reachi Mini + DGX Spark Great work Andi @huggingface Andi Marafioti: Voice agents still dont understand whos speaking to them
- 据 Andi Marafioti：语音智能体仍无法识别对话者身份NVIDIA is open-sourcing Nemotron 3 Diarization: a model that can reliably track speakers in live conversations, under
技术效果：效果 · 推理强化：架构创新：据 Baseten：~100M 参数 Transformer，16 kHz 音频转 10ms 帧输出 T×8 说话人活动概率；据 Baseten：单 checkpoint 覆盖 0.32–30.4 秒四种算法延迟；据 Baseten：AISHELL-4 低剖面 DER 9.8%（前代 Streaming Sortformer v2.1 为 27.2%），单 RTX PRO 6000 可承载 500+ 路 1 小时流（叠加 Parakeet 0.6B 转写为 190 路）
背景补充：2026/09/23 Baseten 报道，Nemotron 3 Diarization 为 Streaming Sortformer v2.1 后继，采用 OpenMDW 1.1 许可证可商用；Hugging Face preview 仍处 Early Access 内部评估、仅限 NVIDIA GPU；采用"按到达顺序"说话人缓存与 FIFO 帧队列，无需嵌入或聚类即可处理无界长度音频。
源链接：https://x.com/NVIDIAAI/status/2102780834193567805
- 任务来源：[NVIDIA AI 原始发布帖](https://x.com/NVIDIAAI/status/2102780834193567805)

## 交付件说明

- [Nemotron-3-Diarization-Benchmark.html](./Nemotron-3-Diarization-Benchmark.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Nemotron-3-Diarization-Benchmark.pptx](./Nemotron-3-Diarization-Benchmark.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [NVIDIA 模型卡](https://huggingface.co/nvidia/Nemotron-3-Diarization)：用于核对输入缓冲档、模型规格及 AISHELL-4 训练集标记。
- [NVIDIA 官方技术介绍](https://huggingface.co/blog/nvidia/nemotron-diarization)：用于核对模型架构、流式机制、指标定义与时延边界。
- [Baseten 实测文章](https://www.baseten.co/blog/nvidia-nemotron-3-diarization/)：用于核对 AISHELL-4 各档 DER、RTX PRO 6000 并发和 p95 emit-lag 的实验条件；网页未公开对应测试切分及复现脚本。

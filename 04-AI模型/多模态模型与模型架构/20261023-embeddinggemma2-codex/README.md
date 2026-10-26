# EmbeddingGemma2

## 一句话总结

EmbeddingGemma 2 是 Google DeepMind 于2026年10月6日发布的740M开源多模态嵌入模型，通过可选视觉与音频编码器把文本、图像、视频和音频映射为统一768维向量，支持本地跨模态检索，并可截为256维以将向量分量存储降至三分之一。

## 任务信息

- 序号：240
- 任务编号：TASK-20261021213238-16c3a731
- 热点编号：HS-20261021-article1792589558863748
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/多模态模型与模型架构
- 归类依据：指定分类null，自动判断。报告对象为模型发布及四模态共享向量空间和模块化编码器，按04模态边界归多模态模型；RAG仅用途，加载/MRL属于模型能力。已比较01/03/04，无指定值差异。
- 任务正文：Google DeepMind 开源 EmbeddingGemma 2，740M 多模态嵌入模型技术线索
- 任务来源：[原始任务来源](https://www.marktechpost.com/2026/10/06/google-deepmind-releases-embeddinggemma-2-a-740m-open-multimodal-embedding-model-built-on-gemma-4/)

## 交付件说明

- [EmbeddingGemma2.html](./EmbeddingGemma2.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [EmbeddingGemma2.pptx](./EmbeddingGemma2.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [EmbeddingGemma 2 model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2)：参数组成、架构、768维、8K、MRL质量与维度表、精度及任务前缀限制；官方full-precision自报，非独立复现。
- [Multimodal Embeddings with EmbeddingGemma 2](https://ai.google.dev/gemma/docs/embeddinggemma/multimodal-embeddinggemma-with-sentence-transformers)：按需模态加载、图音视频输入、视频默认1FPS/最多32帧、图像token预算及交错输入示例。
- [Gemma releases](https://ai.google.dev/gemma/docs/releases)：2026年10月6日发布及740M版本记录。

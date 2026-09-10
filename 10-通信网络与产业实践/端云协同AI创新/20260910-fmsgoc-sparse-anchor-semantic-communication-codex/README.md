# FMSGOC-稀疏锚点语义通信

## 一句话总结

FMSGOC 是面向带宽受限图像传输的基础模型引导语义通信框架，2026年9月7日论文 v1 通过 CLIP 选取稀疏潜变量锚点、LoRA 扩散补全与逐步锚点重注入，在 AWGN 10 dB 实验条件下报告 0.039 coded BPP 以及 CIFAR-10／ImageNet 的 0.1278／0.1558 LPIPS，为通信端侧语义筛选与接收侧生成恢复提供研究依据。

## 任务信息

- 序号：121
- 任务编号：TASK-20260910205425-beb2a4dc
- 热点编号：HS-20260910-article1789044866186640
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：10-通信网络与产业实践/端云协同AI创新
- 归类依据：任务 category 为 null，自动归类；已阅读分类总则以及10和04板块细则，正文主贡献是跨通信信道的发送端锚点选择、比特预算与接收端恢复协作，端云协同AI创新承接基于网络的AI协作；CLIP及Stable Cascade作为已有模型组件，未发布新的通用多模态基础模型，因此不归04-AI模型；未限定实时通话或视频业务，也不归话音、消息与实时通信；不与指定值存在差异。
- 任务正文：FMSGOC框架利用基础模型先验实现0.039 BPP语义通信，保持高保真度技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.07853)

## 交付件说明

- [FMSGOC-稀疏锚点语义通信.html](./FMSGOC-稀疏锚点语义通信.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [FMSGOC-稀疏锚点语义通信.pptx](./FMSGOC-稀疏锚点语义通信.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

0.039 BPP按论文公式含索引、估计潜变量信息量、24-bit CRC及码率2/3的LDPC，但文本提示同步、量化参数及完整协议开销未明确；实验使用真实图像类别提示、AWGN 10 dB和H100，CLIP相似度不等于像素一致或下游任务准确率，锚点之外生成内容可能失真，ImageNet泛化相对本次LoRA训练而非基础模型从未接触，端侧算力、端到端时延、衰落信道及真实业务收益未实证。

## 引用信息源说明

- [Foundation Models for Generalizable Semantic and Goal-Oriented Communication (arXiv:2609.07853v1)](https://arxiv.org/abs/2609.07853v1)：唯一批准的一手来源；支撑系统结构、锚点保持机制、coded BPP计数、CIFAR-10与ImageNet评测及实验边界。

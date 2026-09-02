# LLM.265 视频编解码张量压缩

## 一句话总结

截至 MICRO 2025 论文版本，LLM.265 将成熟视频编解码器用于 LLM 张量传输压缩，在论文覆盖的模型、任务和链路设置下量化验证压缩率、精度与端到端性能取舍。

## 任务信息

- 序号：40
- 任务编号：`PPTRANS-20260902-006`
- 热点编号：PP推理传输优化｜微损压缩
- 周期：2026-09
- 任务正文：方法类别：微损压缩
论文名：LLM.265: Video Codecs are Secretly Tensor Codecs
摘要：将激活、KV、权重和梯度重排为适合视频编码器处理的数据，并复用 GPU 视频编解码硬件完成张量压缩。该方法可用于训练和推理，PP 阶段间激活通信量可降低约 78%；激活压缩约为 3.5 bit/value，但属于有损方案。
- 任务来源：[https://doi.org/10.1145/3725843.3756078](https://doi.org/10.1145/3725843.3756078)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [LLM.265 作者公开论文](https://users.cs.duke.edu/~ml579/papers/llm265_micro2025.pdf)：用于支撑方法设计、实验设置与量化结果。
- [LLM.265 官方代码仓库](https://github.com/Entropy-xcy/llm.265)：用于支撑实现形态与复现入口。

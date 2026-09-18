# GVA-按需键重建

## 一句话总结

2026年9月15日的GVA论文v2提出面向自回归推理的分组值缓存及按需键重建机制，在约350M参数、30B FineWeb-Edu训练tokens条件下使拟议持久缓存标量较同配GQA减少约45–47%、五项零样本任务平均准确率达44.35%，但尚未报告解码吞吐或服务峰值显存收益。

## 任务信息

- 序号：135
- 任务编号：TASK-20260916021217-5e3fb097
- 热点编号：HS-20260916-dsh-tech-insight
- 周期：2026-W38
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：任务category为null，自动分类；已比较03与04细则。主要问题和直接贡献是KV缓存表示压缩，03明确KV机制归KV Cache，因此归03-AI推理与服务加速/KV Cache；04-AI模型/文本模型与模型架构作为次要关联，未指定分类故无调用方约束差异。
- 任务正文：📌GVA 注意力：通过按需重建键实现高效 KV 缓存
原文标题：Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction
元信息：战略 · 2026/09/16 · 编号 #16 · 47%；For the configurations studied, this representatio
要点：
- 在所测配置下，persistent cache 词元量较同配 GQA 减少约 45-47%For the configurations studied, this representation reduces persistent cache scalars by approximately 45-47% relative to matched GQA
技术效果：效果 · 上下文窗口：内存占用：据 arXiv:2609.13285：GVA 仅存储分组值并通过学得线性映射 K=V M 重建内容键，persistent cache 词元量较同配 GQA 减少约 45-47%（350M 参数、30B FineWeb-Edu tokens 下五项任务平均准确率 44.35，与 GQA 的 44.36 持平、优于 MLA 的 43.88）；作者明确指出当前实验尚未建立延迟或解码吞吐增益，预计开源自研解码内核
背景补充：据 arXiv:2609.13285：arXiv:2609.13285（Vishesh Tripathi 等，FrontiersMind，2026/09/08）提出 GVA，与相关工作 GTA（arXiv:2506.17286，声称较 GQA 削减 62.5% 注意力 FLOPs、缩小 KV 缓存 70%、端到端推理速度 2×）同属分组/潜在注意力路线，但均未在推理延迟与解码吞吐上获得验证
源链接：https://arxiv.org/abs/2609.13285
- 任务来源：[原始任务来源](https://arxiv.org/abs/2609.13285)

## 交付件说明

- [GVA-按需键重建.html](./GVA-按需键重建.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [GVA-按需键重建.pptx](./GVA-按需键重建.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

仅约350M参数、30B FineWeb-Edu、三seed五任务；缓存数为表示层标量推导，未证明峰值服务显存、吞吐或延迟收益。v2 PDF和HTML表2为44.35，而abs页面44.18，保留差异不归因于版本变化。GTA仅背景纠偏，非本报告比较证据。

## 引用信息源说明

- [Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction（v2）](https://arxiv.org/abs/2609.13285v2)：论文身份、版本与摘要页面数值差异
- [GVA v2全文](https://arxiv.org/html/2609.13285v2)：机制、缓存公式、表2准确率与局限
- [GVA v2 PDF](https://arxiv.org/pdf/2609.13285v2)：交叉核对第1页摘要和第8页表2的44.35

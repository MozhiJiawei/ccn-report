# EvoResearcher-自确认早停

## 一句话总结

2026年8月19日arXiv v1论文提出EvoResearcher，在冻结LLM上通过生成、批评、修订与CONFIRMED标记控制反思预算，其100题BBH深度扫描在D=2至4时报告82%–88%提前停止、约2次generations且准确率73%–74%，为固定多轮反思提供有成本边界的停止机制。

## 任务信息

- 序号：81
- 任务编号：ISSUE36-20260910-005
- 热点编号：HS-20260910-evoresearcher
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：已验证贡献是推理期早停与生成预算控制，直接限制输出与反思深度；多智能体及环境扩展只是未验证蓝图，故归输入输出数据。
- 任务正文：EvoResearcher以自我确认提前停止，等精度下减少推理轮次技术线索

线索来源：https://github.com/MozhiJiawei/Mozhi-s-AgentWorkspace/issues/36
Issue 所附来源：https://arxiv.org/abs/2608.18884
论文主来源：https://arxiv.org/abs/2608.18884
来源核对备注：Issue 原始论文链接完全一致。核心收益为等精度下提前停止、控制推理成本，不应表述为准确率显著提升。
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.18884)

## 交付件说明

- [EvoResearcher-自确认早停.html](./EvoResearcher-自确认早停.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [EvoResearcher-自确认早停.pptx](./EvoResearcher-自确认早停.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

证据边界：提前停止比例不是节省比例，约2.1次generations仍多于单次回答；CONFIRMED不是正确性保证，Table 8错误且确认占全部样本16%。不同实验/样本量不拼接，generations不擅自换算完整API调用；多智能体、GRPO训练和动态环境图仅为设计蓝图。Docling因资源限制未执行，不宣称完整混合解析合同通过。

## 引用信息源说明

- [Training-Free Inference-Time Self-Reflection and Cost-Bounded Early Stopping for Large Language Models](https://arxiv.org/abs/2608.18884v1)：支持冻结骨干反思协议、CONFIRMED早停、深度与成本实验、错误确认率、跨域结果和未验证扩展边界。

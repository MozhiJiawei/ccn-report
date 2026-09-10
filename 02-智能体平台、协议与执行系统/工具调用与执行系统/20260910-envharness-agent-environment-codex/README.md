# EnvHarness

## 一句话总结

Google Cloud AI Research 等团队于2026年8月20日在EnvHarness论文v1中提出以Stage、Contract、Chain包装已有智能体环境的reset/step接口，并用EnvRigger按轨迹弱点自动生成和验证包装组件，在保留原任务验证器的前提下，相比原环境技能使ALFWorld分布外成功率提高9.0个百分点、SWE-bench Verified平均执行步数减少约9.8%。

## 任务信息

- 序号：92
- 任务编号：TASK-20260910152103-aa7ffc06
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/工具调用与执行系统
- 归类依据：category为null，按正文自动分类。核心交付为环境交互执行装饰器和生成验证闭环，主实验以冻结策略提取技能；模型训练为RL补充应用，评测基准仅用于验证，因此唯一归入02/工具调用与执行系统。与指定值无差异。
- 任务正文：谷歌ENVHarness
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.19880)

## 交付件说明

- [EnvHarness.html](./EnvHarness.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [EnvHarness.pptx](./EnvHarness.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

论文v1作者实验，未做独立复现；+9.0pp对应ALFWorld OOD，9.8%对应SWE-bench执行步数，非综合平均或成本；Chain不在自动主流水线内；RL的ALFWorld OOD下降0.8pp；需reset/step及验证时确定性reset；环境设计循环有额外开销。 解析降级：GROBID正文TEI/XML成功；Docling两次因PDF页数兼容检查41 != -1失败，使用PyMuPDF原PDF页面渲染替代图表素材，未生成通过验证的混合XML与Docling图像索引。

## 引用信息源说明

- [EnvHarness: Awakening Static Worlds for Agent Learning (v1)](https://arxiv.org/abs/2608.19880v1)：唯一批准原始来源，支撑机构、机制、实验数字和局限

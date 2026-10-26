# LensVLM-选择性上下文展开

## 一句话总结

2026年10月9日论文v4中的LensVLM通过低清页面概览与按需回读原文，在七项文本问答中以包含展开输入的4.3倍有效压缩取得68.9%平均准确率，比全文参照72.4%低3.5个百分点。

## 任务信息

- 序号：256
- 任务编号：TASK-20261021221242-c5f9783b
- 热点编号：HS-20261021-article1792591963252523
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/输入输出数据
- 归类依据：任务category=null，已阅读分类总则及02/03/04细则。核心贡献是改变推理输入表征，用压缩页面与按需展开减少reader输入token，03/输入输出数据直接承接输入压缩；9B模型后训练和工具调用是实现手段，未提出新的多模态模型架构或通用Agent平台，故不归04多模态模型或02记忆与上下文系统。无指定分类差异。
- 任务正文：苹果联合杜克发布LensVLM，压缩页面加展开工具实现4.3倍有效压缩技术线索
- 任务来源：[原始任务来源](https://www.jiqizhixin.com/articles/2026-10-14-10?source=rss)

## 交付件说明

- [LensVLM-选择性上下文展开.html](./LensVLM-选择性上下文展开.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [LensVLM-选择性上下文展开.pptx](./LensVLM-选择性上下文展开.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [LensVLM论文v4](https://arxiv.org/abs/2605.07019v4)：支撑选择性展开机制、ICR/ECR定义、七项问答准确率与分上下文长度的效率实验。
- [Apple Machine Learning Research官方页](https://machinelearning.apple.com/research/lensvlm-context-expansion)：核对Apple与杜克作者、方法定位与官方摘要；页面仅显示July 2026。
- [LensVLM官方代码固定提交](https://github.com/apple-aiml-research/ml-lensvlm/tree/10709a7e2a80bdf971628359d47e4bd35fce3d95)：核对read_page原文/高清回读路径、公开推理与评测范围、代码和模型许可边界。

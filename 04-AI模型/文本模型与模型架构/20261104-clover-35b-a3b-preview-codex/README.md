# Clover-35B-A3B-Preview

## 一句话总结

DiffuSpace 在 2026 年 10 月发布 Clover-35B-A3B-Preview，这款约 350 亿总参数、30 亿激活参数的纯文本 MoE 模型通过块内并行去噪生成文本，在发布方 49 项 WebMCP 任务各试 3 次的评测中实现 1.52 秒的中位执行时间，同口径 Gemini 3.6 Flash 为 8.86 秒。

## 任务信息

- 序号：326
- 任务编号：TASK-20261104090435-447cff25
- 热点编号：HS-20261104-article1793754276030162
- 周期：2026-W45
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：任务 category 为 null，按主要贡献自动归类。正文解释 DiffuSpace 发布的纯文本 MoE 模型与双向 GDN 块扩散生成，WebMCP 是能力验证场景，推理解码及 Agent 评测是关联。与现有同任务归档一致。
- 任务正文：扩散智能发布Clover-35B-A3B-Preview，网页Agent中位执行1.52秒快于Jev组合快报
- 任务来源：[原始任务来源](https://www.36kr.com/p/4045119600399241)

## 交付件说明

- [Clover-35B-A3B-Preview.html](./Clover-35B-A3B-Preview.html)：可离线打开的 SingleFile 来源理解报告。
- [Clover-35B-A3B-Preview.pptx](./Clover-35B-A3B-Preview.pptx)：一页式可编辑技术洞察汇报。

## 引用信息源说明

- [DiffuSpace 官方发布稿](https://huggingface.co/blog/Diffuspace/clover-35b-a3b-preview)：Clover Preview 发布、BD-GDN 结构、WebMCP 实验与 Decision Model 的独立历史准确率口径。
- [DiffuSpace 官方发布稿中文镜像](https://diffuspace.ai/blog/clover-35b/)：官方中文表述，核对 WebMCP 对照与 Jev 属于不同实验。
- [DiffuSpace 官方 WebMCP 演示与结果](https://cdn-uploads.huggingface.co/production/uploads/6acdfff3ba3f94d149efc9a9/d2Oifoo7BOmv5DEag5OqF.mp4)：00:18 六项业务演示及 00:28.5 WindTunnel 汇总图，三项耗时、通过次数和计时边界。
- [Clover 固定模型卡与参考实现](https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview/tree/4b0402b65e523d0183a14c431955438714cb16ff)：Qwen 衍生纯文本 MoE、参数量、参考块大小、去噪筛选与缓存提交。
- [Clover 官方 GitHub 固定版本](https://github.com/DiffuSpace/Clover-35B-A3B-Preview/tree/e5a130a48e4a6d6c1d05c1c2338bce555d674044)：推理代码公开与 SGLang、llama.cpp 接入路径。
- [Dream 7B](https://arxiv.org/abs/2508.15487)：同团队扩散语言研究路线背景。
- [Block Diffusion](https://arxiv.org/abs/2503.09573)：按块生成的通用算法背景。

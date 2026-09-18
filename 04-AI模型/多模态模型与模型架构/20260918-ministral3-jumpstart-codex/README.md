# Ministral3-JumpStart

## 一句话总结

AWS于2026年9月14日宣布在SageMaker JumpStart提供Ministral 3 3B与8B Instruct 2512视觉语言模型，两款模型分别采用3.4B或8.4B语言模型加0.4B视觉编码器、支持256K上下文且官方FP8显存规格分别为8GB和12GB，为资源受限的图像理解、多语种及工具调用应用提供可部署模型。

## 任务信息

- 序号：132
- 任务编号：TASK-20260915071115-bbd93458
- 热点编号：HS-20260915-dailyreport-23
- 周期：2026-W38
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/多模态模型与模型架构
- 归类依据：category为null，按正文主贡献自动归类；核心对象是具有视觉编码器的紧凑多模态模型本体、版本及能力，JumpStart为可用性渠道，未提出云资源治理或Serving优化新机制；原任务训练效率标签缺少证据，不据此归入模型训练；没有指定分类差异。
- 任务正文：Ministral-3-3B-Instruct-2512 and Ministral-3-8B-Instruct-2512 models now available on Amazon SageMaker JumpStart

|- These two models from the Ministral 3 family bring compact, vision-capable language models purpose-built for edge deploy…
**效果：训练效率：数据不足，待人工补全。**
- 任务来源：[原始任务来源](https://aws.amazon.com/about-aws/whats-new/2026/01/ministral-3-3b-instruct-2512-ministral-3-8B-Instruct-2512-jumpstart/)

## 交付件说明

- [Ministral3-JumpStart.html](./Ministral3-JumpStart.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Ministral3-JumpStart.pptx](./Ministral3-JumpStart.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

AWS页面日期为2026-09-14，URL中的2026/01不作发布日期。

8GB/12GB为官方FP8容纳规格，未提供完整运行条件，不能推导任意256K上下文或高并发的显存需求。

没有训练时长、吞吐、算力或成本实验，不声称训练效率提升。

模型卡Reasoning、Instruct、Base基准对应不同变体，不能混用。

## 引用信息源说明

- [AWS Ministral 3 3B/8B JumpStart公告](https://aws.amazon.com/about-aws/whats-new/2026/01/ministral-3-3b-instruct-2512-ministral-3-8B-Instruct-2512-jumpstart/)：上架日期、JumpStart部署入口及显存规格
- [Mistral AI Ministral 3 3B Instruct 2512官方模型卡](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512)：3B架构组成、上下文、FP8、图像与工具调用能力及许可证
- [Mistral AI Ministral 3 8B Instruct 2512官方模型卡](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)：8B架构组成、交错滑窗注意力、上下文与部署规格

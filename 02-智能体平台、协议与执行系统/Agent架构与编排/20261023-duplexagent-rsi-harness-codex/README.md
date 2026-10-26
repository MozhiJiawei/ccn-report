# DuplexAgent-RSI

## 一句话总结

2026年10月8日，港中深与Amphion提出DuplexAgent-RSI，通过冻结模型权重、从对话轨迹诊断并修订六模块协调层，在排除感知失败的VoiceChat开发集固定核心测试中将协作分数Q从54.6提高至85.3。

## 任务信息

- 序号：258
- 任务编号：TASK-20261021221806-a505769a
- 热点编号：HS-20261021-article1792592287053784
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：指定分类原值null，依据正式全文自动分类。主要贡献是固定交互与委派模型、将任务委派/取消/替换/交付协调层拆为六模块并迭代，归02-智能体平台、协议与执行系统/Agent架构与编排。已对照05模型训练及02记忆/评测边界：未进行参数学习，记忆与模拟评测均服务协作编排闭环，不构成主归属。无指定分类差异。54.6到85.3限定VoiceChat development fixed-core Q且排除感知失败，非未见集泛化或端到端成功；r10为十轮当前版本，保留多余委派上升、未单列sealed成绩与未披露总成本边界，未宣称代码公开复现。
- 任务正文：港中深提出DuplexAgent-RSI，不改权重将协作分数从54.6提升至85.3技术线索
- 任务来源：[原始任务来源](http://mp.weixin.qq.com/s?__biz=Mzk3NTQxNTEwNQ==&mid=2247487969&idx=1&sn=7ef78f1e7f784fc88ebf5490b8a0dfbf&chksm=c5b84f864ad91feb5001238cca6335686b5bb15ec372e67b6cded26138b6a8ad1a4338e758c9&scene=0&xtrack=1#rd)

## 交付件说明

- [DuplexAgent-RSI.html](./DuplexAgent-RSI.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [DuplexAgent-RSI.pptx](./DuplexAgent-RSI.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [DuplexAgent-RSI原始论文（固定v1）](https://arxiv.org/abs/2610.11299v1)：支撑六模块harness、任务账本与迟到结果过滤、RSI配对门禁、Q定义、固定核心54.6到85.3及隔离/成本/负向结果边界。
- [DuplexAgent-RSI作者官方项目页](https://amphionteam.github.io/DuplexAgent-RSI-Demo/)：支撑原始架构图、原始消融图和六模块解释，核对Code coming soon发布状态；实验口径以固定v1论文为准。

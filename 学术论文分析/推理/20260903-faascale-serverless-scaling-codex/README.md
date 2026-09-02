# FaaScale 无服务器 LLM 扩缩容

## 一句话总结

截至 MLSys 2026 论文版本，FaaScale 通过分层权重装载与资源协同缩短无服务器 LLM 推理扩容路径，并在论文平台和工作负载下量化验证启动与服务性能收益。

## 任务信息

- 序号：53
- 任务编号：`PPTRANS-20260902-019`
- 热点编号：PP推理传输优化｜网络/传输协议
- 周期：2026-09
- 任务正文：方法类别：网络/传输协议
论文名：FaaScale: Unlocking Fast LLM Scaling for Serverless Inference
摘要：针对无服务器 LLM 扩缩容时高昂的模型传输成本，提出流水线化多播推理：PipeCast 自适应多播模型块，并在传输过程中动态形成跨节点 PP 推理流水线。该方案将模型分发与可用分块的即时执行结合，在真实 LLM 轨迹上将尾部 TTFT 最多降低 5 倍、成本降低 31.3%。
- 任务来源：[https://proceedings.mlsys.org/paper_files/paper/2026/hash/6e32c247076c2c0fb381e022c02d2c78-Abstract-Conference.html](https://proceedings.mlsys.org/paper_files/paper/2026/hash/6e32c247076c2c0fb381e022c02d2c78-Abstract-Conference.html)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [FaaScale 原始论文](https://proceedings.mlsys.org/paper_files/paper/2026/file/6e32c247076c2c0fb381e022c02d2c78-Paper-Conference.pdf)：用于支撑系统设计、实验设置和量化结果。
- [FaaScale MLSys 论文页](https://proceedings.mlsys.org/paper_files/paper/2026/hash/6e32c247076c2c0fb381e022c02d2c78-Abstract-Conference.html)：用于支撑正式发表元数据与摘要。

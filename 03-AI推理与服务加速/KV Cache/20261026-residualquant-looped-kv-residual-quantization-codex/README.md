# ResidualQuant-循环KV残差量化

## 一句话总结

ResidualQuant是2026年10月提出的循环Transformer KV缓存量化方法，以INT4末轮锚点和INT2跨轮残差将理论KV存储减少80.7%，在Ouro-1.4B、RTX 5090和16k上下文的固定batch=2解码测试中将吞吐从34.0提升至93.1 tokens/s（2.73倍）。

## 任务信息

- 序号：289
- 任务编号：TASK-20261026152203-e156ede1
- 热点编号：HS-20261026-article1792999323512171
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：API指定分类null，自动分类。已比较03和04板块细则，本文直接贡献是循环模型推理中的KV缓存量化与读取开销优化，03/KV Cache明确承接；循环Transformer是适用结构，非新模型架构，吞吐为KV优化结果，非解码采样机制，因此不归04/文本模型或03/解码。无指定分类差异。
- 任务正文：ResidualQuant将循环Transformer KV缓存压至INT2，解码吞吐提升2.73倍技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.10381)

## 交付件说明

- [ResidualQuant-循环KV残差量化.html](./ResidualQuant-循环KV残差量化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [ResidualQuant-循环KV残差量化.pptx](./ResidualQuant-循环KV残差量化.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals（arXiv v1）](https://arxiv.org/abs/2610.10381v1)：末轮锚点、LS缩放、学习旋转和混合精度机制；理论KV统计口径、两模型四任务质量、RTX5090固定和扩大batch解码吞吐及实现边界。

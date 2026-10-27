# Dual-QK-KV量化

## 一句话总结

Dual-QK是2026年10月提出的KV缓存压缩方法，通过成对非正交Q/K变换结合INT2量化与动态通道选择，在128K上下文下估算KV存储压缩6.8倍，并在Qwen3-4B、90K输入、batch=1、RTX PRO 6000 Blackwell测试中将解码吞吐从24提升至90 tokens/s（最高3.75倍）。

## 任务信息

- 序号：291
- 任务编号：TASK-20261026152228-507e7c25
- 热点编号：HS-20261026-article1792999348204037
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：API指定分类null，自动分类。已加载03与04细则，主要贡献是推理时KV缓存量化与读取压缩，03/KV Cache明确承接；Q/K表示变换为缓存优化手段，非模型本体新架构。吞吐提升来自KV缓存优化，不属采样或投机解码。无指定分类差异。
- 任务正文：Dual-QK 用非正交查询键变换实现 2-bit KV 缓存，128K 上下文压缩 6.8 倍、解码吞吐提升 3.75 倍技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.09827)

## 交付件说明

- [Dual-QK-KV量化.html](./Dual-QK-KV量化.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Dual-QK-KV量化.pptx](./Dual-QK-KV量化.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches（arXiv v1）](https://arxiv.org/abs/2610.09827v1)：支撑成对非正交变换、INT2与动态查询通道剪枝、BF16保护和bucket RoPE机制，128K格式估算、90K实测吞吐及精度损失边界。

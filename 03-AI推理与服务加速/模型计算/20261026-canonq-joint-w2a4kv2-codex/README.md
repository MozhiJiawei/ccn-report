# CanonQ

## 一句话总结

CanonQ是Meta AI于2026年10月6日arXiv v1提出的LLM联合量化感知训练框架，通过固定HDP、能量归一化和冻结高斯参考码本实现W2A4KV2，在LLaMA3-8B上将WikiText-2困惑度从ParetoQ的134.36降至9.41、八任务平均准确率从37.87%升至59.81%，为极低位推理压缩提供已验证的质量恢复路径，但实际部署存储和吞吐收益尚未测量。

## 任务信息

- 序号：288
- 任务编号：TASK-20261026152158-aa7bb516
- 热点编号：HS-20261026-article1792999318220738
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：API指定null，自动分类。已加载03细则，主体是权重/激活/KV统一量化编解码与整体推理模型压缩，模型计算直接承接；KV为联合对象之一而非缓存管理主贡献，QAT是实现手段；无指定分类差异。
- 任务正文：CanonQ 统一量化框架实现 W2A4KV2 极低位压缩，困惑度最高降 14.28 倍技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.09202)

## 交付件说明

- [CanonQ.html](./CanonQ.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [CanonQ.pptx](./CanonQ.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Few Bits, One Law: Toward W2A4KV2（arXiv v1）](https://arxiv.org/abs/2610.09202v1)：统一量化方法、原始图1、表1结果、消融、配置公平性、附录A.4表示开销及部署未验证边界。

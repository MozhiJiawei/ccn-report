# Dynamo-EPD多模态推理

## 一句话总结

NVIDIA 于2026年9月9日说明 Dynamo 通过独立视觉编码工作单元与NIXL嵌入传输解耦编码和预填充/解码，在Qwen3.5-122B-A10B NVFP4、4张GB200的10图×256视觉token、输出1024 token测试中，同置编码使平均首token延迟降低58%，但长输出低图负载可能抵消收益。

## 任务信息

- 序号：111
- 任务编号：TASK-20260910205029-36eb6c14
- 热点编号：HS-20260910-article1789044629411786
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/推理部署
- 归类依据：任务category为null，自动归类；加载03与08细则后，依据正文主要贡献是E与PD推理阶段拆分及同置/异构部署而归入03-AI推理与服务加速/推理部署。异构GPU只是部署实现，不以多租户资源治理为主体；没有指定分类与AI判断的差异。
- 任务正文：NVIDIA Dynamo实现编码-预填充-解码分离，多模态推理TTFT提升5倍技术线索
- 任务来源：[原始任务来源](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)

## 交付件说明

- [Dynamo-EPD多模态推理.html](./Dynamo-EPD多模态推理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Dynamo-EPD多模态推理.pptx](./Dynamo-EPD多模态推理.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

官方引言最多5× TTFT和7× E2E是条件最佳宣称，不能泛化到所有请求；正文热图25–93% TTFT降低与引言倍数没有明确对应同一单元。主实验Qwen3.5-122B-A10B NVFP4、4×GB200；异构编码另加2×RTX6000D；视觉嵌入链路峰值20Gbps，所有基准开启前端并行媒体解码，goodput定义为ITL<100ms。10图×256token、OSL1024的异构goodput提高70%保持GB200数量不变，但不等于总硬件成本不变。5图×128token、OSL2048同置E2E回退2.5%；27B同置goodput仅为聚合0.65×。本文实验重点为E与PD角色分离，不能推断每个实验将P和D再各占独立硬件。

## 引用信息源说明

- [When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)：官方原始技术博客，支撑机制、三种拓扑、实验配置、指标收益及适用边界。

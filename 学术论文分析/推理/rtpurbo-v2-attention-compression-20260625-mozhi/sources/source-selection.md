# Source Selection: 阿里 RTPurboV2 注意力压缩技术

## 输入类型

web

## 名称口径

用户输入为“阿里 PTR 团队开源 PTRurboV2 注意力压缩技术”。公开资料中更一致的写法是：

- 团队：阿里 RTP 团队 / RTP-LLM
- 技术：RTPurboV2
- 开源项目：RTP-LLM

后续研究默认按 `RTPurboV2` 处理，并在证据基线中说明该名称校正。

## 原始页面（最多 3 个）

1. Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps - arXiv
   - URL: https://arxiv.org/abs/2605.16928
   - 选择理由：RTPurbo 论文入口，提供作者、版本、摘要与核心实验口径；v2 于 2026-06-08 更新，和 RTPurboV2 新闻发布同日。

2. 阿里 RTPurboV2：原生 Transformer 再次崛起，百步训练实现 10 倍稀疏注意 - 机器之心 / 腾讯新闻镜像
   - URL: https://news.qq.com/rain/a/20260608A03CGK00
   - 选择理由：直接介绍 RTPurboV2 的公开技术解读，包含 16~32 倍 Full Attention 计算压缩、600 步训练、最高 9.36 倍 Prefill 加速、Qwen3-Coder-30B-A3B 与 Qwen3.5-35B-A3B 评测信息。

3. alibaba/rtp-llm - GitHub
   - URL: https://github.com/alibaba/rtp-llm
   - 选择理由：阿里 RTP-LLM 开源仓库，适合核验“已开源”的工程载体、推理引擎范围、仓库状态与是否能找到 RTPurboV2 相关实现/文档。

## 同类/相邻/竞品方案（2 个）

1. 仅需 15% 全量 Attention！RTPurbo 阿里 Qwen3 长文本推理 5 倍压缩方案 - 微信原文
   - URL: https://mp.weixin.qq.com/s/wFAJ6oG1CsKBJiCBE45BsQ
   - 对照角色：RTPurbo V1 前序方案，用于对照 V2 为什么从“85% 头替换为 SWA”继续压缩剩余 15% Full Attention。

2. Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention - arXiv
   - URL: https://arxiv.org/abs/2502.11089
   - 对照角色：代表“原生稀疏注意力/训练期架构改造”路线，用来对照 RTPurboV2 的后训练、低步数、保留 Full Attention 模型能力的定位。

## 待重点核验的问题

- 注意力压缩对象：区分流式头与召回头；流式头转 SWA，召回头采用低秩投影、聚类索引和动态 top-p。
- 压缩率：V1 的 5x KV/Attention 压缩、V2 对剩余 Full Attention 的 16~32x 计算压缩、是否对应端到端 10x 稀疏注意或 Prefill 9.36x。
- 精度影响：Ruler、LongBenchV2、CoT 等评测是否接近 Full Attention，在哪些长度/模型上成立。
- 吞吐/延迟收益：Prefill 与 Decode 分别收益，硬件、序列长度、模型、batch 和 kernel 口径。
- 适配模型范围：Qwen3-Coder-30B-A3B、Qwen3.5-35B-A3B；对 SWA+Full Attention 混合架构如 MIMO、Gemma 4、GPT-OSS 的推断边界。

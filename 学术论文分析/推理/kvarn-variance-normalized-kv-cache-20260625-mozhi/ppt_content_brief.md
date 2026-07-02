# PPT Content Brief

## Deck Metadata
主题：KVarN: Variance-Normalized KV-Cache Quantization
目标读者：推理系统/LLM Serving 工程负责人
页数口径：1 页；单页输出；只生成 Summary Page，不包含 cover、contents 或额外内容页。
核心结论：KVarN 值得进入复现和 serving 性能验证，但当前证据只能支持 2-bit 精度保真与局部开销低，不能直接支持线上 TPOT/TTFT 收益。
内容来源：review/source_understanding_review.html；sources/paper/source-summary.md；sources/paper/images/

## Summary Page
页码：Page 1
页面标题：华为发布了KVarN双轴KV量化
标题说明：KVarN 在 2-bit KV-cache 上保住推理、代码和指令任务质量，但论文尚未给出整网 TPOT/TTFT 收益
分析总结：
- 机制：新产生的 KV 分块写回前做旋转和双轴方差归一化，减少 token magnitude 漂移
- 收益：AIME24、MATH500、HumanEval、IFEval 上 2-bit 精度保持强，性能证据限于局部 overhead
正文内容：
【机制】
华为 KVarN 的切入点不是“再做一个低 bit KV-cache 压缩”，而是把评估对象从一次性 prefill 拉回真实长链 decoding。长链推理、代码生成和复杂指令会不断生成新 token；每个新 token 产生的 K/V 会写回 KV-cache，后续 token 又会读取这些已经被量化过的历史 K/V。如果每个 block 只产生一点量化误差，这些误差也会沿着 autoregressive decoding 路径继续被模型读取，最后表现为质量退化。论文因此提出 pseudo-decode 评测口径：序列按 block 切开，每个 block 产生后立刻量化写回，下一段只能读取量化后的 cache；这比 prefill-like 的一次性并行量化更接近线上长输出场景。

KVarN 进一步把误差来源定位到 token magnitude / scale error。可以把每个 key 向量理解成“方向 + 长度”：方向决定它在 attention 空间里指向哪里，长度会影响它被 query 匹配时的权重强弱。旧方法即使均方误差不算大，也可能把少数 token 的向量长度放大或缩小，形成 outlier error；论文 Figure 1 显示 top error 中 magnitude 贡献占主导，Figure 8 的 K magnitude 与 quantized K magnitude 联合分布也显示 KVarN 最贴近对角线。对 serving 工程负责人来说，这个机制判断很重要：KVarN 不是只优化平均 reconstruction error，而是在修复会随 decoding 被反复放大的 token scale 漂移。

KVarN 的处理链路是“Hadamard rotation + 双轴 variance normalization + round-to-nearest quantization”。Hadamard rotation 先在 channel 方向摊平 outlier，让待量化分布更适合低 bit 表示；随后 VarN 在 token 与 channel 两个方向交替做方差归一化，减少新产生 KV block 写回前的 token magnitude 漂移；最后再做 RTN 量化，并额外保存第二组 scale。论文给出的关键口径是约 2.3 bits/element，即 K/V 都按 2-bit 主体压缩，但因为 scale、zero-point 和第二组 scale，等效平均 bit 数略高于 2。这里的工程含义是：KVarN 更亲和能处理低 bit KV-cache、并能把 second scale 融进 dequant kernel 的 GPU serving 栈，例如论文使用 vLLM 和 Triton 口径讨论实现。

【收益】
论文最强的收益证据是“低 bit 下质量保真”，不是“整网推理已经更快”。Table 1 显示，在 AIME24 和 MATH500 上，KVarN 以 2/2 K/V、2.3 bits/elem 的设置接近 FP16，并优于 KIVI、QuaRot、KVQuant-1%、PolarQuant、TurboQuant、Kitty 等多个 baseline。以 Qwen3-4B 为例，AIME24 从 FP16 的 61.1% 到 KVarN 的 60.0%，MATH500 从 82.6% 到 79.2%；以 Phi-4-14B 为例，AIME24 从 62.2% 到 61.7%，MATH500 从 84.9% 到 84.8%。这些数字支撑的页面判断是：KVarN 在数学推理任务上可以把 KV-cache 压到低 bit，同时保持主要质量。

Table 2 和 Table 3 扩展了收益范围。HumanEval 上，KVarN 在 Qwen3-4B 为 88.4%，接近 FP16 的 88.8%；在 Phi-4-14B 为 88.2%，接近 FP16 的 88.9%，并明显好于 KIVI 在 Phi-4-14B 上的 74.6%。IFEval 上，KVarN 在 Qwen3-4B、Llama-3.1-8B、Phi-4-14B 的 prompt-level strict / loose 指标上保持或取得最高结果。对单页 PPT 来说，这组证据可以压成一句：KVarN 的质量证据覆盖数学推理、代码生成和指令跟随，不是只在一个 toy benchmark 上成立。

性能侧必须写得克制。论文给出的 Figure 6 是 VarN normalization 相对 128-token generation 的局部 overhead：Qwen3-4B 上 VarN all layers 为 1.9 ms，而 128-token generation 为 1050 ms，论文报告约 0.18%；Llama-3.1-8B 为 1.7 ms vs 3701 ms，Phi-4-14B 为 4.2 ms vs 6717 ms。Appendix I / Figure 11 进一步给出 Triton dequant 口径：4k、8k、16k、32k context 下 KVarN 与 KIVI 的 median dequant time 基本持平，原因是 second scale 被融合进 dequant kernel，避免额外 HBM round-trip。可见收益应该表述为“局部 normalization 和 dequant overhead 很低，支持进入 serving 复测”，而不是“已经证明 TPOT/TTFT 更好”。

这一页需要明确告诉读者：论文没有报告整网 serving 的 TPOT、TTFT、tokens/s、throughput 或 end-to-end latency；因此不能从本文证据直接推出首 token 更快、每 token latency 更低，或线上吞吐已经提升。真正的工程结论是“值得排期复现，但复现 gate 要设在端到端 serving 指标上”。建议验证指标包括：目标模型上的质量回归、长输出 TPOT、TTFT、tokens/s、显存上限、并发 batch 下的 KV-cache memory traffic、2-bit KV-cache kernel 可用性，以及 second scale 是否能在目标框架中融合。若本地 serving 框架不支持 2-bit KV-cache，或者 second scale 不能融合进 kernel，论文中的低 overhead 结论就不能直接照搬。
参考图片：
- ![Figure 2: KVarN 方法链路](sources/paper/images/picture_002.webp)
- ![Figure 1: token magnitude error 是 top error 主因](sources/paper/images/picture_001.webp)
- ![Table 1: AIME24 与 MATH500 质量结果](sources/paper/images/table_001.webp)
- ![Figure 6: VarN normalization 相对生成耗时的局部 overhead](sources/paper/images/picture_008.webp)
- ![Figure 11: Triton dequant overhead 与 KIVI 基本持平](sources/paper/images/picture_013.webp)
备注：
- 论文首页作者 Lorenz K. Muller、Philippe Bich、Chiara Boretti、Hyun-Min Chang、Jiawei Zhuang、Lukas Cavigelli 均标注 Huawei，代码仓库为 huawei-csl/KVarN。
- 单页讲法建议保持“值得复现，但不能承诺线上加速”的审慎口径；把 0.18% 明确称为 normalization overhead，不写成 TPOT/TTFT 收益。

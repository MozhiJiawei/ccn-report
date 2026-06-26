# KVarN Paper Source Summary

## 一句话主张

KVarN 认为长链推理的 KV-cache 量化不能只看一次性 prefill：在 autoregressive decoding 中，量化过的历史 KV 会被后续 token 继续读取，错误会按时间累积；主要问题不是方向误差，而是 token magnitude / scale 没保住。KVarN 用 Hadamard rotation 加双轴 variance normalization 修复 scale error，在 2-bit KV-cache 上改善 reasoning、coding 和 instruction following。

## 关键术语

- KV-cache：Transformer 推理时缓存每层 attention 的 key/value，避免每生成一个 token 都重算旧 token。
- Test-time scaling：通过更长推理链、更多生成步骤或更长上下文换取更强推理能力。
- Prefill：一次性处理已知 prompt；很多旧评测假设固定长上下文并行量化。
- Autoregressive decoding：模型逐 token 生成；新产生的 KV 写回 cache 后又被后续 token 读取。
- Token magnitude / scale error：量化后某个 token 的 key 向量长度被放大或缩小，导致 attention 几何关系偏离。
- Hadamard rotation：把 channel 方向的异常值摊平，让量化输入更接近均匀/高斯分布。
- VarN：在 token 和 channel 两个轴上做 variance normalization，记录第二组 scale。

## 证据索引

- Figure 1：top error 中 magnitude error 占主导；KVarN 比 KIVI / HK / VarN(K) 更好保持 token norm。
- Figure 2：KVarN pipeline：cache -> Hadamard rotated cache -> normalized cache -> RTN quantized cache。
- Figure 4：prefill 与 pseudo-decode 的差异；pseudo-decode 会把已量化历史 KV 继续喂给后续步骤。
- Figure 8：K magnitude 与 quantized K magnitude 的联合分布；KVarN 更贴近对角线。
- Table 1：AIME24 / MATH500；KVarN 在 Qwen3-4B 与 Phi-4-14B 的 2/2 bits、2.3 bits/elem 设置下接近 FP16 并优于多个 2-bit baseline。
- Table 2：HumanEval；KVarN 在 Qwen3-4B 88.4%、Phi-4-14B 88.2%，接近 FP16。
- Table 3：IFEval；KVarN 在 Qwen3-4B / Llama-3.1-8B / Phi-4-14B 上保持或取得最高 prompt-level accuracy。
- Figure 6：VarN normalization overhead 相对 128-token generation 很小：Qwen3-4B 1.9 ms vs 1050 ms，论文称 0.18%。
- Figure 11 / Appendix I：KVarN dequantization 在 Triton kernel 中把第二个 scale 融合进 dequant，避免额外 HBM round-trip；4k/8k/16k/32k context 下与 KIVI 单 scale dequant 基本持平。
- Appendix E/J：边界包括非 KV-cache 架构、MLA train-time compression 未明、serving 框架 2-bit KV-cache 支持不足；复现实验约 50 GPU days。

## 硬件亲和与性能判断

- 更亲和 GPU serving 场景，尤其是 vLLM / Triton 这类能写融合 dequant kernel 的栈。
- 亲和高 memory bandwidth 硬件，因为 KV-cache 解码常受 HBM 读写压力影响；论文测试硬件口径为约 500 TFLOP fp16、1.8 TB/s memory bandwidth。
- KVarN 额外开销主要有两类：每 128 token 新 chunk 的 VarN normalization，以及 dequant 时多一个 per-row scale。
- 论文声称 normalization 在 Qwen3-4B 上为 1.9 ms，相比 128-token generation 的 1050 ms 是 0.18%；Llama-3.1-8B 为 1.7 ms vs 3701 ms，Phi-4-14B 为 4.2 ms vs 6717 ms。
- dequantization overhead 在 Triton 测试中几乎不增加：4k/8k/16k/32k context 分别约 16.6/19.5/26.8/128.8 µs，和 KIVI 的 16.4/19.3/26.8/128.9 µs 基本一致。
- 论文没有报告整网 serving 的 TPOT、TTFT、tokens/s 或 end-to-end latency 收益；因此不能从本文证据直接得出“上线后首 token 更快”或“每 token latency 更低”的结论。
- 风险边界：如果 serving 框架无法支持 2-bit KV-cache、无法融合 second scale，或硬件不是高带宽 GPU，则论文的低 overhead 结论不能直接照搬。

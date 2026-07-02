# PPT Content Brief

## Deck Metadata
主题：2026 年 6 月，SGLang 通过内核与运行时深度优化，使 DeepSeek-V4 在 GB300 上吞吐量提升 5 倍
目标读者：AI 基础设施/推理平台技术负责人
页数口径：1 页；单页输出，只生成 Summary Page，不包含 cover、contents 或额外内容页。
核心结论：SGLang 不是靠单个 kernel 拉高峰值，而是把 prefill、decode、MoE、speculation 和 runtime hardening 连成一条更稳的 serving 路径。
内容来源：PyTorch Blog / SGLang Team 文章《Serving DeepSeek-V4 on GB300 with SGLang: 5x Higher Throughput at the Same Interactivity Since Day-0》；本轮 Source Understanding 审阅 HTML

## Summary Page
页码：Page 1
页面标题：SGLang团队发布了GB300优化复盘
标题说明：GB300 8K/1K 口径下，June MTP 在约 50 tok/s/user 处达到 Day-0 no-MTP 的约 5 倍吞吐
分析总结：
- 机制：MHC 融合、KV Compression V2、W4A4 MoE、SWA 预算和 CUDA graph 共同减少路径损耗
- 效果：GB300 lane 在约 50 tok/s/user 处从约 2,200 提升到约 11,200 tok/s/GPU
正文内容：
【机制】
这篇复盘的主线不是“GB300 更强所以更快”，而是 SGLang 团队把 DeepSeek-V4 的 serving 路径从 Day-0 的可运行状态继续推进到更适合高并发的生产形态。Day-0 栈已经能跑 DeepSeek-V4：支持 FP4 inference、MoE execution、DP/EP/TP recipe、prefill/decode disaggregation、speculative decoding，以及 decode 侧 CUDA graph。6 月的变化发生在更细的瓶颈层：prefill 侧减少 MHC 路径里的中间张量搬运和 stage boundary，decode 侧更准确地计算 full token 与 sliding-window attention tail 的内存预算，MoE 路径把 activation quantization 推到 W4A4 MegaMoE，runtime recipe 按不同并发和部署形态调 prefill-to-decode ratio、parallel plan、KV cache allocation、token/request limit。

MHC 融合对应的是 DeepSeek-V4 prefill 路径里的非矩阵乘开销。原文提到 SGLang 将大的 mhc_pre 路径改到更强的 DeepGEMM-backed flow，把 RMSNorm 融进 MHC path，并增加 dedicated fused hc_head kernel；后续又加入 fused mhc_fused_post_pre kernel。对一页 PPT 来说，可以把它表述成：prefill 不只是算 matmul，还会被 norm、head、post/pre 小 kernel 和调度边界拖住；融合的价值是减少 intermediate tensor traffic 和 scheduler-visible plumbing。

KV Compression V2 对应的是高并发下压缩与 indexer kernel 的效率。原文列出 c4、c128、online c128 compression kernels，以及 fused norm/rope V2 pieces。这里不要把它讲成泛泛的 KV cache 优化，而要讲成 DeepSeek-V4 在并发增加时，compression 和 indexer 不能成为新的瓶颈。W4A4 MegaMoE 则对应 FP4 MoE 路径：原先 DeepGEMM MegaMoE path 使用 W4A8 kernel，expert weights 是 MXFP4，但 activation path 仍量化到 MXFP8；W4A4 让 activation path 也走 MXFP4，原文称 negligible accuracy loss，并在更高吞吐 operating range 更能体现 MoE efficiency。

Runtime 部分是这次 5x 不能被简化为“kernel 优化”的关键。SWA 预算和 eviction/preallocation 行为决定 decode worker 能否在 disaggregated decode 里维持更高 effective batch size。原文提到修正 disaggregated decode SWA preallocation sizing，区分 full-length accounting 和 sliding-window pool 中真正需要常驻的 tail；随后又加强 waiting、running、transfer states 之间的 reservation logic。可见含义是：decode worker 不是理论上能批多大就能批多大，内存预算保守或错误会提前撞限，吞吐曲线会在高交互区间掉下去。

CUDA graph 和 hardening 是把性能前沿“稳住”的部分。DeepSeek-V4 prefill path 有足够多 irregular behavior，runtime 过去会退回 eager islands，导致 host-bound 和 GPU utilization 不稳。breakable CUDA graph for DP attention 与 speculative-path enablement 让更多 prefill path 回到 graph-friendly execution。bug fix 也不是附属项：PD-MTP metadata hidden-size bug、disaggregated decode + MTP 下 SWA double-free、MHC token-count bucket lazy compile、Blackwell FP8-einsum scaling NaN、Dynamo bootstrap-room DP rank imbalance，这些问题会让 speculative / disaggregated 路径在真实并发 sweep 中失真或崩掉。把这些修掉后，MTP acceptance、worker balance 和曲线可信度才一起恢复。

【效果】
核心数字来自原文 TL;DR 和 Performance Results：在 public SemiAnalysis InferenceX GB300 disaggregated lane 上，DeepSeek-V4 Pro、FP4、ISL=8192、OSL=1024、dynamo-sglang 的 June 2026 MTP curve 在约 50 tok/s/user 处达到约 11,200 tok/s/GPU；Day-0 April 2026 no-MTP curve 在相同用户可见交互性附近约为 2,200 tok/s/GPU，因此 headline comparison 是约 5x。这个 5x 必须带着口径讲：它不是所有 DeepSeek-V4 部署的通用倍数，也不是 GB300 硬件单独带来的提升，而是固定模型、硬件族、精度、输入输出长度、serving framework、serving mode 和 interactivity 点之后的曲线对照。

这页最应该让技术负责人记住两层效果。第一层是单点 headline：约 50 tok/s/user 处，吞吐从约 2,200 到约 11,200 tok/s/GPU，说明在接近真实用户交互速度的条件下，系统可以承载更多 token throughput。第二层是曲线形态：原文强调这不是 single-point win，no-MTP 和 MTP curves 都在整个 interactivity range 上移；Day-0 curve 在约 40 tok/s/user 之后陡降，而 June curves 能在更深的 high-interactivity region 维持吞吐。原文还给出 no-MTP 在 40 tok/s/user 处 2.1x、MTP 在 80 tok/s/user 处 2.6x 的补充比较，用来说明改善不是只靠 50 tok/s/user 这一点。

如果这页要做成单页 summary，视觉上建议让 GB300 曲线图成为主证据：横轴是 tok/s/user，代表用户可见生成速度；纵轴是 tok/s/GPU，代表单位 GPU 承载的 token throughput；要在图上标出约 50 tok/s/user 的取点，并把 Day-0 no-MTP 约 2,200 与 June MTP 约 11,200 以 callout 连接起来。旁边用一个简短机制链承接数字：kernel fusion 降低 prefill path overhead；KV Compression V2 与 W4A4 MoE 让 compression/MoE path 在高并发下更有效；SWA budgeting、decode admission、recipe dispatch 让 decode worker 维持更高 effective batch；CUDA graph 与 bug fix 让 speculative/disaggregated path 不再被 compile、NaN、double-free、metadata sizing 和 DP imbalance 拖垮。

边界也要在一页里说清。可说：SGLang 团队在这篇复盘中展示了 DeepSeek-V4 Pro 在 GB300 disaggregated 8K/1K lane 上，从 Day-0 到 June 的 serving frontier 变化，并把提升拆到 kernel、runtime、hardening 三类工程改造。谨慎说：这些机制对其他 MoE 模型、其他上下文长度、其他 serving mode 有启发，但不能直接声称同样 5x。不能说：SGLang 在所有 GB300 推理任务上提升 5 倍，或者 5x 完全来自某一个 PR、某一个 kernel、某一个硬件特性。对推理平台团队的决策含义是：复用价值不在照搬倍数，而在照着这条链路排查自己的 serving frontier，到底是 prefill kernel、decode memory accounting、MoE quant path、speculative acceptance、runtime graph capture，还是稳定性问题在压低高交互区间吞吐。
参考图片：
- ![DeepSeek V4 Pro on NVIDIA GB300](../sources/web/pytorch-sglang-deepseek-v4-gb300-5x/images/image-02.webp)
  这张图是单页 summary 的主证据图，展示 DeepSeek-V4 Pro 在 NVIDIA GB300 disaggregated 8K/1K lane 上不同曲线随 tok/s/user 变化的吞吐 frontier，可支撑约 50 tok/s/user 处 5x 的 headline comparison，以及 June 曲线在高交互区间更能维持吞吐的判断。
- ![Serving DeepSeek-V4 on GB300 with SGLang hero](../sources/web/pytorch-sglang-deepseek-v4-gb300-5x/images/image-01.webp)
  这张图可作为来源封面或小型 source locator，支撑材料出处，不应替代性能曲线作为主证据。
备注：
- 口径来自 SGLang Team and Community Contributors 在 PyTorch Blog 发布的文章正文；发布平台是 PyTorch，叙事主体和贡献者列表指向 SGLang Team / NVIDIA Team / Dynamo 相关协作。
- 讲述时先报数字，再报口径：GB300 8K/1K、DeepSeek-V4 Pro、FP4、dynamo-sglang、约 50 tok/s/user、June MTP 对 Day-0 no-MTP。
- 不要把 5x 外推为所有模型、所有请求长度、所有 GB300 部署或所有 SGLang 版本的通用收益。

# PPT Content Brief

## Deck Metadata
主题：RTPurboV2 注意力压缩技术
目标读者：AI Infra 技术负责人 / 架构负责人
页数口径：1 页；只生成 1 页 Summary Page；不包含 cover、contents 和内容页。
核心结论：值得受控复现；它的核心是把既有 Full Attention 模型迁移到可训练、可部署的稀疏注意力路径。
内容来源：Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps, arXiv:2605.16928；GROBID + Docling parsed XML package under .tmp/pdf_xml/full-attention-strikes-back-rtpurbo/；Approved source_understanding_review.html baseline

## Summary Page
页码：Page 1
页面标题：RTPurboV2实现稀疏注意力迁移
标题说明：它用少量后训练把既有 Full Attention 模型转成稀疏推理路径，决策时要分开看精度、模型范围和真实加速口径
分析总结：
- 迁移路径：用 head 分工、低维召回和动态 top-p，把全量注意力改造成稀疏推理
- 收益信号：长上下文和推理精度接近 Full Attention，并报告最高 9.36× prefill、约 2.01× decode 加速
正文内容：
【迁移路径】
AI Infra 视角下，RTPurboV2 最重要的回答不是“又提出一个稀疏注意力算子”，而是给既有 Full Attention 模型一条后训练迁移路径：不推倒重训 native sparse attention，不只做启发式 token eviction，而是先识别模型内部已经形成的稀疏结构，再把 full attention 的计算路径迁移成可部署的 sparse inference。这个判断来自论文的三个机制观察：第一，attention heads 已经出现功能分化，少数 retrieval heads 负责长程召回，多数 heads 主要依赖局部上下文或 sink tokens；第二，retrieval heads 的长程相关性主要由低维子空间承载，论文使用 16 维 token indexer 做候选召回，避免每次都用完整高维 QK 全量匹配；第三，不同 query 需要保留的 token 数差异很大，固定 top-k 要么浪费计算，要么漏掉复杂 query 的关键证据，因此 RTPurbo 使用动态 top-p 按 attention mass 选择有效 token。

这条路径可以概括成“head、feature、token 三层压缩”：head 层先决定哪些头还值得保留长程能力，feature 层用低维投影快速筛候选，token 层再按 query 动态决定实际参与 attention 的 token 集合。它压缩的不是单一对象，也不是粗暴裁掉 KV cache，而是把 Full Attention 中最贵的全头、全维度、全 token 匹配拆成三次更可控的选择。对架构负责人来说，这意味着 RTPurboV2 的价值不只是某个 benchmark 上的加速，而是把“已训练 Full Attention 模型是否能低成本稀疏化”变成一个可验证工程命题：先复现 head 校准和 token indexer，再验证动态 top-p 是否能在本地模型和业务长度上保持召回质量。

这个迁移路径也有明确边界。论文强支撑的是 RTPurbo 的后训练稀疏化范式，以及 Qwen 系长上下文 / reasoning 模型上的实验结果；外部材料中关于 RTPurboV2 的开源实现、聚类索引、16-32× Full Attention 计算压缩等发布口径，需要在后续技术评审中和 GitHub 实现、kernel 条件、模型配置逐项对齐。不要把“可迁移”理解成所有模型即插即用；更稳妥的表达是：RTPurboV2 提供了一条低成本注意力压缩路线，适合进入受控复现，而不是直接按发布数字规划线上容量。

【收益信号】
论文里的收益信号分成两类：精度是否守住，以及速度收益属于哪个阶段。精度上，RULER、ultra-long multi-hop 和 reasoning benchmarks 共同支撑“接近 Full Attention”的判断。RULER 表里，RTPurbo w/top-p 在 32K 和 64K 长上下文任务上明显优于固定 top-k 变体，尤其 multi-Q、multi-V、multi-K 这类需要跨远距离证据的任务，说明动态 token 预算比固定 4096 top-k 更能保护复杂 query 的召回质量。Ultra-long 图把长度拉到 128K-512K，RTPurbo 在 Multi-K、Multi-Q、Multi-V 三类多跳任务上仍保持较高 accuracy，同时黑线显示 high sparsity，说明它不是简单靠多算 token 换精度。Reasoning 表则换成 Qwen3-30B-A3B-Think，覆盖 AIME24、AIME25 和 MMLU-PRO；这些任务输入短但生成 reasoning traces 长，瓶颈转到 decode 阶段，RTPurbo w/top-p 仍接近 dense baseline，说明稀疏化没有明显破坏推理链。

速度上必须拆开口径。论文摘要报告最高 9.36× prefill speedup at 1M context，同时报告约 2.01× decode speedup；Figure 7 展示的是 sparse decoding latency，对照 Full Attention 的 FlashAttention-2，在 H=32、KV=128K/256K/512K 下约 1.96-1.99×。因此 Summary Page 上可以写“最高 9.36× prefill、约 2.01× decode”，但不能把它混成“端到端 9.36×”或“所有场景 9.36×”。面向决策时，应把收益拆成四个检查项：prefill 是否真的受 attention 主导，decode 的 KV 长度和 batch 是否匹配论文设置，kernel 是否可在目标硬件上复现，端到端吞吐是否被调度、采样、通信或非 attention 算子稀释。

这页的决策含义是：RTPurboV2 有足够证据进入下一阶段验证，但验证目标应被写清楚。第一阶段验证机制闭环：head 校准是否稳定、16 维 indexer 是否能保住 attention mass、top-p 是否明显优于 top-k。第二阶段验证收益闭环：在本地目标模型、目标上下文长度、目标硬件上分别测 prefill latency、decode latency、端到端 tokens/s 和精度回归。第三阶段验证泛化边界：Qwen3-Coder-30B-A3B、Qwen3-30B-A3B-Think 之外的模型是否仍有同样的 retrieval head 分布和动态 token 预算收益。只有这三层跑通，发布数字才有资格转成容量规划或产品 SLA 假设。
参考图片：
- ![Figure 4: RTPurbo overall architecture](assets/fig4-architecture.png)
- ![Figure 6: Ultra-long multi-hop accuracy and sparsity](assets/fig6-ultralong.png)
- ![Figure 7: Sparse decoding speedup](assets/fig7-speedup.png)
- ![Table 4: RULER accuracy comparison](assets/table4-ruler.png)
- ![Table 5: Reasoning benchmark accuracy](assets/table5-reasoning.png)
备注：
- 这页是单页 summary，建议视觉上突出“迁移路径”和“收益信号”两块。主视觉材料要配解释：Figure 4 用来说明迁移路径，Figure 6 / Figure 7 / Table 4 / Table 5 用来支撑精度与速度口径。不要把 9.36× prefill、2.01× decode 和端到端收益合并表达。

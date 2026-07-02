# PPT Content Brief

## Deck Metadata
主题：Geometry-Aware Online Scheduling for LLM Serving: SVF / 1-bit SVF
目标读者：AI Infra / LLM Serving 技术负责人
页数口径：1 页；只生成单页 Summary Page；不包含 cover、contents 或内容页
核心结论：SVF 值得进入 PoC 池；核心价值是 volume-first 调度指标，但必须把 predictor 自训、权重未发布和精度未充分披露作为复现边界。
内容来源：arXiv:2606.22327；本目录 `research_audit.md`；本目录 `evidence-board.html`；https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling

## Summary Page
页码：Page 1
页面标题：人大高瓴等发布SVF论文
标题说明：在 vLLM 与 Llama-3.1 实验中，SVF 用 KV cache volume 降低延迟；alpha=1/2 时竞争比为 5，高并发接近 3
分析总结：
- 机制：按预测输出长度计算请求的 memory-time volume，再以最小 volume 优先入队
- 效果：理论上收紧 prior 48 的竞争比上界，实验中 SVF 通常取得最低平均延迟
正文内容：
【机制】
这页要让技术负责人先记住一个判断：SVF 不是把 SJF 的输出长度预测做得更准，而是把 LLM serving 的调度成本从“一维时间”换成“二维内存面积”。论文把每个请求的输入 prompt 长度记为 s，把输出长度记为 o；prefill 阶段会先占住与 prompt 对应的 KV cache，decode 阶段每生成一个 token 又会继续增加 KV cache。因此一个请求在生命周期里占用的不是静态 job size，而是一块 memory-time volume：`v_i = s_i * o_i + (o_i^2 + o_i) / 2`。前半项对应 prompt 在输出期间持续占用的矩形面积，后半项对应 decode 逐步增长形成的三角面积。

SVF 的调度动作就是按这个 volume 从小到大 admission：后台 predictor 先批量预测输出长度，再把预测出的 `o_hat` 写成等待队列里的 priority；调度器从等待队列弹出最小 volume 请求，只要 KV cache 容量允许就放入运行批次。这个机制对 AI Infra 的意义在于，它不要求推翻 vLLM 的连续批处理引擎，而是作为 plug-and-play scheduler 改变等待队列的排序和 admission 顺序。换句话说，SVF 主要动的是“谁先进入活跃 batch”，不是重写模型推理 kernel。

1-bit SVF 是同一思路的轻量版本。它不回归精确输出长度，而是用 BERT-tiny binary classifier 只判断请求是 short 还是 long，再用类别代理长度计算 proxy volume。这个设计降低了预测负担，但不能被讲成“预测更准”。论文正文报告 predictor overhead：full regression predictor 最大约 0.06% E2E time，classifier 约 0.01%；但论文没有充分披露 predictor 的 accuracy、MAE、RMSE、F1 或误差分布。因此单页里应把它表述为“预测链路开销很低，但精度需要本地复测”。

【效果】
理论效果要分清口径。论文的定理 3.2 给出 burst arrival 下 SVF 的 worst-case competitive ratio：`CR <= 1 + 2/(1 - alpha)`，其中 `alpha = max_i p_i / M` 表示单个请求峰值内存占 GPU 总容量的比例。`alpha=1/2` 时表 1 给出 `CR <= 5.00`；当 alpha 趋近 0，也就是高并发、单请求只占很小容量时，竞争比上界趋近 3。这里不能写成“实测性能提升 48 到 5 倍”。48、5、3 都是竞争比上界口径，不是 latency speedup；更准确的说法是：SVF 用 volume-certificate proof 收紧了 prior best 48 的理论上界，在高并发 LLM serving 设定下给出更贴近 3 的保证。

实验效果也要分清场景。论文在单节点 8 张 NVIDIA A100 80GB、vLLM continuous batching、Meta-Llama-3.1-8B-Instruct 和 70B-Instruct 上评估，工作负载包括 LMSYS-Chat 和 LongBench，到达模式包括 burst 和 Poisson。Table 2 的 burst-arrival 结果显示，SVF 在四个模型/数据集组合中通常取得最低 non-oracle 平均 per-token latency，并且多数 P95 latency 优于 FCFS/SJF；LongBench 这类 memory-intensive workload 上，volume-first 的优势更直观。论文还用 Oracle-SJF 与 Oracle-SVF 对照说明：即使用 ground-truth output length，time-centric metric 在内存密集场景中仍可能错维，问题不只是“预测不准”。

给决策者的落点应该是“进入 PoC 池，不直接上线”。支持 PoC 的证据是：理论上，SVF 把竞争比上界从 prior 48 收紧到 alpha=1/2 时的 5，并在高并发下接近 3；工程上，论文给出了 vLLM 集成与 Llama-3.1 实验，且 predictor overhead 很低。限制条件同样必须放在 Summary Page：companion GitHub repo 公开了 `predictor/` 训练、预处理和评估代码，支持 BERT-base regression 与 BERT-tiny 1-bit classification，也有 `evaluate_predictor_accuracy.py` 计算 MAE、RMSE、within-token accuracy 和 95% accuracy threshold；但仓库树未发现 `.pth`、`.pt`、`.safetensors`、`.bin` 等训练好 checkpoint。因此复现前必须本地训练 predictor、用本地 prompt/output 分布测误差，并用本地 traffic replay 比较 FCFS、SJF、SVF、1-bit SVF 的平均延迟、P95 latency、吞吐和 starvation 风险。
参考图片：
- ![Figure 1: LLM inference process and volume calculation](assets/figure1-volume.webp)
  Figure 1 展示 prefill/decode 如何形成 KV cache 占用面积，支撑“调度指标从时间换成 volume”的机制判断。
- ![Table 1: competitive ratio by alpha](assets/table1-cr.webp)
  Table 1 展示 alpha=1/2 时 CR<=5，以及 alpha 趋近 0 时接近 3，支撑理论效果口径。
- ![Table 2: burst-arrival performance](assets/table2-burst.webp)
  Table 2 展示 burst-arrival 下 FCFS、SJF、1-bit SVF、SVF 在 Llama-3.1-8B/70B 和 LMSYS/LongBench 上的平均延迟、P95 延迟与吞吐对比。
- ![Table 3: predictor overhead](assets/table3-overhead.webp)
  Table 3 展示 regression predictor 与 classifier 的 overhead，支撑“开销低但精度未充分披露”的边界表达。
备注：
- 单页输出建议把视觉重心放在 Figure 1 的 volume 机制和 Table 1 的竞争比口径；Table 2/3 可作为右侧小型证据卡或 speaker note 补充。不要把 48/5/3 讲成实测加速倍数；不要把 GitHub repo 讲成已发布可直接下载的小预测器权重。

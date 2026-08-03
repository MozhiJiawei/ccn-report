# UltraEP 实时 MoE 专家负载均衡

截至 2026 年 6 月发布的 UltraEP 原始论文，该系统面向 Rack-Scale Node 上 106B–671B 参数 MoE 的训练与 serving prefill，在每个 microbatch、每层 gating 后以 GPU 配额规划、临时专家复制和流式中继传输实施精确负载均衡，作者实验报告其综合吞吐达到 force-balanced ideal 的 94.3%、较无均衡基线提升 1.49×，并在 2560 GPU 生产训练中验证超过 92% 的理想吞吐，因此其直接价值是把快速漂移的专家热点从周期性历史预测问题转化为约 0.3 ms 量级的现场调度问题。

## 来源与边界

- 原始来源：[UltraEP: Unleash MoE Training and Inference on Rack-Scale Nodes with Near-Optimal Load Balancing](https://arxiv.org/abs/2606.04101)
- `94.3%` 是训练和 serving prefill 跨模型平均后相对人为强制均衡上界的结果，不代表硬件峰值吞吐利用率。
- “约 0.3 ms”由 0.111 ms GPU quota solver 与高 fan-out 场景约 0.28 ms 的专家状态通信等组件级结果构成，不应表述为所有场景固定 300 微秒的完整端到端耗时。
- 结果依赖 RSN 级高速 scale-up 互联；论文未把 serving decode 作为主要优化对象。

## 交付件

- `ultraep_source_understanding_report.html`：dependency-free SingleFile HTML，可离线打开。

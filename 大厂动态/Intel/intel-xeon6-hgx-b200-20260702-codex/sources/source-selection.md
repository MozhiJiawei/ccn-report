# Source Selection

输入类型：web

## 原始来源清单

1. Intel Community Blog: Intel Xeon 6 Processors and Intel AMX Deliver More Concurrent Users with NVIDIA HGX B200 Systems — https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Intel-Xeon-6-Processors-and-Intel-AMX-Deliver-More-Concurrent/post/1752394
   - 选择理由：Intel 官方博客，直接提出 Xeon 6 + AMX 与 NVIDIA HGX B200 共同承载 vLLM 推理、提升并发用户数的架构线索。
2. Supermicro White Paper: Supermicro X14 HGX B200 GPU Servers With Intel Xeon 6 Processors — https://www.supermicro.com/white_paper/white_paper_X14-Intel-AMX-Concurrency-Performance.pdf
   - 选择理由：与题目同源的系统级测试白皮书，包含 SYS-822GS-NBRT、2x Xeon 6 6776P、8x NVIDIA HGX B200、并发提升口径和复现命令线索。

## 对照研究/同类方案清单

不做同类调研；后续 Source Understanding 和 PPT Content Brief 仅基于上述两个原始来源。

# Source Selection

输入类型：paper

## 原始来源清单

1. Nexus Sampling 原始论文
   - URL: https://arxiv.org/abs/2606.23961
   - 选择理由：主题中的 KV-cache 驱逐方法原始来源，论文实验明确对比 SnapKV、PyramidKV、H2O、MorphKV，并在附录对比 Ada-KV 变体。

## 对照研究/同类方案清单

1. MorphKV
   - URL: https://arxiv.org/abs/2503.00979
   - 对照角色：Nexus Sampling 在 prefill + decode 设置下的直接实验对比方法之一；比 H2O 更新，更适合对照“长生成流里连续驱逐误差会累积”的问题。
2. PyramidKV
   - URL: https://arxiv.org/abs/2406.02069
   - 对照角色：Nexus Sampling 在 prefill-only 设置下的直接实验对比方法之一；用于对照“层级预算/信息漏斗”与 Nexus 的“桥接 token + 概率保留”。

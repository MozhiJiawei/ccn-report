# DART-SD

## 一句话总结

DART-SD 是字节跳动与中国科学技术大学于 2026 年 8 月 19 日发布的 v1 论文提出的多轮工具调用 Agent 自蒸馏框架，通过交互状态图定位关键拓扑断点并仅监督恢复步骤，在论文默认 no-thinking 设置下将 Qwen3-8B 的 FTRL Solve-F1 从全轨迹 SFT 的 41.89 提升至 45.66，用于保留有效探索并提高工具任务完成质量。

## 任务信息

- 序号：88
- 任务编号：TASK-20260910151631-6fb9be62
- 热点编号：HS-001
- 周期：2026-W32
- 指定分类：由 AI 自动分类
- 实际归档分类：05-模型训练/微调、后训练与对齐
- 归类依据：任务分类为 null，自动判断：核心贡献是 ISTG 结构先验、CTB 恢复监督与渐进自蒸馏，直接改变模型参数及训练损失；按 02/05 边界，Agent 参数学习归模型训练；SD 指 Self-Distillation。与指定值无差异。
- 任务正文：DART-SD
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.18524)

## 交付件说明

- [DART-SD.html](./DART-SD.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [DART-SD.pptx](./DART-SD.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

唯一证据为预印本 v1，未独立复现；CTB 是经验成功可达域的首次离开，并非绝对错误证明；prefix mask 免直接监督不等于共享参数冻结；工具调用数仅统计成功轨迹，不等价端到端时延或总成本；默认 no-thinking 与补充 thinking 结果分别报告。

## 引用信息源说明

- [DART-SD 原始论文 v1](https://arxiv.org/abs/2608.18524v1)：支撑方法、训练设置、实验主表、消融与证据边界
- [DART-SD 论文 PDF v1](https://arxiv.org/pdf/2608.18524v1)：同一原始来源的全文、原图、定量表格和图注

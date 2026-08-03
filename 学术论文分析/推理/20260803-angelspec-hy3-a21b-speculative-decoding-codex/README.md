# AngelSpec Speculative Decoding

AngelSpec 是腾讯混元 AI Infra 团队面向真实异构大模型推理负载提出的统一投机解码训练与部署框架；在 2026-07-29 发布的论文 v2 中，DFly 在 Hy3-A21B、六类数学/代码/聊天基准及并发 4–64 条件下相对自回归解码取得 1.98–2.40× 端到端吞吐加速，并通过 D-cut 在 TP=8、8×NVIDIA H20 的线上流量实验中于并发 64 将吞吐提升至 981 tok/s，因此适合用于理解 drafter 架构、训练分布与在线验证预算如何共同决定无损推理加速。

## 归档信息

- 归档日期：2026-08-03
- 归档路径：`学术论文分析/推理/20260803-angelspec-hy3-a21b-speculative-decoding-codex/`
- 交付件：`source_understanding_review.html`
- 交付形态：SingleFile 离线 HTML

## 来源范围

- 论文：`AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding`
- arXiv：https://arxiv.org/abs/2607.25852
- 论文版本：v2，2026-07-29

本次归档只使用上述论文作为来源，不包含官方仓库、模型卡或同类方案对照来源。

## 生成与校验摘要

- 论文解析：通过；42 个图表全部索引，缺失 0、未索引 0、重复 0。
- HTML 渲染：通过；1920 px 桌面视口无横向溢出，破图 0。
- 独立视觉 QA：`PASS`；已完成 01–10 逐章 Primary Visual Checks。
- 人工审批：用户要求归档至 `ccn-report`，据此保存 Source Understanding approval baseline。

## 证据边界

- `2.40×` 是指定模型、基准与并发下的区间上界，不是跨硬件、跨模型的固定收益。
- DFly 相对自回归解码的 `1.98–2.40×` 与相对 DFlash 的 `10.5–11.8%` 使用不同基线，不能混写。
- D-cut 的 `981 tok/s` 来自 Hy3-295B-A21B、TP=8、8×NVIDIA H20、并发 64 的线上流量实验。
- 原文结论段出现 `A20B`，但摘要、主体与表格使用 `A21B`；报告按主体证据采用 `Hy3-A21B` 并标注一致性风险。

## 未归档内容

按照 `ccn-report` 规则，PDF、XML、图表目录、渲染截图、视觉 QA 记录与生成日志不进入正式归档；这些材料保留在工作区 `.tmp/ppt-deep-search/angelspec-hy3-a21b/` 下。

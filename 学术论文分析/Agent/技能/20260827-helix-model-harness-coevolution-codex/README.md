# HELIX：模型与 Harness 的证据驱动协同演化

## 一句话总结

HELIX 是 2026 年发布的模型—运行框架协同演化基础设施，它把来源可追溯的 harness 组件拆成 atoms、通过 ports 与 recipes 重组候选并在匹配任务上保留 sibling trajectories 和验证证据，在论文单轮代码修复实验中将最佳固定 harness 由 50/100 提高到 52/100、由 65 个候选的事后并集覆盖 79/100 并派生 438 条训练记录，用于让当前运行时改进可审计地交接给下一轮模型更新，而非把组合覆盖误当成单次 Pass@1。

## 任务信息

- 序号：29
- 任务编号：TASK-20260827174257-40f16019
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：HELIX让模型与运行框架协同演化，保留Agent改进来源与轨迹证据技术线索
- 任务来源：[https://arxiv.org/abs/2608.13951](https://arxiv.org/abs/2608.13951)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 HELIX 的 atoms/ports/recipes、证据平面、单轮结果、GitHub 实现与闭环边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [HELIX 论文](https://arxiv.org/abs/2608.13951)：用于支撑模型—harness 双时间尺度框架、候选组装、sibling trajectories、固定候选/组合覆盖/派生记录口径和单轮实验边界。
- [HELIX 官方代码仓库](https://github.com/HKUDS/HELIX)：用于核对 ports、atoms、recipe/lockfile、runtime trace、证据导出与当前 README 自述的工程实现状态。


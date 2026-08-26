# MindMemOS：可迁移、可演化的 Agent 长期记忆层

## SMART 技术一句话

截至 2026-08-03 的官方项目资料，MindMemOS 是面向 Agent 的可迁移记忆操作层，通过 MindVanilla、MindSchema、Dreaming 与 Feedback 组织实体—属性—时间记忆及演化轨迹，项目方在 LoCoMo 和 PersonaMem 上分别报告 94.03 与 70.63 的 Overall Accuracy，并报告 Dreaming 可归档 19.4%–23.5% 的活跃记忆，用于在多轮交互中维护可检索、可更新的长期状态。

## 归档信息

- 任务编号：TASK-20260803-01
- 热点编号：HS-20260803-01
- 周期：2026-W32
- 本地归档日期：2026-08-03
- 创建者：Codex

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile Source Understanding HTML。
- `one-page.html`：16:9、单页、dependency-free HTML 技术简报。
- `one-page-editable.pptx`：与单页 HTML 同版式的可编辑 PowerPoint。

## 来源与证据边界

- 任务指定微信页面因浏览器安全策略无法完成渲染抓取，本报告以 MindMemOS 官方 GitHub、官网和 PyPI 信息作为事实锚点，没有冒充微信原文。
- LoCoMo、PersonaMem 和 Dreaming 指标均为项目方官方 README 自报，不代表独立复现，也不应无条件外推到其他模型、数据或生产环境。
- EverMemOS 与 Mem0 仅用于机制和定位对照，不构成 MindMemOS 效果证明。

## QA 状态

- 来源包校验：通过。
- SingleFile 导出：成功。
- 独立视觉 QA：PASS；未发现裁切、重叠、横向溢出或破图。
- 单页 HTML / PPTX 双格式渲染：通过；PPTX 页面与文本边界检查 0 项异常。
- 单页独立视觉 QA：PASS；方案为明确视觉中心，关键数字已注明量纲、配置、基线缺失与证据边界。

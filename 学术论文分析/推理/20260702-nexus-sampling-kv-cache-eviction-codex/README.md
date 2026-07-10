# Nexus Sampling KV Cache Eviction Evidence Board

本目录归档 `Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets` 的单页技术证据板交付件。

## 交付件

- `nexus-one-page-evidence-board.pptx`：1:1 复刻 HTML 证据板的可编辑 PowerPoint 版本。
- `evidence-board.html`：单页 HTML 技术证据板。
- `assets/evidence-board-preview.webp`：HTML 版本渲染预览。
- `assets/pptx-render-preview.webp`：PPTX 版本渲染预览。
- `ppt_content_brief.md`：PPT 深度研究产出的单页内容 brief。
- `sources/source-selection.md`：本轮确认使用的论文来源与对照方案。
- `qa/html-visual-qa.md`：HTML 证据板视觉 QA 记录。
- `qa/pptx-overlap-check.json`：PPTX 可编辑版重叠 / 溢出检查结果。

## 核心判断

Shrivastava 课题组发布 Nexus Sampling 论文：方法用桥接重要性补足直接注意力，并用 weighted reservoir 替代每步 deterministic top-K 硬删，将 KV-cache eviction 从局部排序问题改写成跨时间的缓存生存概率问题。

关键效果口径采用论文 Table 3 的 agentic coding / SWE-bench sampled 证据：

- `20% KV density / 80% eviction`。
- `50` 个 SWE-bench sampled tasks，不是完整 SWE-Bench。
- Prefill-only true eviction 下，PyramidKV 从 `7/50` 掉到 `1/50`，Nexus 从 `9/50` 到 `8/50`。
- Prefill+Decode true eviction 这个 hardest setting 下，MorphKV 为 `9/50`，Nexus 为 `8/50`，H2O 为 `4/50`。

## 边界

- 这份证据支持“值得复现”，不支持“已证明生产收益”。
- SWE-Bench 结果来自 `50` 个 sampled tasks，任务选择需要本地复核。
- Dense reference 只有 `12/50`，说明任务、模型或环境本身通过率低。
- Nexus 在 hardest setting 下低于 MorphKV 1 题，不能包装成全面领先。
- Reservoir 随机性需要固定 seed、cache 状态记录和回放调试。

## 素材来源

- Nexus Sampling arXiv: `2606.23961`
- MorphKV arXiv: `2503.00979`
- PyramidKV arXiv: `2406.02069`
- 本目录 `assets/` 中的 method figure、Table 3 与预览图来自论文解析和最终证据板渲染。

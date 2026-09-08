# SVF LLM Scheduling Evidence Board

本目录归档 `Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice` 的单页技术证据板交付件。

## 交付件

- `one-page.html`：自包含的一页同版式 HTML。
- `one-page-editable.pptx`：以可编辑文字、形状和论文表格原图组成的一页 PowerPoint。
- `svf-one-page-evidence-board.pptx`：可编辑 PowerPoint 版本。
- `evidence-board.html`：单页 HTML 技术证据板。
- `assets/evidence-board-preview.webp`：HTML 版本渲染预览。
- `assets/pptx-render-preview.webp`：PPTX 版本渲染预览。
- `ppt_content_brief.md`：PPT 深度研究产出的单页内容 brief。
- `research_audit.md`：证据审计与边界说明。
- `qa/html-visual-qa.md`：HTML 证据板视觉 QA 记录。

## 核心判断

人大高瓴等发布 SVF 论文：在 vLLM 与 Llama-3.1 实验中，SVF 用 KV cache volume 降低延迟；`alpha=1/2` 时竞争比为 5，高并发接近 3。

关键边界：

- `48 / 5 / 3` 是 worst-case competitive ratio bound，不是实测 speedup。
- predictor 训练、预处理、评估代码开源，但未发现论文特定 checkpoint；PoC 前需要自训并本地评估。

## 素材来源

- arXiv: `2606.22327`
- Companion repo: `https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling`
- 本目录 `assets/` 中的 Figure/Table 来自论文解析与最终证据板渲染。

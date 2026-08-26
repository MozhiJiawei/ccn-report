# ICML 2026 Poster收录了Dustin论文

本目录归档 Dustin 长上下文投机解码稀疏验证研究的人工认可交付件。核心结论页围绕 Qwen2.5-72B、32k 上下文、batch16、512 token 验证预算下的 27.85x 自注意力加速和 9.17x 解码阶段端到端加速展开。

## 交付件

- Issue #25 一句话单页（自包含 HTML）：[one-page.html](one-page.html)
- Issue #25 一句话单页（可编辑 PPTX）：[one-page-editable.pptx](one-page-editable.pptx)
- HTML 视觉证据板：[report/index.html](report/index.html)
- HTML 静态预览：[report/index-preview.webp](report/index-preview.webp)
- 可编辑 PPT 复刻版：[ppt/dustin-one-page-evidence-board.pptx](ppt/dustin-one-page-evidence-board.pptx)
- PPT 渲染预览：[ppt/slide-1-preview.webp](ppt/slide-1-preview.webp)
- 内容 Brief：[brief/ppt_content_brief.md](brief/ppt_content_brief.md)
- HITL 确认记录：[brief/ppt_brief_hitl.json](brief/ppt_brief_hitl.json)

## QA 记录

- HTML 视觉 QA：[qa/html-visual-qa.md](qa/html-visual-qa.md)
- PPT 1:1 可编辑复刻 QA：[qa/ppt-editable-replication-qa.txt](qa/ppt-editable-replication-qa.txt)

## 来源

- Dustin arXiv PDF: https://arxiv.org/pdf/2606.24957
- SpecAttn: Speculating Sparse Attention: https://arxiv.org/abs/2510.27641
- Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference: https://arxiv.org/abs/2406.10774

## 归档说明

HTML 报告的 CSS、JS 和图片资产已复制到 `report/assets/`，图片按仓库规范转换为 WebP。目录不包含中间失败稿、构建缓存、调试脚本或运行时依赖目录。

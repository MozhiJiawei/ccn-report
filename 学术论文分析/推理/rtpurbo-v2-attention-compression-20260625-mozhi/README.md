# RTPurboV2 实现稀疏注意力迁移

本目录归档 RTPurboV2 / RTPurbo 注意力压缩论文分析交付件。

## 入口

- `review/source_understanding_review.html`：Source Understanding HTML review deck。
- `review/source-understanding-images/`：Source Understanding 逐页导出截图。
- `review/assets/`：review deck 与最终 slide 使用的论文图表证据。
- `review/visual-qa.md`：Source Understanding 渲染校验与独立视觉 QA 记录。
- `final-slide/rtpurbo-summary-slide.html`：一页高密度 HTML PPT。
- `final-slide/rtpurbo-summary-slide.png`：一页 HTML PPT 的渲染预览。
- `final-slide/rtpurbo-summary-slide.pptx`：可编辑 PowerPoint 版本。
- `final-slide/rtpurbo-summary-slide.pptx.inspect.ndjson`：PPTX 检查快照。
- `baselines/ppt_content_brief.md`：生成一页 PPT 的内容 brief。
- `baselines/ppt_brief_hitl.json`：PPT brief HITL 审批记录。
- `baselines/015-source-understanding.md`：已批准的 source understanding baseline。
- `sources/source-selection.md`：来源选择与研究对象口径记录。
- `html-ppt-assets/`：归档内自带的 HTML PPT 运行依赖。

## 主要结论

RTPurboV2 的核心不是单点加速数字，而是把既有 Full Attention 模型通过少量后训练迁移到可训练、可部署的稀疏注意力路径。决策时应分开核验精度、模型范围、prefill / decode / 端到端收益口径。

## 校验

归档后重新运行：

```powershell
python ../skills/ppt-deep-search/scripts/validate_source_understanding_html.py ccn-report/学术论文分析/推理/rtpurbo-v2-attention-compression-20260625-mozhi/review/source_understanding_review.html all ccn-report/学术论文分析/推理/rtpurbo-v2-attention-compression-20260625-mozhi/review/source-understanding-images
```

```powershell
python ../skills/ppt-deep-search/scripts/validate_source_understanding_html.py ccn-report/学术论文分析/推理/rtpurbo-v2-attention-compression-20260625-mozhi/final-slide/rtpurbo-summary-slide.html all ccn-report/学术论文分析/推理/rtpurbo-v2-attention-compression-20260625-mozhi/final-slide/qa-images
```

结果：两个 HTML 均通过渲染校验；最终 PPTX 由 `@oai/artifact-tool` 生成，子 agent 已检查 1 页、无明显裁切/遮挡，程序化边界检查 `outOfBounds: []`。

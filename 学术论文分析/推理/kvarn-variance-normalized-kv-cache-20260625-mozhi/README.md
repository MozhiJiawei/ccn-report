# KVarN 论文 Source Understanding

本目录归档 KVarN 论文的 Source Understanding HTML PPT 交付件。

## 入口

- `review/source_understanding_review.html`：Source Understanding HTML review deck。
- `review/source-understanding-images/`：Source Understanding 逐页导出截图。
- `review/visual-qa.md`：渲染校验与独立视觉 QA 记录。
- `sources/source-selection.md`：来源选择与输入材料记录。
- `sources/paper/source-summary.md`：论文核心 claim、证据索引和性能边界摘要。
- `sources/paper/images/`：deck 使用的论文图表证据。
- `ppt_content_brief.md`：单页 PPT Content Brief，供后续 PPT 生成使用。
- `baselines/ppt_brief_hitl.json`：Content Brief HITL 审批记录。
- `final-slide/kvarn-summary-slide.html`：基于 Content Brief 生成的一页 16:9 HTML PPT。
- `final-slide/kvarn-summary-slide.webp`：一页 HTML PPT 的渲染预览。
- `final-slide/kvarn-summary-slide.pptx`：可编辑 PowerPoint 版本。
- `final-slide/kvarn-summary-slide.pptx.preview.webp`：PPTX 重新导入后的渲染预览。
- `final-slide/kvarn-summary-slide.pptx.inspect.ndjson`：PPTX 结构检查快照。
- `html-ppt-assets/`：归档内自带的 HTML PPT 运行依赖。

## 主要结论

KVarN 的核心不是证明整网 TPOT / TTFT 变快，而是指出长链 decoding 下 KV-cache 量化误差会累积，主要来自 token magnitude / scale error。方法通过 Hadamard rotation 与双轴 variance normalization 在 2-bit KV-cache 下保住精度；性能证据仅支持 normalization / dequant 局部 overhead 很低，论文没有报告整网 serving 的 TPOT、TTFT、tokens/s 或 end-to-end latency 收益。

## 校验

归档后已运行：

```powershell
python skills/ppt-deep-search/scripts/validate_source_understanding_html.py ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/review/source_understanding_review.html all ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/review/source-understanding-images
```

结果：PASS。检测到 13 页，左右键导航正常，截图导出成功，图片缩放硬门禁通过；独立视觉 QA Verdict 为 PASS。

Content Brief 校验：

```powershell
python skills/ppt-deep-search/scripts/validate_ppt_content_brief.py ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/ppt_content_brief.md --min-page-content-chars 900 --min-summary-content-chars 1200 --allow-absolute-paths --expected-pages 1
```

结果：PASS。单页 Summary Page 内容密度达标，参考图片绝对路径位于 `参考图片` 字段内。

一页 HTML PPT 校验：

```powershell
chrome --headless=new --disable-gpu --hide-scrollbars --window-size=1600,900 --force-device-scale-factor=1 --screenshot=ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/final-slide/kvarn-summary-slide.webp ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/final-slide/kvarn-summary-slide.html
```

结果：PASS。截图为 1600x900，比例 16:9；HTML 中 5 个图片引用均指向归档内存在的证据素材。

PPTX 转换校验：

结果：PASS。最终 PPTX 已重新导入并渲染为 `final-slide/kvarn-summary-slide.pptx.preview.webp`；页面为 1 页，文本、形状和图片均为可编辑对象，未使用整页截图贴片。构建缓存目录已清理，正式归档仅保留 PPTX、预览图和 inspect 快照。

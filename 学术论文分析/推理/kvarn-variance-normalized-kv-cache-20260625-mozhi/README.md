# KVarN 论文 Source Understanding

本目录归档 KVarN 论文的 Source Understanding HTML PPT 交付件。

## 入口

- `review/source_understanding_review.html`：Source Understanding HTML review deck。
- `review/source-understanding-images/`：Source Understanding 逐页导出截图。
- `review/visual-qa.md`：渲染校验与独立视觉 QA 记录。
- `sources/source-selection.md`：来源选择与输入材料记录。
- `sources/paper/source-summary.md`：论文核心 claim、证据索引和性能边界摘要。
- `sources/paper/images/`：deck 使用的论文图表证据。
- `html-ppt-assets/`：归档内自带的 HTML PPT 运行依赖。

## 主要结论

KVarN 的核心不是证明整网 TPOT / TTFT 变快，而是指出长链 decoding 下 KV-cache 量化误差会累积，主要来自 token magnitude / scale error。方法通过 Hadamard rotation 与双轴 variance normalization 在 2-bit KV-cache 下保住精度；性能证据仅支持 normalization / dequant 局部 overhead 很低，论文没有报告整网 serving 的 TPOT、TTFT、tokens/s 或 end-to-end latency 收益。

## 校验

归档后已运行：

```powershell
python skills/ppt-deep-search/scripts/validate_source_understanding_html.py ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/review/source_understanding_review.html all ccn-report/学术论文分析/推理/kvarn-variance-normalized-kv-cache-20260625-mozhi/review/source-understanding-images
```

结果：PASS。检测到 13 页，左右键导航正常，截图导出成功，图片缩放硬门禁通过；独立视觉 QA Verdict 为 PASS。

# 增量 BPE 分词算法实现 O(n log²t) 复杂度，推理吞吐提升 3 倍

本目录归档 PPT Deep Search / Source Understanding 阶段产物。

## 入口

- `review/source_understanding_review.html`：可直接打开的 HTML review deck。
- `review/source-understanding-images/`：HTML deck 的逐页导出截图。
- `review/assets/`：deck 使用的论文图表证据。
- `review/visual-qa.md`：渲染校验与独立视觉 QA 记录。
- `sources/source-selection.md`：来源选择记录。
- `sources/source-map.md`：核心 claim 与证据映射。
- `html-ppt-assets/`：归档内自带的 HTML PPT 运行依赖。

## 校验

归档后已重新运行：

```powershell
python skills/ppt-deep-search/scripts/validate_source_understanding_html.py ccn-report/学术论文分析/推理/20260626-incremental-bpe-tokenization-throughput-mozhi/review/source_understanding_review.html all ccn-report/学术论文分析/推理/20260626-incremental-bpe-tokenization-throughput-mozhi/review/source-understanding-images
```

结果：PASS。检测到 13 页，左右键导航正常，截图导出成功，图片缩放硬门禁通过。

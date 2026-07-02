# SGLang GB300 DeepSeek-V4 serving 优化复盘归档

本目录归档《SGLang 团队发布 GB300 优化复盘：DeepSeek-V4 在同交互口径下吞吐提升约 5 倍》的研究过程和正式交付件。

## 交付件

| 类型 | 文件 |
| --- | --- |
| 一页 HTML 技术证据板 | `html/index.html` |
| 可编辑 PowerPoint | `pptx/sglang-gb300-evidence-board-editable.pptx` |
| HTML 预览图 | `previews/html-evidence-board/` |
| PPTX 预览图 | `previews/pptx-editable/` |
| Source Understanding 审阅稿 | `review/source_understanding_review.html` |
| Source Understanding 预览图 | `previews/source-understanding/` |
| PPT Content Brief | `brief/ppt_content_brief.md` |
| QA 记录 | `qa/` |
| 信源包 | `sources/` |

## 研究范围

本轮按用户要求只保留一个原始信源：

- PyTorch Blog / SGLang Team：`Serving DeepSeek-V4 on GB300 with SGLang: 5x Higher Throughput at the Same Interactivity Since Day-0`

没有归档早期候选中的对照研究或同类方案。

## 核心结论

SGLang 团队的复盘显示，在 GB300 disaggregated 8K/1K 口径下，DeepSeek-V4 Pro 的 June MTP 曲线在约 `50 tok/s/user` 处达到 Day-0 no-MTP 的约 `5x` 吞吐。原文给出的 headline comparison 是：

- Day-0 no-MTP：约 `2,200 tok/s/GPU`
- June MTP：约 `11,200 tok/s/GPU`
- 对照口径：DeepSeek-V4 Pro、GB300、FP4、ISL=8192、OSL=1024、dynamo-sglang、约 `50 tok/s/user`

这条线索的价值不在于把 `5x` 外推为所有模型和硬件的通用收益，而在于把 serving frontier 的提升拆成可复用的工程排查链：MHC 融合、KV Compression V2、W4A4 MoE、SWA 预算、CUDA graph、MTP / disaggregated runtime hardening。

## 证据边界

- `5x` 只适用于原文限定的公开 GB300 lane、模型、精度、输入输出长度、serving framework 和用户交互速度取点。
- 不能表述为 SGLang 在所有 GB300 推理任务上提升 5 倍。
- 不能表述为单个 kernel、单个 PR 或硬件本身带来完整 5 倍收益。
- 原图来自 source package 中的 GB300 performance chart；HTML 和 PPTX 均围绕该原图组织指标和机制解释。

## 处理过程

1. 使用 `web-article-capture` 抓取 PyTorch Blog 正文和正文图片，输出 `sources/web/pytorch-sglang-deepseek-v4-gb300-5x/`。
2. 使用 `ppt-deep-search` 生成并审批 Source Understanding HTML，输出 `review/source_understanding_review.html`。
3. 基于用户确认的一页 Summary Page 生成 `brief/ppt_content_brief.md`，并通过 brief validator。
4. 使用 `hw-ppt-gen-html` 将 brief 转成一页高密度 HTML 技术证据板，输出 `html/index.html`。
5. 使用 Codex Presentations skill 将 HTML 证据板转成可编辑 PPTX，输出 `pptx/sglang-gb300-evidence-board-editable.pptx`。

## QA 状态

- Source Understanding HTML：独立视觉 QA `PASS`。
- 一页 HTML 技术证据板：独立视觉 QA `PASS`。
- 可编辑 PPTX：PPTX 导出和渲染通过，`slides_test.py` 返回 `Test passed. No overflow detected.`。

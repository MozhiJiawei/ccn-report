# Source Understanding Visual QA

## Hard Render Gate

Command:

```text
python skills/ppt-deep-search/scripts/validate_source_understanding_html.py .tmp/ppt-deep-search/incremental-bpe-tokenization-throughput-redo/review/source_understanding_review.html all .tmp/ppt-deep-search/incremental-bpe-tokenization-throughput-redo/review/source-understanding-images
```

Final result: PASS

- Detected 13 `section.slide` nodes.
- Keyboard navigation passed: ArrowRight advances and ArrowLeft returns.
- Exported 13 PNG screenshots to `review/source-understanding-images/`.
- Image-scale hard gate passed after increasing Slide 5 source Figure 2 display width.

## Independent Checker Round 1

Verdict: FAIL

Scores:

- 读者可理解性: 3/4
- 技术机制解释: 3/4
- 证据与口径: 3/4
- 主视觉材料可读性: 2/4
- 版面安全: 4/4

Key original findings:

- [P0] Slide 11 flame graph labels were too small to read; checker requested local crop, zoom, or reconstructed bars for regex/BPE/normalization shares.
- [P1] Slide 5 Figure 2 was too dense for beginners; checker requested a highlighted path or local redraw explaining monotonic path.
- [P1] Deck-level numbered references lacked a complete mapping; checker requested a reference table.

Fixes made:

- Slide 5 now includes a reconstructed monotonic-path diagram and keeps original Figure 2 as source evidence.
- Slide 11 now uses readable profile bar charts for Qwen-3/tokenizers and tiktoken O200K.
- Slide 13 adds the numbered reference mapping to paper sections, figures, tables, and local assets.

## Independent Checker Round 2

Verdict: PASS

Scores:

- 读者可理解性: 4/4
- 技术机制解释: 4/4
- 证据与口径: 4/4
- 主视觉材料可读性: 4/4
- 版面安全: 4/4

Key original PASS rationale:

- 技术小白能看懂主线：先解释 tokenizer / BPE / 增量 BPE，再讲标准 BPE 的流式难点、monotonic path、算法步骤、复杂度、收益和边界。
- 关键术语基本都有“人话解释”或图解承接；少量专家词如 Aho-Corasick、centroid 不是主阅读障碍。
- Slide 5 已用重构图解释 monotonic path，原 Figure 2 可读，且页面显示约 790px / 原图 969px，满足不低于 80% 缩放要求。
- Slide 11 已用可读条形图替代 flame graph，并保留 Qwen-3 BPE merge 13.11%、tiktoken O200K regex 80.25%、BPE merge 6.45% 等关键口径。
- Slide 13 已补齐编号引用映射，能追踪到论文段落、图表和本地素材。
- 全 deck 标题、正文、图表、页脚无明显裁切、遮挡、重叠或横向溢出。

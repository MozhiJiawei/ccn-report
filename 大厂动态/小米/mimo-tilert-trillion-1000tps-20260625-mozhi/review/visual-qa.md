# Source Understanding Visual QA

HTML: `.tmp/ppt-deep-search/mimo-tilert-trillion-1000tps/review/source_understanding_review.html`

Rendered PNG directory: `.tmp/ppt-deep-search/mimo-tilert-trillion-1000tps/review/source-understanding-images/`

Validator command:

```powershell
python skills/ppt-deep-search/scripts/validate_source_understanding_html.py .tmp/ppt-deep-search/mimo-tilert-trillion-1000tps/review/source_understanding_review.html all .tmp/ppt-deep-search/mimo-tilert-trillion-1000tps/review/source-understanding-images
```

Validator result: PASS.

Independent checker: Halley (`019efde8-b24c-7e72-9996-c96b6378143c`)

## Checker Verdict

Verdict: PASS

已实际查看导出目录中的 8 张 PNG，未发现白屏、破图、alt 文本、空占位、横向溢出、标题裁切、固定元素残影或正文遮挡问题。

关键检查结果：
- 8 页章节标识和主标题均在首屏完整显示，不依赖滚动。
- 信息密度总体合格：覆盖来源映射、机制链条、FP4、DFlash、TileRT、模型卡与后续 brief 边界。
- 视觉锚点有效：第 4 页 benchmark 图、第 6 页 TileRT 原图渲染正常且可读；第 2、5、7、8 页表格/卡片承担证据锚点，未缩成小框。
- 版面安全：表格、卡片、图像边界清晰，低对比问题不明显；页脚/进度条未覆盖正文。
- 证据边界表达明确：第 2、7、8 页对未公开 GPU 型号、batch、并发、runtime 复现实验等边界有清楚标注。

## Checker Verdict After DFlash Expansion

HTML updated after user feedback to add DFlash paper/project evidence and expand DFlash explanation to slides 5-8.

Validator result after update: PASS.

Independent checker: Aquinas (`019efeab-666d-7f42-b52a-a4f2296e4b74`)

Verdict: PASS

已实际查看 11 张导出 PNG。全 deck 未见白屏、破图、alt 文本占位、横向溢出、标题裁切或明显遮挡；每页章节标识和主标题都在首屏完整可见。

新增 DFlash 第 5-8 页检查结果：
- Slide 5：DFlash 原理图真实渲染，target hidden states / fused target context feature / KV cache injection / draft layer / block diffusion draft 的关系能看出来；右侧解释把“先由 target model 产生 hidden features，再注入 drafter KV cache”讲清楚。
- Slide 6：训练 attention / anchor + mask block 图真实且可读，颜色图例清楚，能理解 target context feature、mask token、clean token、invisible token 的约束关系。
- Slide 7：两张论文证据图均渲染，左侧 speedup 图和右侧 latency 图可读；页面明确区分“论文 6x speedup”与 MiMo 1000+ TPS 不能直接等同。
- Slide 8：接受长度表格清晰，coding/agent 场景高收益的结论突出，verification acceptance 的“连续前缀长度”含义表达明确。

快速全 deck：
- Slides 1-4、9-11 布局稳定，图表/表格/卡片文字可读。
- Slide 4、7、9 的原图均非空占位，证据图没有缩成不可辨认的小框。
- 未发现低对比导致不可读的问题；底部页进度条不遮挡内容。

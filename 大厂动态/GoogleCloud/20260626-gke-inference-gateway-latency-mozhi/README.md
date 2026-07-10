# GKE Inference Gateway Latency Source Understanding

归档日期：2026-06-25

## 交付件

- `review/source_understanding_review.html`：Source Understanding HTML deck，9 页，已通过硬校验和独立视觉 QA。
- `review/source-understanding-images/`：HTML deck 导出 PNG 与 render manifest。
- `review/source-map.md`：页面到来源的证据映射。
- `review/visual-qa.md`：独立视觉 QA 记录。
- `sources/`：已确认并抓取的网页 source packages。
- `assets/html-ppt/`：HTML deck 运行所需的最小 html-ppt 静态资源。

## 核心结论

GKE Inference Gateway 的“92% AI response latency”应收窄理解为：在 Llama 3.1 8B Instruct shared-prefix workload、8x NVIDIA A100 40GB、对比 conventional round-robin HTTP load balancing 的 benchmark 中，mean TTFT 下降 92.8%。机制核心是通过 llm-d Endpoint Picker 做 prefix-cache/load/LoRA aware routing，提高 shared prefix 的 KV cache 复用概率。

## 备注

Principled Technologies PDF 为 Google 原文链接证据，但本归档仅包含已抓取网页来源包；如后续进入正式 PPT Content Brief 或技术选型报告，应补抓并审计该 PDF 全文。

# SwiftCache Source Understanding

本目录最初归档 Issue #18「推理周报」主题「南科大与阿里提出 SwiftCache」的 Source Understanding 报告，并在 Issue #25 中补充单页 HTML 与可编辑 PowerPoint 交付件。

截至论文 arXiv:2606.16135（2026 年 6 月），SwiftCache 面向单机多 GPU 异构 LLM 服务，通过 NVLink/NVSwitch 在缓存高需求 Master 与低需求 Worker 间共享 KV Cache 并结合 Layer Stream Cache，在 ShareGPT/L-Eval 多轮负载上相对 SGLang HiCache 将 P99 TTFT 最多降低 69%，用于缓解长对话历史缓存的 PCIe/CPU/SSD 搬运瓶颈。

## 内容

- `source_understanding_review.html`：SingleFile 单文件 HTML，可离线打开。
- `one-page.html`：16:9、依赖自包含的单页技术简报。
- `one-page-editable.pptx`：与单页 HTML 同版式的可编辑 PowerPoint。

## 来源

- SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing
- arXiv PDF: https://arxiv.org/pdf/2606.16135

## 说明

- 本报告来自 PPT深度研究前置阶段，只用于确认论文理解和证据边界。
- 本目录不归档 PDF、解析 XML、图片包、QA 记录或临时导出日志。

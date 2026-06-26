# Source Selection: KVarN Source Understanding

- 输入类型：paper
- 主题：KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks

## 原始来源清单

1. `D:/Agent Repo/Mozhi-s-AgentWorkspace/.tmp/pdf_xml/kvarn-2606.03458/final/kvarn-2606.03458.xml`
   - 角色：GROBID + Docling 解析后的结构化论文正文、章节、图表 caption、参考文献与图片索引。
2. `D:/Agent Repo/Mozhi-s-AgentWorkspace/.tmp/pdf_xml/kvarn-2606.03458/final/images/`
   - 角色：Docling 导出的论文图、表图片，作为 Source Understanding HTML 的主证据材料。
3. `D:/Agent Repo/Mozhi-s-AgentWorkspace/.tmp/kvarn-paper/kvarn-2606.03458.pdf`
   - 角色：原始 PDF，用于必要时回查版面与图表。

## 对照研究/同类方案清单

1. KIVI
   - 对照角色：基础 KV-cache 量化路线，K 按 channel、V 按 token，论文用作核心 baseline。
2. QuaRot / Hadamard-only route
   - 对照角色：说明单独做 incoherence processing 能改善 channel outlier，但不足以解决 token-scale error。
3. KVQuant / PolarQuant / TurboQuant / Kitty
   - 对照角色：表 1/2/3 中的同类 KV-cache quantization baseline，用于比较精度、bits/element、是否 uniform precision。

## 本轮产物约束

- 论文输入场景按 `source-understanding-html-ppt.md` 跳过 HITL 来源确认。
- 任务 workspace-root 设为 `.tmp/source-understanding-kvarn-refresh-v2/`。
- HTML 输出：`review/source_understanding_review.html`。
- 截图输出：`review/source-understanding-images/`。

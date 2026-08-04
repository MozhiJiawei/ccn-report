# 从 Vector RAG 的一次失败，到 Agent Memory 的新栈

> SMART 技术总结：截至 2026-08-04，《从 Vector RAG 的一次失败，到 Agent Memory 的新栈》所述对象被本报告界定为面向“Agent记忆”的工程方法、系统机制与技术路线，并以 报告内固定的公开来源、实现证据与版本边界覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持Agent记忆 技术选型；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`context-graph-memory-report-20260626/main/context-graph-main-report.html`
- 来源 SHA256：`eda7cd73d9f1446d455b58f8ef06d5cc36e09c22b0ec333e59b7a5e048a0e3fa`
- 选择与证据边界：取 1.5 MiB 主报告；仅在主报告运行时依赖子报告链接时递归导出必要子页。

## 交付件

- [`main/context-graph-main-report.html`](main/context-graph-main-report.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。
- [`subreports/01-blog-context-graph-benchmark/blog-context-graph-benchmark-report.html`](subreports/01-blog-context-graph-benchmark/blog-context-graph-benchmark-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`subreports/02-2026-agentic-graph-memory-sota/agentic-graph-memory-sota-report.html`](subreports/02-2026-agentic-graph-memory-sota/agentic-graph-memory-sota-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`subreports/03-2026-graphrag-beyond-vector-rag/graphrag-beyond-vector-rag-report.html`](subreports/03-2026-graphrag-beyond-vector-rag/graphrag-beyond-vector-rag-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`subreports/04-temporal-context-graph-production/temporal-context-graph-production-report.html`](subreports/04-temporal-context-graph-production/temporal-context-graph-production-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`subreports/05-agent-memory-platforms/agent-memory-platforms-report.html`](subreports/05-agent-memory-platforms/agent-memory-platforms-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`subreports/06-multi-agent-shared-memory-governance/multi-agent-shared-memory-governance-report.html`](subreports/06-multi-agent-shared-memory-governance/multi-agent-shared-memory-governance-report.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。

## 来源锚点

- https://arxiv.org/html/2601.03236v2/x2.png
- https://arxiv.org/html/2507.21892v2/x3.png
- https://arxiv.org/html/2606.24535v1/figure_1_system_overview.png
- https://github.com/Emmimal/context-graph-benchmark
- https://arxiv.org/abs/2606.06036

## 归档验证

- 共归档 7 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

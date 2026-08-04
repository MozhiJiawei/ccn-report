# Agent 长期记忆：基准、架构与生产选型

> SMART 技术总结：截至 2026-08-04，《Agent 长期记忆：基准、架构与生产选型》所述对象被本报告界定为围绕“Mem0”的开源 Agent 系统或工程实现，并以 Mem0 的归档时公开代码、文档与报告内引用覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持Mem0 评估；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`mem0-memory-benchmark-report-20260724/mem0-memory-benchmark-report-standalone.html`
- 来源 SHA256：`4bc393413fba6b0bae2680862ccbcc8c7e96ba96024d7faf537e562e95d484ab`
- 选择与证据边界：取 standalone。

## 交付件

- [`mem0-memory-benchmark.html`](mem0-memory-benchmark.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。

## 来源锚点

- https://github.com/mem0ai/memory-benchmarks
- https://arxiv.org/abs/2504.19413
- https://help.openai.com/en/articles/8590148-memory-faq
- https://arxiv.org/abs/2310.08560
- https://arxiv.org/abs/2402.17753

## 归档验证

- 共归档 1 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

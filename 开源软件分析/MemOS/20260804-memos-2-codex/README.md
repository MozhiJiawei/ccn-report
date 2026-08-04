# MemOS 2.0：从记忆操作系统到自进化 Agent Memory

> SMART 技术总结：截至 2026-08-04，《MemOS 2.0：从记忆操作系统到自进化 Agent Memory》所述对象被本报告界定为围绕“MemOS”的开源 Agent 系统或工程实现，并以 MemOS 的归档时公开代码、文档与报告内引用覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持MemOS 评估；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`memos-2.0-tech-report-20260722/memos-2.0-technical-analysis.html`
- 来源 SHA256：`989e68c1f9ebc985697fa670ba6f41d40cf57b981af6a4af5dbe4595894aa2cf`
- 选择与证据边界：对应 `MemTensor/MemOS`，不是 `MemOS-main` 源码页。

## 交付件

- [`memos-2.html`](memos-2.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。

## 来源锚点

- https://github.com/MemTensor/MemOS/blob/main/apps/memos-local-plugin/core/session/episode-manager.ts
- https://github.com/MemTensor/MemOS/blob/main/apps/memos-local-plugin/core/capture/README.md
- https://github.com/MemTensor/MemOS/blob/main/apps/memos-local-plugin/core/capture/step-extractor.ts
- https://github.com/MemTensor/MemOS/blob/main/apps/memos-local-plugin/core/capture/alpha-scorer.ts
- https://github.com/MemTensor/MemOS/blob/main/apps/memos-local-plugin/core/reward/README.md

## 归档验证

- 共归档 1 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

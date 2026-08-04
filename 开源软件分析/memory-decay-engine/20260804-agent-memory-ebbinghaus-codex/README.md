# 从上下文窗口到使用强化衰减｜Agent Memory 技术报告

> SMART 技术总结：截至 2026-08-04，《从上下文窗口到使用强化衰减｜Agent Memory 技术报告》所述对象被本报告界定为围绕“memory-decay-engine”的开源 Agent 系统或工程实现，并以 memory-decay-engine 的归档时公开代码、文档与报告内引用覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持memory-decay-engine 评估；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`agent-memory-report/agent-memory-ebbinghaus-report.html`
- 来源 SHA256：`618b9877de5fe6cc6fc8218a92ee43173a86fb77eb15c95a66400d6fcd4dec9d`
- 选择与证据边界：报告明确对应 `Emmimal/memory-decay-engine`。

## 交付件

- [`agent-memory-ebbinghaus.html`](agent-memory-ebbinghaus.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。

## 来源锚点

- https://github.com/Emmimal/memory-decay-engine
- https://arxiv.org/abs/2402.17753
- https://towardsdatascience.com/context-windows-forget-what-matters-i-used-a-140-year-old-psychology-paper-to-fix-ai-memory/
- https://psychclassics.yorku.ca/Ebbinghaus/index.htm
- https://doi.org/10.1037/0033-2909.132.3.354

## 归档验证

- 共归档 1 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

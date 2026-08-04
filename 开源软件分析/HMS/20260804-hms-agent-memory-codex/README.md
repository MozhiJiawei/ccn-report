# HMS Agent 记忆系统技术洞察

> SMART 技术总结：截至 2026-08-04，《HMS Agent 记忆系统技术洞察》所述对象被本报告界定为围绕“HMS”的开源 Agent 系统或工程实现，并以 HMS 的归档时公开代码、文档与报告内引用覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持HMS 评估；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`hms-memory-report-20260724/humanize-run/hms-report.html`
- 来源 SHA256：`7ab74a916dbd36621d6def408aeec885ccd85c451ffbda553d5efb4286f19809`
- 选择与证据边界：对应 `Shadow-Weave/HMS`；虽然位于 humanize-run，但这是该路径唯一正式 HTML。

## 交付件

- [`hms-agent-memory.html`](hms-agent-memory.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。

## 来源锚点

- https://github.com/Shadow-Weave/HMS/blob/72ba4207ae7f3e8f0dd9a14914984e783f428989/core/dataplane/hms_api/engine/retain/fact_extraction.py
- https://github.com/Shadow-Weave/HMS/blob/72ba4207ae7f3e8f0dd9a14914984e783f428989/core/dataplane/hms_api/engine/retain/orchestrator.py
- https://github.com/Shadow-Weave/HMS/blob/72ba4207ae7f3e8f0dd9a14914984e783f428989/core/dataplane/hms_api/engine/search/implementations.py
- https://github.com/Shadow-Weave/HMS/blob/72ba4207ae7f3e8f0dd9a14914984e783f428989/core/dataplane/hms_api/engine/search/link_expansion_retrieval.py
- https://github.com/Shadow-Weave/HMS/blob/72ba4207ae7f3e8f0dd9a14914984e783f428989/core/dataplane/hms_api/engine/search/fusion.py

## 归档验证

- 共归档 1 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

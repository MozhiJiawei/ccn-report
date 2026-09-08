# Independent HTML Report A/B

> SMART 技术总结：截至 2026-08-04，《Independent HTML Report A/B》所述对象被本报告界定为围绕“Agent工作流”的可复现实验设计与方案对比，并以 归档实验的对照条件、生成结果与报告内评价证据覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持Agent工作流 流程选择；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`anthropic_agent_workspace_ab_experiment_20260625/comparison/independent_html_side_by_side.html`
- 来源 SHA256：`5464d92253ad0b69d655d1f52419d7623fd16ca656de40c5b26fe25e4e2192d9`
- 选择与证据边界：最新 A/B 对比入口；SingleFile 时必须内联 A、B 两个 iframe 报告。

## 交付件

- [`anthropic-workspace-ab-experiment.html`](anthropic-workspace-ab-experiment.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。

## 归档验证

- 共归档 1 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

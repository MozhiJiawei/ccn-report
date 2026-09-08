# 实验总报告

> SMART 技术总结：截至 2026-08-04，《实验总报告》所述对象被本报告界定为围绕“Agent工作流”的可复现实验设计与方案对比，并以 归档实验的对照条件、生成结果与报告内评价证据覆盖核心机制、实现或评测证据、适用场景与限制边界四个可复核维度，用于支持Agent工作流 流程选择；结论只适用于归档时可验证的版本与来源。

## 归档信息

- 归档日期：2026-08-04
- 归档动作：新增报告
- 来源入口：`anthropic_2026_blog_token_quality_experiment_20260625/comparison/final_experiment_report.html`
- 来源 SHA256：`80acc14290b81c932fe8ccff752abb11350da593aa1f74ba8c5f9c0146e5e792`
- 选择与证据边界：README/命名明确为实验总报告；不误选后来放入同路径的“文档持久化”独立技术报告。

## 交付件

- [`comparison/final_experiment_report.html`](comparison/final_experiment_report.html)：主入口，使用仓库导出器与 `single-file-cli@2.0.83` 生成的 dependency-free SingleFile HTML。
- [`B_single_agent_html_report/final/index.html`](B_single_agent_html_report/final/index.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。
- [`C_orchestrated_nested_reports/final/index.html`](C_orchestrated_nested_reports/final/index.html)：主入口递归引用的同一逻辑报告子页，已完成 SingleFile 封装。

## 归档验证

- 共归档 3 个 HTML 页面；所有样式、脚本、图像与字体依赖均随页面封装，可离线打开。
- 归档目录仅包含 HTML 与本 README；生成日志、截图、manifest 和 QA 中间件保留在仓库外。

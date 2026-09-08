# PROMPTING.md：把 AI 指令当作可审计配置管理

## SMART 技术一句话

截至 2026-08-03 审阅的开源规则正文，PROMPTING.md 是面向编写和审计 AI 提示词、技能、计划、Agent 指令、记忆与交接材料的配置规则集，覆盖指令覆盖边界、跨会话状态、模型实际输入、工具权限、副作用以及六类测试与对抗场景，用于帮助 Claude Code、Codex、Cursor、OpenCode 等工具的使用者建立可检查的指令生命周期，但本轮未验证其跨模型行为效果。

## 归档信息

- 任务编号：TASK-20260803-03
- 热点编号：HS-20260803-03
- 周期：2026-W32
- 本地归档日期：2026-08-03
- 创建者：Codex

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile Source Understanding HTML。

## 来源与证据边界

- 原始证据来自作者 Reddit 发布帖、官方 GitHub 仓库和 PROMPTING.md 规则正文。
- 规则材料只能证明其设计、建议与作者声明，不能证明规则已经跨模型有效或消除了提示注入；本轮没有执行跨工具兼容性或部署级行为评测。
- OWASP 和 WASP 仅用于建立外部安全与评测对照，不作为该项目效果背书。

## QA 状态

- 来源包校验：通过。
- SingleFile 导出：成功。
- 主报告及两份对照报告均通过独立视觉 QA；本目录归档主报告，最终主报告 QA 为 PASS。

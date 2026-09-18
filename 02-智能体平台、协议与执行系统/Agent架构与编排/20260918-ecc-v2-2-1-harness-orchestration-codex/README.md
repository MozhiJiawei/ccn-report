# ECC-v2.2.1

## 一句话总结

ECC v2.2.1 是面向 AI 编码宿主的开源工程编排工具集，通过专业 Agent 分工、技能工作流与人工计划审批串起计划、测试、审查和记忆，其固定版本记录 68 个 Agent、286 项技能和 94 个命令入口，尚无本材料可支持的独立任务收益测量。

## 任务信息

- 序号：138
- 任务编号：TASK-20260916021220-fa9e2309
- 热点编号：HS-20260916-dsh-tech-insight
- 周期：2026-W38
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：category=null，依据正文自动归类；主要改变对象为专业Agent协作、计划审批及跨harness工作流组织，命中02/Agent架构与编排。研发效率是应用目标而不是通用构建工具贡献，故不归12/软件工程与研发效率；技能和执行hook是编排组成，未以工具调用器为中心。无指定值与AI判断差异。
- 任务正文：📌ECC v2.2.1 智能体调度框架：68 agents × 292 skills 多 harness 协同（Claude Code / Codex / Cursor / Kimi）
原文标题：affaan-m/ECC ⭐259192
元信息：战略 · 2026/09/16 · 编号 #45 · The agent harness performance optimization system.
要点：
- The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
技术效果：效果 · 推理强化：架构创新：据 affaan-m/ECC (AGENTS.md)：v2.2.1 包含 68 specialized subagents、292 workflow skills、94 slash commands、14 MCP server configurations，五大原则为 Agent-First、Test-Driven (80%+ 覆盖率)、Security-First、Immutability、Plan Before Execute；据 affaan-m/ECC (Releases)：v1.6.0 起就以 102 条安全规则 + 912 测试覆盖保护层，v2.1.0 引入 Plan Canvas 作为 harness-agnostic 的 CLI + JSON 协议
背景补充：据 affaan-m/ECC (README)：sponsor 已列 Moonshot AI (Kimi)、Itô Markets、Atlas Cloud、CodeRabbit、Greptile，v2.1.0 新增 Hermes 与 OpenClaw 作为 install target，私有仓库 ECC Pro 定价 $19/seat/mo
源链接：https://github.com/affaan-m/ECC
- 任务来源：[原始任务来源](https://github.com/affaan-m/ECC)

## 交付件说明

- [ECC-v2.2.1.html](./ECC-v2.2.1.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [ECC-v2.2.1.pptx](./ECC-v2.2.1.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

v2.2.1固定tag为286 skills，292来自后续main快照；资源数量、80%覆盖率要求及历史102安全规则/912测试不等于实际任务成功率或安全保证。多harness适配能力不同，不表示跨宿主自动协同或全部功能一致。赞助与定价属于项目背景，不构成技术收益证据。

## 引用信息源说明

- [ECC README（2026-09-18捕获后核对HEAD）](https://github.com/affaan-m/ECC/blob/dd6ee538aee0f548d4a6b520118f875431fd749e/README.md)：项目定位、工作流、harness能力边界与商业背景
- [ECC AGENTS.md v2.2.1 固定版本](https://github.com/affaan-m/ECC/blob/5064474d4d762dc9640234a41617cccb79185cec/AGENTS.md)：68/286/94固定版本计数与五大原则
- [ECC AGENTS.md 后续固定文件版本](https://github.com/affaan-m/ECC/blob/95b9fe157f815ef064793e49eacfecdbbfc5b813/AGENTS.md)：292技能与发布版本差异
- [ECC v2.1.0 Release](https://github.com/affaan-m/ECC/releases/tag/v2.1.0)：Plan Canvas CLI+JSON、Kimi安装目标、Hermes/OpenClaw新增
- [ECC v1.6.0 Release](https://github.com/affaan-m/ECC/releases/tag/v1.6.0)：AgentShield 102规则/912测试的历史统计口径

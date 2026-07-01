# Loop Engineering 架构图交付归档

## 归档信息

- 归档日期：2026-06-15
- 创建人：mozhi
- 报告类型：开源软件架构分析 / 3+1 架构视图
- 归档路径：`开源软件分析/Loop-Engineering/loop-engineering-architecture-20260615-mozhi/`

## 分析对象

本报告分析对象为本地仓库：

```text
D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\loop-engineering-analysis
```

该对象是 Loop Engineering 项目的代码与模板材料快照。本次分析围绕 Loop Engineering 的用例、逻辑视图、运行视图和开发视图展开，重点补充了 UC02「执行 Loop」以及 Codex Automations 下 PR Babysitter 场景的运行链路和开发侧 prompt / skill / template / config 约束。

## 归档来源

本目录内容从以下生成目录整理归档：

```text
D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\generate-3plus1-diagrams\loop-engineering-analysis
```

归档时排除了预览服务运行日志 `preview-server*.log`；保留 HTML 页面、可编辑 `.drawio`、导出 PNG、JSON 中间模型、evidence/assumptions 说明、visual review 和 QA 截图。

## 主要入口

- `index.html`：翻页式 HTML 图册入口。
- `use-case/`：全局用例视图与用例目录。
- `UC01/`：UC01「定义 Loop」的逻辑视图、运行视图、开发视图。
- `UC02/`：UC02「执行 Loop」的逻辑视图、运行视图、开发视图。

重点新增页面：

- `UC02/runtime/exports/Codex PR Babysitter tick.webp`
- `UC02/development/exports/pr-babysitter-development-view-with-code.webp`

## 交付内容

```text
index.html
use-case/
UC01/
UC02/
qa-index-*.png
```

每个视图目录通常包含：

- `*.json`：结构化中间模型。
- `*.drawio`：可编辑 draw.io 源文件。
- `exports/*.png`：导出预览图。
- `evidence-assumptions.md` 或同类 evidence 文件：证据、假设与取舍说明。
- `exports/visual-review.md`：视觉检查记录。

## 说明

- 本报告以架构图阅读为主，`index.html` 已按单图一页的 PPT 式页面组织。
- UC02 的 PR Babysitter 运行视图明确表达：Codex Automations 定时触发一个主 Agent run；主 run 根据 state、GitHub PR/CI/Review 与 triage 结果，条件性调度 worktree、minimal-fix implementer 和 verifier；最终只评论、回写状态并交给人工门禁，不自动 merge。
- UC02 的 PR Babysitter 开发视图已新增“涉及代码”栏，用于展示每个 prompt / config / skill / template / CLI 卡片对应的首开文件。

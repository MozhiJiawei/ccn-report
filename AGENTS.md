# AGENTS.md

本仓库用于归档 AI 生成的正式报告交付件，不是 skill 仓库。

## Archive Scope

- 只归档正式交付件、必要源材料、QA 记录和报告说明。
- 不归档临时草稿、缓存、运行日志、未整理的中间导出。
- 仓库根目录只保存说明、脚本和分类入口。

## Directory Rules

报告必须进入两层分类后再创建独立报告目录：

```text
<大类>/<对象或方向>/<report-slug>-<YYYYMMDD>-<creator>/
```

当前大类：

- `大厂动态/`
- `开源软件分析/`
- `学术论文分析/`

示例二级目录：

- `大厂动态/Anthropic/`
- `大厂动态/OpenAI/`
- `开源软件分析/LangChain/`
- `开源软件分析/OpenHarness/`
- `学术论文分析/Agent/`
- `学术论文分析/推理/`

## Report Directory Naming

报告目录名必须满足：

```text
<report-slug>-<YYYYMMDD>-<creator>
```

规则：

- `<report-slug>` 使用小写字母、数字和短横线。
- `<YYYYMMDD>` 使用 8 位日期，例如 `20260611`。
- `<creator>` 使用小写字母、数字和短横线。
- 报告文件不能直接放在大类目录或二级分类目录下。

## Report Package Contents

每个报告目录内部结构由交付件自身决定，不强制套用统一模板。

允许归档的正式交付形态包括 HTML、PPTX、PDF、Markdown、图片包、源材料摘要和 QA 记录。无论采用哪种形态，都必须先创建符合命名规则的报告目录，不能把交付文件直接放在大类或二级分类目录下。

## Pre-Commit Gates

提交前必须运行：

```powershell
python scripts/pre_commit_gate.py
```

若门禁失败，先修复目录层级或命名问题，再提交。

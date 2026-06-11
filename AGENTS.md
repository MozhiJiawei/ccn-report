# AGENTS.md

本仓库用于归档 AI 生成的正式报告交付件，不是 skill 仓库。

## Archive Scope

- 只归档正式交付件、必要源材料、QA 记录和报告说明。
- 不归档临时草稿、缓存、运行日志、未整理的中间导出。
- 仓库根目录只保存说明、模板、脚本和分类入口。

## Directory Rules

报告必须进入两层分类后再创建独立报告目录：

```text
reports/<大类>/<对象或方向>/<report-slug>-<YYYYMMDD>-<creator>/
```

当前大类：

- `reports/大厂动态/`
- `reports/开源软件分析/`
- `reports/学术论文分析/`

示例二级目录：

- `reports/大厂动态/Anthropic/`
- `reports/大厂动态/OpenAI/`
- `reports/开源软件分析/LangChain/`
- `reports/开源软件分析/OpenHarness/`
- `reports/学术论文分析/Agent/`
- `reports/学术论文分析/推理/`

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

每个报告目录建议包含：

```text
REPORT.md
deliverables/
sources/
qa/
```

- `REPORT.md` 记录报告目的、产物清单、来源、QA 和变更记录。
- `deliverables/` 放最终交付文件。
- `sources/` 放允许归档的输入材料或引用材料。
- `qa/` 放校验结果、截图、导出预览或人工检查记录。

## Pre-Commit Gates

提交前必须运行：

```powershell
python scripts/pre_commit_gate.py
```

若门禁失败，先修复目录层级或命名问题，再提交。

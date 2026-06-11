# AGENTS.md

本仓库用于归档 AI 生成的正式报告交付件，不是 skill 仓库。

## Archive Scope

- 只归档正式交付件、必要源材料、QA 记录和报告说明。
- 不归档临时草稿、缓存、运行日志、未整理的中间导出。
- 仓库根目录只保存说明、脚本和分类入口。

## Directory Rules

报告必须进入大类和对象或方向之后，再创建独立报告目录；中间可以按需要增加自定义子类：

```text
<大类>/<对象或方向>/.../.../<report-slug>-<YYYYMMDD>-<creator>/.../
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
- `<creator>` 使用中文、英文字母、数字、短横线或下划线。
- 报告文件不能直接放在大类、对象或方向、自定义子类目录下。
- 大类目录下不能直接创建报告目录；至少需要 `<大类>/<对象或方向>/<报告目录>`。
- 合法报告目录内部可以继续创建任意子目录和文件，不再受归档层级门禁约束。

## Report Package Contents

每个报告目录内部结构由交付件自身决定，不强制套用统一模板。

允许归档的正式交付形态包括 HTML、PPTX、PDF、Markdown、图片包、源材料摘要和 QA 记录。无论采用哪种形态，都必须先创建符合命名规则的最终报告目录，不能把交付文件直接放在大类、对象或方向、自定义子类目录下。

## Git LFS Rules

三大归档目录下的文件默认走 Git LFS。

以下可读文本扩展名通过 `.gitattributes` 白名单保留普通 Git diff：

```text
.md .markdown .html .htm .css .js .mjs .cjs .ts .tsx .jsx
.json .jsonl .yaml .yml .toml .txt .csv .tsv .svg .xml
```

白名单文本文件超过 5 MiB 时，`python scripts/pre_commit_gate.py` 会失败。归档前应优先拆出内嵌图片或大资产；若确实需要保留单个超大文本文件，应在 `.gitattributes` 为该具体路径添加 Git LFS 例外。

## Pre-Commit Gates

提交前必须运行：

```powershell
python scripts/pre_commit_gate.py
```

若门禁失败，先修复目录层级或命名问题，再提交。

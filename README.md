# CCN Report Archive

AI 生成报告交付件归档仓库。

本仓库只保存可追踪、可复用的正式交付件和必要元信息；临时草稿、导出日志、运行缓存不进入归档。

## Directory Convention

```text
.
|-- AGENTS.md
|-- README.md
|-- reports/
|   |-- 大厂动态/
|   |   |-- Anthropic/
|   |   `-- OpenAI/
|   |-- 开源软件分析/
|   |   |-- LangChain/
|   |   `-- OpenHarness/
|   `-- 学术论文分析/
|       |-- Agent/
|       `-- 推理/
|-- scripts/
|   |-- check_report_archive.py
|   `-- pre_commit_gate.py
`-- templates/
    `-- REPORT.md
```

## Report Package

报告必须归档到二级分类目录下的独立子目录，不能直接放在大类或二级分类根目录。

```text
reports/<大类>/<对象或方向>/<report-slug>-<YYYYMMDD>-<creator>/
```

示例：

```text
reports/大厂动态/OpenAI/gpt-5-market-scan-20260611-mozhi/
reports/开源软件分析/LangChain/langgraph-runtime-review-20260611-mozhi/
reports/学术论文分析/Agent/multi-agent-planning-survey-20260611-mozhi/
```

目录名规则：

- `<report-slug>`：小写字母、数字和短横线，例如 `gpt-5-market-scan`。
- `<YYYYMMDD>`：8 位日期，例如 `20260611`。
- `<creator>`：小写字母、数字和短横线，例如 `mozhi`。

每个报告目录建议包含：

- `REPORT.md`：交付说明、背景、产物清单、生成方式和版本记录。
- `deliverables/`：最终交付文件，例如 `.pptx`、`.pdf`、`.docx`、`.xlsx`、图片包。
- `sources/`：允许归档的输入材料、摘要、引用材料或源文件。
- `qa/`：校验记录、截图、导出预览、人工检查记录。

## Archive Rules

- 根目录不直接放报告文件。
- 大类目录下不直接放报告文件。
- 二级分类目录下只放报告目录，不直接放单个交付文件。
- 一个报告一个目录，不把多个主题混在同一目录。
- 报告目录名必须满足 `<report-slug>-<YYYYMMDD>-<creator>`。
- 大型中间文件、缓存、临时导出默认不归档。

## Validation

提交前运行：

```powershell
python scripts/pre_commit_gate.py
```

该入口会检查报告归档目录是否满足分类层级和命名规则。

# CCN Report Archive

AI 生成报告交付件归档仓库。

本仓库只保存可追踪、可复用的正式交付件和必要元信息；临时草稿、导出日志、运行缓存不进入归档。

## Directory Convention

```text
.
|-- AGENTS.md
|-- README.md
|-- 大厂动态/
|   |-- Anthropic/
|   `-- OpenAI/
|-- 开源软件分析/
|   |-- LangChain/
|   `-- OpenHarness/
|-- 学术论文分析/
|   |-- Agent/
|   `-- 推理/
|-- scripts/
|   |-- check_report_archive.py
|   `-- pre_commit_gate.py
```

## Report Package

报告必须归档到对象或方向目录之后的独立报告目录里，中间可以按需要增加自定义子类。

```text
<大类>/<对象或方向>/.../.../<report-slug>-<YYYYMMDD>-<creator>/.../
```

示例：

```text
大厂动态/OpenAI/gpt-5-market-scan-20260611-mozhi/
大厂动态/OpenAI/模型发布/gpt-5-market-scan-20260611-mozhi/
开源软件分析/LangChain/Runtime/LangGraph/langgraph-runtime-review-20260611-mozhi/
学术论文分析/Agent/多智能体规划/multi-agent-planning-survey-20260611-mozhi/
```

目录名规则：

- `<report-slug>`：小写字母、数字和短横线，例如 `gpt-5-market-scan`。
- `<YYYYMMDD>`：8 位日期，例如 `20260611`。
- `<creator>`：中文、英文字母、数字、短横线或下划线，例如 `mozhi`、`墨之`、`mozhi-jiawei`。

每个报告目录内部结构由交付形态决定。HTML、PPTX、PDF、图片包、源材料和 QA 记录都可以按该报告自身需要组织。

## Archive Rules

- 根目录不直接放报告文件。
- 大类目录下不直接放报告文件。
- 对象或方向目录及其自定义子类目录下不直接放单个交付文件。
- 一个报告一个目录，不把多个主题混在同一目录。
- 只有最终报告目录名必须满足 `<report-slug>-<YYYYMMDD>-<creator>`。
- 报告目录内部可以按交付件需要继续创建任意子目录和文件。
- 大型中间文件、缓存、临时导出默认不归档。
- 不强制使用统一模板；报告内容可以是 HTML、PPTX、PDF、Markdown 或其他正式交付形态。

## Git LFS

三大归档目录下的文件默认使用 Git LFS，以避免 PPTX、PDF、图片、视频、压缩包等交付件撑大 Git 历史。

可读文本文件通过 `.gitattributes` 白名单保留普通 Git diff，例如 Markdown、HTML、CSS、JavaScript、JSON、YAML、CSV、SVG、XML 和纯文本。

白名单文本文件如果超过 5 MiB，门禁会失败。处理方式：

- 优先拆出内嵌图片或大资产，让二进制资产走 LFS。
- 如果确实需要归档单个超大文本文件，在 `.gitattributes` 为该具体路径添加 Git LFS 例外。

## Validation

提交前运行：

```powershell
python scripts/pre_commit_gate.py
```

该入口会检查报告归档目录是否满足分类层级和命名规则。

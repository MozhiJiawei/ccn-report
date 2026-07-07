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

每个报告目录内部只归档最终交付件和必要说明。正式交付形态只允许：

- dependency-free HTML：必须是可离线打开的 SingleFile 单文件 HTML。
- PPTX：可编辑或可演示的幻灯片文件。
- `README.md`：可选，用于补充报告说明、来源摘要或人工核验备注。

## Archive Rules

- 根目录不直接放报告文件。
- 大类目录下不直接放报告文件。
- 对象或方向目录及其自定义子类目录下不直接放单个交付文件。
- 一个报告一个目录，不把多个主题混在同一目录。
- 只有最终报告目录名必须满足 `<report-slug>-<YYYYMMDD>-<creator>`。
- 报告目录内部只保留 HTML、PPTX 和可选 `README.md`。
- 大型中间文件、缓存、临时导出默认不归档。
- 不归档 PDF、图片依赖包、源码材料、QA 中间记录或生成日志；如需说明，整理进 `README.md`。

## Git LFS

三大归档目录下的交付件默认使用 Git LFS，以避免 SingleFile HTML 和 PPTX 撑大 Git 历史。

只有报告说明 Markdown 保留普通 Git diff。HTML 和 PPTX 都是正式交付件，默认走 LFS。

## HTML SingleFile Export

HTML 报告必须使用 SingleFile 单文件归档，不能依赖旁路 CSS、JS、图片或字体文件。常规导出：

```powershell
python scripts/export_singlefile_archive.py --root <html-root> <entry.html> --output-dir <archive-output-dir>
python scripts/pre_commit_gate.py
```

入口页会索引子报告时追加 `--recursive-linked-html`。导出后只归档 HTML、PPTX 和 `README.md`。

## Latest Release Package

GitHub Release 只维护最新离线下载包。PR 合入 `main` 后运行：

```powershell
python scripts/release_compressed_archive.py --quality 70
```

默认会更新 `latest-compressed-archive` 这个滚动 Release，并覆盖 zip、`manifest.json` 和 `SHA256SUMS.txt`。只有需要长期保留里程碑时才使用 `--snapshot` 创建独立 Release。

## Validation

提交前运行：

```powershell
python scripts/pre_commit_gate.py
```

该入口会检查报告归档目录是否满足分类层级和命名规则。

# AGENTS.md

本仓库用于归档 AI 生成的正式报告交付件，不是 skill 仓库。

## Archive Scope

- 只归档正式交付件和必要报告说明。
- 不归档临时草稿、缓存、运行日志、未整理的中间导出。
- 仓库根目录只保存说明、脚本和分类入口。

## Directory Rules

报告必须进入大类和对象或方向之后，再创建独立报告目录；中间可以按需要增加自定义子类：

```text
<大类>/<对象或方向>/.../.../<YYYYMMDD>-<report-slug>-<creator>/.../
```

当前常用大类（仅作为示例，不是归档脚本的固定白名单）：

- `大厂动态/`
- `开源软件分析/`
- `学术论文分析/`

归档脚本和门禁会从仓库根目录递归发现符合命名规则的最终报告目录。可以新增、改名或调整分类根目录，无需同步修改代码；报告目录仍须位于仓库根目录至少两级之下。

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
<YYYYMMDD>-<report-slug>-<creator>
```

规则：

- `<YYYYMMDD>` 使用 8 位合入日期，例如 `20260611`。
- `<report-slug>` 使用小写字母、数字和短横线。
- `<creator>` 使用中文、英文字母、数字、短横线或下划线。
- 报告文件不能直接放在大类、对象或方向、自定义子类目录下。
- 大类目录下不能直接创建报告目录；至少需要 `<大类>/<对象或方向>/<报告目录>`。
- 合法报告目录内部可以继续创建任意子目录和文件，不再受归档层级门禁约束。

## Report Package Contents

每个报告目录内部只保留最终交付件和可选说明，不强制套用统一模板。

允许归档的正式交付形态只有：

- dependency-free HTML：必须是 SingleFile 单文件 HTML，离线打开不依赖旁路 CSS、JS、图片或字体文件。
- PPTX：可编辑或可演示的幻灯片文件。
- `README.md`：可选，用于补充报告说明、来源摘要或人工核验备注。

不归档 PDF、图片依赖包、源码材料、QA 中间记录或生成日志；如需说明，整理进 `README.md`。无论采用哪种形态，都必须先创建符合命名规则的最终报告目录，不能把交付文件直接放在大类、对象或方向、自定义子类目录下。

## HTML SingleFile Export

- HTML 报告必须先导出为 SingleFile 单文件，再进入归档。
- 常规导出：

```powershell
python scripts/export_singlefile_archive.py --root <html-root> <entry.html> --output-dir <archive-output-dir>
```

- 入口页会索引子报告时，追加 `--recursive-linked-html`。
- 导出后报告目录只保留 HTML、PPTX 和 `README.md`。
- 其他参数按需查看 `python scripts/export_singlefile_archive.py --help`。

## Release Packages

- GitHub Release 只维护一个滚动发布入口；不要为每次合入创建永久日期 Release。
- PR 合入 `main` 后，更新滚动 Release：

```powershell
python scripts/release_compressed_archive.py --quality 70
```

- 默认 tag 为 `latest-compressed-archive`；报告通过最终目录名中的 `YYYYMMDD` 识别，再按月份生成 `ccn-report-YYYYMM-q70.zip`。
- 每个 ZIP 保留仓库相对目录结构，可将多个月度包解压到同一目录增量合并。
- 同时发布 `ccn-report-full-q70.zip` 全量包，供首次下载或一次性获取全部报告。
- 根目录 `index.html` 独立发布，不合入月度包或全量包。
- 脚本通过上一版 manifest 跳过未变化月度包；全量包仅在报告内容变化时覆盖，并清理失效月度包、旧日期包和旧格式整仓大包。
- `manifest.json` 和 `SHA256SUMS.txt` 每次更新，作为滚动资产索引。
- 只有人工明确要求保留里程碑快照时，才使用 `--snapshot` 创建带时间戳的独立 Release。

## Git LFS Rules

动态发现到的报告目录中的 HTML 和 PPTX 默认走 Git LFS；根目录 `index.html` 保留普通 Git diff。

只有报告说明 Markdown 保留普通 Git diff：

```text
.md .markdown
```

HTML 和 PPTX 都是正式交付件，默认走 LFS；

## Pre-Commit Gates

提交前必须运行：

```powershell
python scripts/pre_commit_gate.py
```

若门禁失败，先修复目录层级、命名问题或报告目录内的非归档文件，再提交。

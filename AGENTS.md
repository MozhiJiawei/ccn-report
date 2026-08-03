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

每个报告目录内部只保留最终交付件和必要说明，不强制套用统一模板。

允许归档的正式交付形态只有：

- dependency-free HTML：必须是 SingleFile 单文件 HTML，离线打开不依赖旁路 CSS、JS、图片或字体文件。
- PPTX：可编辑或可演示的幻灯片文件。
- `README.md`：必需，用于提供 SMART 技术一句话总结，并可补充来源摘要或人工核验备注。

### README SMART Summary

每个报告目录的 `README.md` 必须包含一句独立、完整、可直接引用的技术总结，回答“这个技术是什么”，并满足 SMART：

- **Specific**：明确技术对象、目标用户或运行平台以及解决的问题。
- **Measurable**：写出来源可验证的规模、覆盖范围、指标、评分权重或验证状态。
- **Achievable**：只陈述当前版本已经实现或论文已经验证的能力，不把规划、目标或推断写成事实。
- **Relevant**：说明该技术对目标场景的直接价值或用途。
- **Time-bound**：注明版本、论文版本、发布日期、评测时间或其他有效时间边界。

该总结必须保持为一句话；可以使用分号或冒号组织信息，但不能拆成多条口号。若来源没有性能数字，应使用支持的平台、任务覆盖、验证条件或能力边界实现可衡量性，禁止为了满足 SMART 编造数据。

不归档 PDF、图片依赖包、源码材料、QA 中间记录或生成日志；如需说明，整理进 `README.md`。无论采用哪种形态，都必须先创建符合命名规则的最终报告目录，不能把交付文件直接放在大类、对象或方向、自定义子类目录下。

## HTML SingleFile Export

- HTML 报告必须先导出为 SingleFile 单文件，再进入归档。
- 常规导出：

```powershell
python scripts/export_singlefile_archive.py --root <html-root> <entry.html> --output-dir <archive-output-dir>
```

- 入口页会索引子报告时，追加 `--recursive-linked-html`。
- 导出器会扫描 HTML 中的本地 `href`、`src` 和 CSS `url(...)` 引用；资源位于 `--root` 外时，会自动上移临时 HTTP 服务根目录，同时保持输出仍相对于 `--root`。
- SingleFile 若产出空的 `data:` 图片会判定导出失败，避免把本地图片加载失败的残缺页面归档。
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

## Pull Request Delivery

- 用户要求“提 PR”“合入”“合并”或其他等价交付时，默认表示完成整套交付流程，而不只是创建 PR。
- 创建 PR 后必须持续跟进 CI、自动化检查和评审意见；出现失败或新增反馈时，应修复、提交并重新验证，不能在推送修复后停止跟进。
- 只有 PR 已实际合并进目标分支，且合并后的远端状态已确认，任务才算完成；仅达到“CI 通过”“可合并”或“等待人工点击合并”不算完成。
- 若受权限、必需人工审批、语义冲突或外部系统故障阻塞，必须明确报告阻塞原因和所需人工动作；除此之外不要把可自动完成的收尾留给用户。

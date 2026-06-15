# UC01 定义 Loop - 开发视图证据与假设

## 证据口径

- 只跟踪 `README.md`、`docs/pattern-picker.md`、`docs/loop-design-checklist.md`、`starters/README.md`、`patterns/registry.yaml`、`tools/loop-init/`、`tools/loop-cost/`、`tools/loop-audit/` 这条链上的开发者维护单元。
- 边方向统一表示“源模块依赖目标模块”，含文档入口依赖、包内打包依赖、元数据读取依赖和补件资产依赖。
- 优先保留仓库中明确出现的命令、路径和字段；只有 `loop-init -> pattern-registry` 这条同步边使用了推断。

## Pruning / Omissions

- 省略 `patterns/*.md` 全量正文、`examples/`、`stories/`、`assets/visuals/`、`resources/`，因为它们对 UC01 的“定义 Loop”主维护链不是第一层依赖。
- 省略 `dist/`、`package-lock.json`、`node_modules/`、`web-captures/`、`.tmp/` 和其他缓存/导出物。
- 不把生成后的 `STATE.md`、`LOOP.md`、`loop-budget.md`、`loop-run-log.md` 单列成节点；这些文件在本视图中被折叠进 `Starter & Templates` 和 `loop-init / loop-audit` 两类维护边界。
- 不单列 `tools/loop-audit/src/reporter.ts`、各 tool 变体的单个 skill 文件和每个 starter 子目录；它们被折叠到对应 CLI 包或 Starter 资产包中，以避免图退化成目录树。

## Inferred Relationships

- `loop-init CLI -> Pattern Registry` 标记为 `inferred: true`：
  - 证据显示 `loop-init` 当前运行时依赖的是 `PATTERN_STARTERS`、`STATE_FILES`、`PATTERN_BUDGET` 等硬编码常量。
  - 同时，`bundle-assets.mjs` 会把根 `patterns/registry.yaml` 镜像进 `tools/loop-init/registry.yaml`。
  - 因此，这条边更像“发布与维护时需要保持同义”的同步依赖，而不是当前版本的直接解析依赖。

## Key Assumptions

- `README/docs -> tools` 这些边保留下来，是因为 UC01 明确从开发者入口面开始；它们表达的是“维护入口必须和工具包保持一致”，不是源码 import 关系。
- `Starter & Templates` 被视作一个开发者会整体维护的资产包，因为 `loop-init` 和 `loop-audit --suggest` 都按这一层级消费它，而不是按单个文件零散消费。
- `loop-cost` 与 `loop-audit` 在用户工作流里前后相邻，但在代码视图中是独立 CLI；本模型没有人为加一条两者之间的直接代码依赖边。

## Remaining Uncertainties

- `tools/loop-init/registry.yaml` 当前是否会在后续版本替代硬编码常量，仓库内没有直接证据；若实现切换，这条边应从 inferred 升级为 explicit。
- `loop-audit` 只检查 `patterns/registry.yaml` 的存在性，不检查字段质量，因此 readiness 和 pattern 元数据目前仍是松耦合关系。
- 不同 starter 之间的差异已经折叠；若后续需要单独解释 `pr-babysitter` 或 `dependency-sweeper` 的定义路径，需要把 `Starter & Templates` 再切开。

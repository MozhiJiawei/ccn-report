# UC01 定义 Loop - Logic View Evidence & Assumptions

## Scope

本中间模型只解释 `UC01 定义 Loop` 的稳定责任协作：

- 选择 pattern 与工具
- 复制或脚手架 starter
- 配置 `STATE.md`、`LOOP.md`、skills、verifier、`loop-budget.md`、`loop-run-log.md`
- 估算 cadence / token 成本
- 审计 readiness
- 明确 `L1 -> L2 -> L3`、human gates、pause/kill 规则

不覆盖 loop 运行期的具体 triage/fix/verify 交互，也不重建整个仓库全景。

## Evidence Basis

核心证据分四类：

1. 入口与定义引导：`README.md`、`docs/pattern-picker.md`、`docs/loop-design-checklist.md`
2. 装配路径：`starters/README.md`、`starters/minimal-loop-codex/*`、`tools/loop-init/README.md`、`tools/loop-init/src/cli.ts`
3. 评估路径：`tools/loop-cost/*`、`tools/loop-audit/*`、`patterns/registry.yaml`
4. 治理与持久状态：`LOOP.md`、`STATE.md`、`loop-budget.md`、`loop-run-log.md`、`docs/operating-loops.md`、`docs/safety.md`

## Modeling Decisions

### Collapsed responsibilities

- 把 `README Quick Links`、`Getting Started`、以及它们暴露的工具/文档入口折叠成一个 `定义入口`，因为它们的职责是引导，不是各自独立执行业务逻辑。
- 把手工复制 starter 与 `loop-init` 自动脚手架折叠成一个 `Starter 装配`，因为两者都在完成同一个稳定责任：把被选中的 loop 模式具体化到项目根目录。
- 把 `STATE.md`、`LOOP.md`、`loop-budget.md`、`loop-run-log.md` 折叠成一个 `Loop 骨架`，因为它们共同承载 durable state、cadence、budget、kill switch 与 run history。
- 把 triage/minimal-fix/verifier/loop-budget 等 skill 与 agent 配置折叠成一个 `技能守护`，因为它们共同承担 maker/checker split 与运行时约束，而不是独立的用例目标。

### Kept rendered

- `模式选择 -> Starter 装配`：解释为什么装配不是裸复制，而是 pattern/tool-aware 的选择结果。
- `Starter 装配 -> Loop 骨架 / 技能守护`：解释定义 Loop 时到底要落什么东西到项目里。
- `Loop 骨架 / 技能守护 -> 就绪审计`：解释 audit 评分依赖哪些已定义的结构。
- `成本估算 / 就绪审计 / Loop 骨架 -> 升级门控`：解释从“能跑”到“能升 L2/L3”之间的治理判断。

### Render pruning

- 为满足 stacked-groups 的直线布局约束，`entry_hub -> design_checklist`、`design_checklist -> skill_guardrails`、`starter_scaffold -> skill_guardrails`、`loop_contract -> upgrade_gates`、`pattern_selector -> cost_estimator` 保留在 JSON 关系与证据中，但设为 `render:false`。

## Omitted or Not Rendered

- `定义入口 -> loop-init / loop-cost / loop-audit` 的直接扇出没有单独成边，而是通过下游责任转述，避免入口层形成多叉星形。
- `设计清单 -> 升级门控` 这条语义上成立，但已经由 `设计清单` 的 element 说明和 `就绪审计 -> 升级门控`、`Loop 骨架 -> 升级门控` 覆盖，因此未额外渲染。
- `成本估算 -> Loop 骨架` 的直接关系也未画出；仓库里更多体现为“先估算，再把 budget/kill switch 写入文档”，因此在模型里通过 `升级门控` 这一治理责任汇合。
- 未把每个 pattern、每个 starter variant、每个具体 skill 目录拆成独立节点，否则图会退化成目录树。

## Inferred Relationships

以下关系是逻辑责任上的强约束，但不是单一代码调用：

- `设计清单 -> Starter 装配`
- `设计清单 -> 技能守护`

原因：checklist 定义了装配时必须补齐的 state / verifier / cost / safety / human handoff 责任，但这些约束在仓库中分散体现为文档、starter 样板与 CLI scaffolding 规则。

## Key Uncertainties

- 仓库把“定义 Loop”同时做成了文档引导、starter 样板和 CLI 工具；本模型把这三种交付面折叠成一套逻辑协作，而不是三条并行产品线。
- `loop-audit` 的 `L3` 是 readiness classification，不等于系统自动强制进入 unattended；真正启停仍依赖人类遵循 `LOOP.md` 与安全规则。
- human gates、denylist、pause/kill 规则并非都由同一文件集中声明；它们散落在 checklist、starter LOOP、root LOOP、operating-loops 与 safety 中，因此 `升级门控` 是一个汇聚责任而非单文件模块。

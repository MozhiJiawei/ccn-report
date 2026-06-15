# UC02「执行 Loop」逻辑视图证据与假设

## 范围确认

本轮只建模 UC02「执行 Loop」的逻辑视图中间模型。

- 主参与者：`Loop 操作者`
- 入口面：`patterns/README.md`、`patterns/registry.yaml`、Grok `/loop`、Claude `/loop`、Codex Automations、GitHub Actions
- 用例摘要：定义完成后，按选定 cadence 或事件触发运行 loop，并把模式接到 Grok、Claude、Codex 或 GitHub Actions / 外部 harness

以上边界来自既有用例结果：

- `D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\generate-3plus1-diagrams\loop-engineering-analysis\use-case\use-case-view.json`
- `D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\generate-3plus1-diagrams\loop-engineering-analysis\use-case\evidence-assumptions.md`

## 本轮建模结论

本次把 UC02 的逻辑结构收敛为四层：

1. `运行入口面`
2. `Loop 编排层`
3. `执行资产与守护层`
4. `外部工作系统`

核心判断是：这个仓库在“执行 Loop”上提供的不是单一运行程序，而是一套跨工具共享的运行契约。

- 入口面负责触发
- 编排层负责按模式运行
- 执行资产层负责提供模式元数据、技能、检查者、状态脊柱、预算与 readiness 门禁
- 外部工作系统提供被观察和被驱动的真实工程上下文

## 关键证据

| 证据文件 | 为什么重要 |
| --- | --- |
| `README.md` | 顶层把 Patterns、Starters、Examples by Tool、Operating & Safety 并列暴露，说明执行能力是“跨工具运行体系”，不是单个 CLI。 |
| `LOOP.md` | 明确了当前仓库有哪些 active loops、cadence、phase、worktree、budget、kill switch 与 handoff。 |
| `patterns/README.md` | 把 7 个模式组织成统一模式库，并把 set up scheduling、week one、audit 视为共同执行流程。 |
| `patterns/registry.yaml` | 为每个模式统一声明 tools、skills、state、phases、human_gates、week_one_mode、token_cost。 |
| `docs/primitives.md` | 把 scheduling、worktree、skills、connectors、sub-agents、state 明确成 loop 的基础构件。 |
| `examples/claude-code/daily-triage.md` | 证明动作阶段需要 implementer + verifier，并要求 `isolation: worktree`。 |
| `examples/codex/daily-triage.md` | 证明 Codex 的执行入口是 Automations，结果进入 Triage inbox 并回写 `STATE.md`。 |
| `examples/github-actions/README.md` 与 `daily-triage.yml` | 证明 GitHub Actions 主要负责触发、收集上下文、委派到 agent harness。 |
| `skills/loop-triage/SKILL.md` | 证明 loop 会读取 CI、Issue、提交、聊天和 state，并输出结构化发现。 |
| `skills/loop-verifier/SKILL.md` | 证明执行动作不是单代理闭环，而是 maker/checker split。 |
| `docs/operating-loops.md`、`tools/loop-audit/README.md`、`tools/loop-cost/README.md` | 证明预算、run log、activity proof、L1-L3、kill switch 都是执行期持续生效的控制能力。 |

## 为什么没有把 7 个 pattern 画成 7 个顶级系统

这点需要单独说明。

我没有把 `Daily Triage`、`PR Babysitter`、`CI Sweeper`、`Dependency Sweeper`、`Changelog Drafter`、`Post-Merge Cleanup`、`Issue Triage` 画成 7 个顶级系统，原因是：

1. `patterns/registry.yaml` 显示它们共享同一套字段模型：
   `goal / cadence / tools / skills / state / phases / human_gates / starter / week_one_mode / token_cost`
2. `patterns/README.md` 把它们当成同一模式库中的“pick one and run”模式，而不是 7 个彼此隔离的产品。
3. `starters/README.md` 与 `examples/README.md` 显示共享的是运行骨架，只是技能包、状态文件和触发方式不同。
4. `loop-audit` 与 `loop-cost` 也是围绕统一 registry 和统一 readiness/budget 约束工作的。

因此，更稳定的逻辑切法是：

- 画一个 `模式目录（7种）`
- 把差异留在模式元数据、技能组合、状态文件和门禁规则里
- 不把模式数量误画成系统数量

## 推断与保守处理

以下内容做了保守推断，并在 JSON 里标记为 `inferred` 或放入 `uncertainties`：

1. `GitHub Actions + Harness` 被建模为入口面，而不是执行内核。
   原因是示例 workflow 的 “Run triage agent” 仍是占位接线。
2. `隔离工作树 -> 协作/代码系统` 的关系保留为 `render: false`。
   这条关系在概念上成立，但如果直接画出来，会把逻辑图往 runtime 协作图方向带偏。
3. `Codex Triage inbox` 没有单独建模成独立逻辑元素。
   我把它吸收到 `协作/代码系统` 中，因为它更像某个宿主工具提供的交付面，而不是仓库独有的稳定责任边界。

## 本轮刻意省略

- 不展开单个 pattern 的 detect/triage/fix/verify 详细顺序。
- 不展开具体 workflow job、CLI 参数、技能正文段落。
- 不把 `templates/`、`stories/`、`assets/`、`web-captures/` 建成逻辑元素。
- 不把 UC01 的 `loop-init` 脚手架细节并入当前视图中心，只保留与 UC02 明确耦合的状态、预算与 readiness 资产。

## 未解决不确定性

1. 未来如果仓库新增统一宿主 runtime 或 headless controller，`Loop 编排层` 可能需要从“约定性编排”改画成“具体控制器”。
2. Issue Triage 的专属 starter/example 证据弱于其他模式；当前仍按统一模式目录处理。
3. GitHub Actions 场景下到底接 Codex CLI、`repository_dispatch` 还是自定义 harness，仓库示例刻意留白，所以不宜在 logic view 中画成单一确定实现。

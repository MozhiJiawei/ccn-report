# PR Babysitter 开发视图代码证据说明

## 建模结论

- 本次补订把开发视图收束成 11 个“开发者会真的点开”的入口卡片，优先选择单个 prompt、单个 starter 文档、单个 skill/template、单个 agent 配置和单个 CLI 文件。
- `paths` 没有故意凑成多文件列表。对这个场景来说，很多关键模块本身就是“一份文件即一个契约”，例如 `examples/codex/pr-babysitter.md`、`templates/SKILL.md.minimal-fix`、`starters/pr-babysitter/.codex/agents/verifier.toml`。
- 原始视图里的 `Verifier` 被拆成两个节点：`verifier.toml` 和 `Verifier Template`。这样“涉及代码”栏能明确区分 repo-local checker 配置，与共享 fallback 契约模板。
- `minimal-fix` 继续用共享模板建模，而不是伪造一个 starter 本地 skill 节点；本次扫描未发现 `starters/pr-babysitter/.codex/skills/minimal-fix/SKILL.md`。
- 保留 `patterns/registry.yaml` 与 `patterns/pr-babysitter.md`，因为开发者要解释“为什么 loop 要这样跑”，这两个文件就是最先回看的规则源，而不是纯文档噪音。

## 涉及代码栏取舍

| 卡片 | 选用 `paths` | 取舍理由 |
| --- | --- | --- |
| Pattern Registry | `patterns/registry.yaml` | 这是机器可读模式入口，开发者会先看这里确认 skills、state、starter 和 human gates。 |
| Pattern Guide | `patterns/pr-babysitter.md` | 这是解释 loop 周期、verification strategy 和 human handoff 的主文档。 |
| Codex Prompt | `examples/codex/pr-babysitter.md` | 这是 Codex Automations 侧最直接的提示词入口，不需要再把别的 prompt 资产并进来。 |
| Starter README | `starters/pr-babysitter/README.md` | 开发者接入 starter 时，第一个会打开的就是 quick start 与安全说明。 |
| LOOP.md | `starters/pr-babysitter/LOOP.md` | 这是 repo 内可维护的 loop 参数文件，应该独立成卡，而不是藏在 README 下。 |
| State Schema | `starters/pr-babysitter/pr-babysitter-state.md.example` | watched PR 的字段骨架是一个独立约束面，开发者调 loop 时会直接看它。 |
| PR Triage | `starters/pr-babysitter/.codex/skills/pr-review-triage/SKILL.md` | triage 是 loop 第一步，且 skill 文件本身就是接口契约。 |
| minimal-fix | `templates/SKILL.md.minimal-fix` | 这里建模的是共享 implementer 契约，不是假设 starter 里已经有本地副本。 |
| verifier.toml | `starters/pr-babysitter/.codex/agents/verifier.toml` | 这是 repo-local checker 入口，最适合直接显示在“涉及代码”栏。 |
| Verifier Template | `templates/SKILL.md.verifier` | 用来解释 verifier 的共享规则来源，以及 CLI fallback 的合成来源。 |
| loop-init CLI | `tools/loop-init/src/cli.ts` | 所有 starter/state/template 补齐逻辑都收敛在这一个 CLI 文件里，单文件锚点最清晰。 |

## 关键证据

- `patterns/registry.yaml:5-24`：声明 `pr-babysitter` 的 `skills`、`state`、`phases`、`human_gates`、`starter` 和 `early_exit_required`。
- `patterns/pr-babysitter.md:13-17,35-56,92`：给出 required skills、典型循环步骤、verification strategy，以及 `Worktree + minimal-fix + verifier` 的 L2 fix attempt。
- `examples/codex/pr-babysitter.md:7-21`：把 `pr-review-triage`、`update pr-babysitter-state.md`、`minimal-fix`、`verifier must APPROVE`、`do not merge` 写成 Codex 自动化主提示词。
- `starters/pr-babysitter/README.md:3-20,33-36`：给出 `loop-init` / manual copy、starter `/loop` 命令，以及 `No auto-merge` 与 denylist。
- `starters/pr-babysitter/LOOP.md:5-16`：固定 cadence、watched 规则、3 次尝试上限和 human gates。
- `starters/pr-babysitter/pr-babysitter-state.md.example:1-19`：定义 watched PR 条目、attempts、last action、human decision、run log。
- `starters/pr-babysitter/.codex/skills/pr-review-triage/SKILL.md:13-29`：定义 triage 输出结构、suggested action，以及 ready-to-merge / 高风险升级规则。
- `starters/pr-babysitter/.codex/agents/verifier.toml:1-13`：给出 repo-local checker 的默认 REJECT、scope/intent/tests/no cheating/risk 检查项。
- `templates/SKILL.md.minimal-fix:14-45`：给出 minimal-fix 的输入、最小变更流程、>5 文件升级和“verifier decides”规则。
- `templates/SKILL.md.verifier:14-47`：给出共享 verifier checklist、verdict 枚举，以及不能跑测试时的升级策略。
- `tools/loop-init/src/cli.ts:22-24,40-49,116-179,267-270,359-408`：证明 `pr-babysitter` starter 映射、needs-fix 模式补齐、Codex 启动命令，以及 state/LOOP/skills/agents 的复制流程都在 CLI 内。

## 拆分与省略

- `Verifier` 拆分为 `verifier.toml` 和 `Verifier Template`，是因为开发者排查时会区分“本仓里到底加载了哪个 agent 文件”和“共享模板原文是什么”。
- 没有把 `starters/pr-babysitter/.codex/` 整个目录塞进一个卡片。那会让开发视图退化成目录树，失去“首开文件”粒度。
- 没有把 GitHub connector、PR 评论线程、CI job 明细拉进来；这些更偏 runtime/use-case，而不是当前开发视图的代码边界。
- 没有把 `rebase-and-clean` 加进主图。它确实是模式的一部分，但不是本轮用户点名证据集里的核心主链。

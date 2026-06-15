# 用例视图证据与假设

## 本轮收敛结论

本轮把原先“7 个 pattern = 7 个顶级主用例”的结构收敛为两个主 case：

1. `定义 Loop`
2. `执行 Loop`

这样收敛的理由是：本仓库的主叙事不是卖 7 个互不相干的产品，而是教采用者先把一条 loop 设计好，再把它接到具体运行面上持续执行。

## 为什么 `定义 Loop` 是一个独立主 case

以下证据共同说明，仓库把 pattern 选择、脚手架、状态配置、预算配置、readiness 审计、成本估算、升级边界与安全门禁视为同一个“定义/配置 loop”的能力面：

| 证据文件 | 关键含义 |
| --- | --- |
| `README.md` | Quick Links 和 Getting Started 明确给出 `Pattern Picker → loop-init → loop-cost → loop-audit → start report-only` 的采用顺序。 |
| `docs/pattern-picker.md` | 先按症状挑选 pattern，再估算成本、决定 cadence 与 first loop，说明“选模式”属于定义阶段。 |
| `docs/loop-design-checklist.md` | purpose、cadence、skills、maker/checker、state、connectors、cost、safety 被建模成一整套设计清单。 |
| `starters/README.md` | starter 不是运行结果，而是把 Grok / Claude / Codex 的 loop 骨架复制进目标仓库。 |
| `tools/loop-init/README.md` | 直接把脚手架职责写成 pattern/tool 初始化。 |
| `tools/loop-init/src/cli.ts` | 代码会复制 skills/agents、写入 state file、LOOP.md、`loop-budget.md`、`loop-run-log.md`，并输出 first-loop command。 |
| `tools/loop-cost/README.md` | cadence 与 level 的 token 成本在真正开跑前就需要估算。 |
| `tools/loop-audit/README.md` | readiness 被显式量化为 L0-L3，并要求 activity proof、budget、run log、verifier 等条件。 |

所以这次不再把 `配置 Loop`、`审计预算`、`接入自动化` 拆成多个并列主用例，而是合并到 `定义 Loop` 这个更贴近采用者心智模型的主能力下。

## 为什么 `执行 Loop` 是另一个主 case

以下证据说明，仓库真正要“跑起来”的能力，是在定义完成后按 pattern 和 cadence 持续执行 loop：

| 证据文件 | 关键含义 |
| --- | --- |
| `patterns/README.md` | 7 个 pattern 被组织为可复用运行模式，并给出 `pick → scaffold → scheduling → week one → audit` 的落地顺序。 |
| `patterns/registry.yaml` | 7 个 pattern 统一具有 `goal/cadence/tools/skills/state/phases/starter/week_one_mode/cost` 元数据，更像同一执行能力下的配置档，而不是 7 个独立产品。 |
| `README.md` Patterns 表 | README 顶层就把 Daily Triage、PR Babysitter、CI Sweeper、Dependency Sweeper、Changelog Drafter、Post-Merge Cleanup、Issue Triage 作为运行模式公开。 |

因此 7 个 pattern 仍然很重要，但它们更适合作为 `执行 Loop` 的子类型或运行模式，而不是 7 个顶级 P0 行。

## `执行 Loop` 具体“运行在哪里”

这是本轮需要特别说清楚的点。证据链如下：

| 运行面 | 证据 | 说明 |
| --- | --- | --- |
| Grok `/loop` | `docs/primitives.md`、`examples/grok/README.md`、`starters/minimal-loop/README.md` | Grok 把 `/loop` 作为原生调度入口，Daily Triage 等 pattern 可直接按 cadence 运行。 |
| Claude Code `/loop` | `docs/primitives.md`、`examples/claude-code/daily-triage.md`、`starters/minimal-loop-claude/README.md` | Claude 版本同样通过 `/loop 1d ...` 运行，只是 skill/agent 放在 `.claude/`。 |
| Codex Automations | `docs/primitives.md`、`examples/codex/daily-triage.md`、`starters/minimal-loop-codex/README.md` | Codex 要在 Automations tab 配 cadence、environment、prompt，然后周期性运行 triage/fix/verifier。 |
| GitHub Actions / CI automation | `examples/github-actions/README.md` | Actions 负责 `schedule`、`workflow_run`、`push` 等触发，再在 “Invoke agent” 步骤接上 Codex CLI/API、`repository_dispatch` 或自定义 harness。 |

所以 `执行 Loop` 的准确表达不是“仓库内部自己跑一套统一 runtime”，而是：

- 仓库提供 pattern、starter、state 约定与示例接线
- 使用者把它接到 Grok `/loop`、Claude `/loop`、Codex automation、GitHub Actions 或其他 scheduler/harness
- 然后按 pattern 对应的 cadence 或事件触发持续执行

## 7 个 pattern 在本版里的落点

本版没有删除它们，只是不再让它们喧宾夺主。它们都被吸收到 `执行 Loop` 的 summary、entry surfaces 和证据说明里：

- `Daily Triage`
- `PR Babysitter`
- `CI Sweeper`
- `Dependency Sweeper`
- `Changelog Drafter`
- `Post-Merge Cleanup`
- `Issue Triage`

理由是这些模式对用户来说，差异主要体现在：

- 观察对象不同
- cadence 不同
- 风险门禁不同
- starter / skills / state file 不同

但它们共享同一个更高层用户目标：让一条已经定义好的 loop 在某个运行面上反复执行。

## 辅助 case 的保留逻辑

本版保留了几个低于主 case 的辅助能力：

| 用例 | 证据 | 保留原因 |
| --- | --- | --- |
| `复盘与升级` | `docs/operating-loops.md`、`tools/loop-audit/src/auditor.ts` | 运行后必须根据 budget、run log、activity、false positive 决定升降级与暂停。 |
| `治理模式库` | `CONTRIBUTING.md`、`patterns/registry.yaml`、`scripts/validate-registry.mjs` | 仓库维护者要长期维护 pattern/starter/registry/tooling 一致性。 |
| `发布工具链` | `docs/RELEASE.md`、`tools/*/README.md` | `loop-init`、`loop-audit`、`loop-cost` 是定义能力的重要供给面，但它们属于维护者职责，不应压过主用例。 |

## 本轮明确假设

1. `定义 Loop` 和 `执行 Loop` 都是用户可直接感知的主能力，因此保留为 `P0`。
2. `复盘与升级` 虽与定义阶段相连，但更接近运行后的控制闭环，因此保留为 `P1` 辅助用例。
3. `治理模式库` 与 `发布工具链` 主要面向仓库维护者，属于 `P2`。
4. `Issue Triage` 虽然 starter 仍复用 `minimal-loop`，但在 registry 与 README 中已经是一等 pattern，因此继续归入 `执行 Loop` 的运行模式集合。

## 本轮明确省略

- 不渲染 draw.io，不输出截图。
- 不把 `minimal-fix`、`loop-verifier`、`loop-budget` 单独升级成主用例。
- 不按 Grok / Claude / Codex / GitHub Actions 各拆一套平行用例树；这些更适合表达为 `执行 Loop` 的运行面。

# UC02 PR Babysitter Development View - Evidence / Assumptions

## Scope

- 只建模让 Codex PR Babysitter loop 跑起来所需的 developer-facing 单元：模式注册、模式说明、Codex prompt、starter 文档与配置、state schema、triage skill、minimal-fix/verifier 契约、loop-init 脚手架。
- 不建模 GitHub 运行时 sequence、PR/CI 实例数据、评论线程、MCP 连接器调用细节。

## Key Modeling Judgments

1. **把 `examples/codex/pr-babysitter.md` 视为核心入口，而不是附属示例。**  
   这里直接写出了 Codex Automations 的 cadence、watched PR 选择条件、`attempts < 3` gate、`Open worktree`、`$minimal-fix`、`Verifier subagent: must APPROVE`、`Comment on PR with proposal - do not merge`。对“到底 prompt 写了什么”这个问题，它是最直接证据。

2. **把 `starters/pr-babysitter/LOOP.md` 视为与 prompt 并列的配置面。**  
   它没有重复写执行步骤，但把 cadence、`Max fix attempts per PR: 3`、`Watched: PRs authored by team / label loop-watch`、`Auto-merge: disabled`、human gates 固化成 repo 级配置边界，所以 development view 里单独成一个节点。

3. **把 `pr-babysitter-state.md.example` 视为 loop 的外部状态 schema，而不是普通文档。**  
   证据里能看到它明确承载 `Status`、`Attempts: 0/3`、`Last action`、`Human decision`、`Run log`。这正是 triage/fix/verify 后需要持续更新的控制面。

4. **把 `pr-review-triage` -> `minimal-fix` -> `verifier` 画成核心开发依赖链。**  
   `pr-review-triage` 给出 `Suggested loop action`；`minimal-fix` 限制 implementer 只能做 smallest diff；`verifier` 作为 checker 输出 `APPROVE | REJECT | ESCALATE_HUMAN`。这条链解释了 loop 为什么不会直接失控改代码。

5. **把 `loop-init` 单独成节点，而不是埋在 README 注释里。**  
   因为 `tools/loop-init/src/cli.ts` 不只是文档提到的命令，它真实编码了：`pr-babysitter` 属于 `PATTERNS_NEEDING_FIX`，会复制 starter 资产，并在 Codex 场景补齐 `SKILL.md.minimal-fix` 和 `verifier.toml` fallback。

## Evidence Highlights

- `patterns/registry.yaml:5-24`
  - PR Babysitter 元数据条目：`cadence: 5m-15m`、`skills: [pr-review-triage, minimal-fix, rebase-and-clean]`、`state: pr-babysitter-state.md`、`human_gates: [security, payments, auth, max-fix-attempts]`、`starter: starters/pr-babysitter`、`early_exit_required: true`

- `examples/codex/pr-babysitter.md:13-21`
  - 直接给出 Codex Prompt Template：
    - watched PR 条件：`team-authored or label loop-watch`
    - 先 `Run $pr-review-triage`
    - 再 `Update pr-babysitter-state.md`
    - 条件命中且 `attempts < 3` 时：`Open worktree` -> `Implementer: $minimal-fix` -> `Verifier subagent: must APPROVE` -> `Comment on PR with proposal - do not merge`

- `starters/pr-babysitter/README.md:20`
  - starter 启动命令把关键治理文案写死在操作入口：
    - `allowlisted PRs`
    - `worktree + minimal-fix + loop-verifier`
    - `Never merge - propose only`
    - `Escalate after 3 attempts per PR`

- `starters/pr-babysitter/LOOP.md:9-16`
  - repo 内配置边界：
    - `Max fix attempts per PR: 3`
    - `Auto-merge: disabled`
    - `Watched: PRs authored by team / label loop-watch`
    - Human gates 包括 `Security, auth, payments, infrastructure` 和 `PRs with >10 files changed in loop fix`

- `starters/pr-babysitter/.codex/skills/pr-review-triage/SKILL.md:20-29`
  - triage 决策输出与升级规则：
    - `Suggested loop action: none | minimal-fix | rebase | escalate-human`
    - `Ready to merge` 需要 required checks + approvals
    - 高风险 labels 一律 `escalate-human`

- `templates/SKILL.md.minimal-fix:19-45`
  - implementer 约束：
    - denylist：`.env`, `auth/`, `payments/`, secrets
    - `Change only what is required`
    - `Run tests/lint relevant to the change`
    - `>5 files or design change -> stop and escalate`
    - `verifier decides`

- `starters/pr-babysitter/.codex/agents/verifier.toml:2-13`
  - checker 约束：
    - `Default stance: REJECT until proven otherwise`
    - checklist 包括 scope/tests/no cheating/risk
    - verdict 固定为 `APPROVE | REJECT | ESCALATE_HUMAN`

- `tools/loop-init/src/cli.ts:116-179`
  - scaffolding 逻辑：
    - `copyTemplateSkill(... 'SKILL.md.minimal-fix' ...)`
    - Codex verifier 缺失时 `copyTemplateVerifier()` 用 `templates/SKILL.md.verifier` 生成 `verifier.toml`

## Omissions

- **未纳入 `rebase-and-clean` 节点。**  
  它在 `patterns/pr-babysitter.md` 与 `patterns/registry.yaml` 中被列为 required skill，但用户这轮关注的是“让 agent loop 起来自主 triage/fix/verify 的 prompt 与规则”，而点名证据文件也没有对应 Codex starter 资产，因此从核心开发链中省略，并在此说明。

- **未纳入 GitHub MCP connector 与评论 API 细节。**  
  `examples/codex/pr-babysitter.md` 提到 GitHub MCP connector，但这是运行时集成点，不是本 development view 要画的代码/提示词/配置模块。

- **未纳入 `.grok` / `.claude` 变体。**  
  这些变体存在于 starter 目录，但本任务明确要打穿 Codex Automations 场景，所以 development view 只保留 `.codex` 资产和共享模板。

## Uncertainties / Caveats

1. **`starters/pr-babysitter/.codex/skills/minimal-fix/SKILL.md` 不存在。**  
   这是本轮最重要的缺口。development view 因此把 `templates/SKILL.md.minimal-fix` 视为有效契约来源，并通过 `loop-init CLI` 建模它是如何被补齐进目标仓库的。

2. **`allowlisted PRs` 没有独立配置文件。**  
   README 的 starter 命令有这个词，但 inspected files 里没有单独 allowlist manifest。当前最接近的可落地选择器是：
   - `examples/codex/pr-babysitter.md` 的 `team-authored or label loop-watch`
   - `starters/pr-babysitter/LOOP.md` 的 `Watched: PRs authored by team / label loop-watch`
   所以视图把 allowlist 视为 prompt/config 规则，而非独立节点。

3. **starter verifier 与 template verifier 来源不同。**  
   starter 已自带一个内联指令版 `verifier.toml`；`loop-init` 的 Codex fallback 则会从 `templates/SKILL.md.verifier` 合成 verifier。两者语义一致，但不是“starter 直接引用 template”的关系，因此图里用“同一 verifier contract、两种来源”来表示。

4. **`README.md` 的 Quick Start 对 Grok 更直接。**  
   `README.md` 的命令示例以 `--tool grok` 和 `.grok/skills/*` 为主，但 target repo 同时确实存在 `.codex/skills/pr-review-triage/SKILL.md` 与 `.codex/agents/verifier.toml`，所以本视图仍把 README 视为 starter 总入口，而把 Codex 具体 prompt 细节交给 `examples/codex/pr-babysitter.md`。

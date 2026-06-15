# PR Babysitter Runtime 证据与假设

## 建模范围

本文件只支撑一张具体 runtime scene：

- 运行面：Codex Automations
- 模式：PR Babysitter
- 目标：画清楚一次定时 tick 如何触发一个主 Agent run，主 run 如何基于 state、GitHub、triage、minimal-fix、verifier 与 LOOP 限制决定是否进入 worktree，并最终止于评论、状态回写与人工门禁。

我没有复用现有 `runtime-view.json` 的 UC02 全景模型，因为用户要求的是把 Codex Automations 下的 PR Babysitter 场景打穿，而不是再次画四种运行面的并列总览。

## 关键证据

### 1. 定时器先触发一个主 Agent run

直接证据：

- `examples/codex/pr-babysitter.md:7-8`
  - cadence 是 `Every 5–15 minutes (working hours)`。
- `examples/codex/pr-babysitter.md:13-22`
  - prompt template 是一段单一 run 要执行的步骤：先 `Run $pr-review-triage`，再 `Update pr-babysitter-state.md`，然后才进入条件分支。
- `examples/codex/pr-babysitter.md:25-38`
  - subagents 与 GitHub connector 是单独列出的能力依赖，不是 automation 的一级触发项。

建模判断：

- 图里把 `Codex Automations -> 主 Agent run` 画成一条单独关系，而且标记为 `inferred: true`。
- 这是受约束推断，不是臆造：
  - 仓库没有公开 Codex Automations 内部 runtime 实现；
  - 但示例文案明显是“每次定时执行一段主 prompt”，而不是“定时器同时直接调用 triage、implementer、verifier 三个并行 agent”。

因此必须在图上表达：

1. 定时器只起一个主 run。
2. 子 agent / worktree 是主 run 的条件性派生。

### 2. 主 run 决策前必须结合 state 与 GitHub

直接证据：

- `starters/pr-babysitter/pr-babysitter-state.md.example:3-19`
  - state 文件里有 `Attempts`、`Last action`、`Human decision`、`Escalated`、`Resolved`、`Run log`。
- `examples/codex/pr-babysitter.md:15-22`
  - prompt 先 triage、更新 state，再按 `attempts < 3` 与 `high-risk labels` 分叉。
- `examples/codex/pr-babysitter.md:38`
  - GitHub MCP connector 用来 `list PRs, read checks, and post comments`。
- `starters/pr-babysitter/.codex/skills/pr-review-triage/SKILL.md:16-29`
  - triage 输出 CI、reviews、blocking comments、ready to merge、suggested loop action，并规定高风险 label 直接 `escalate-human`。

建模判断：

- 主 run 先读 `pr-babysitter-state.md`，再读 `GitHub PR / CI / Review`，然后才调用 `pr-review-triage`。
- 其中“读取 state”这条边也标记为 `inferred: true`，因为仓库给的是 state 结构和 prompt 条件，而不是可执行源码；但从 `attempts < 3`、`Human decision` 这些字段看，不读取 state 就无法实现模板里的条件判断。

### 3. worktree、implementer、verifier 只在条件满足后出现

直接证据：

- `examples/codex/pr-babysitter.md:17-22`
  - 只有在 `CI red or actionable review comment AND attempts < 3` 时，才：
    - `Open worktree`
    - `Implementer: $minimal-fix`
    - `Verifier subagent: must APPROVE`
    - `Comment on PR with proposal — do not merge`
- `patterns/pr-babysitter.md:39-45`
  - CI red 时 spawn minimal-fix；review comments actionable 时 propose minimal patches；高风险则 human。
- `patterns/pr-babysitter.md:49-54`
  - implementer 不能自证完成；必须由独立 verifier 明确确认 scope / intent / tests；loop 只 propose，人来 merge。
- `patterns/pr-babysitter.md:58-61`
  - 多次修复无进展、高风险领域都要 handoff。
- `starters/pr-babysitter/README.md:20`
  - starter 命令再次把 `worktree + minimal-fix + loop-verifier`、`Never merge`、`Escalate after 3 attempts per PR` 写死。

建模判断：

- `主 Agent run -> worktree -> implementer -> verifier` 是主路径里的条件性动作链。
- worktree、implementer、verifier 不是 automation 的并列触发对象。
- verifier 返回 `APPROVE` 才进入“评论修复提案”这条主线。

### 4. implementer 采用模板技能约束，不假装 starter 内已有 Codex 版 minimal-fix

直接证据：

- `patterns/registry.yaml:11-16`
  - PR Babysitter 的 skills 中包含 `minimal-fix`。
- `templates/SKILL.md.minimal-fix:12-45`
  - 明确 smallest diff、相关测试、denylist、超过 5 文件或设计变更即升级。

缺口证据：

- `starters/pr-babysitter/.codex/skills/minimal-fix/SKILL.md`
  - 实际不存在。

建模判断：

- 图中仍保留 `Implementer ($minimal-fix)` 参与者，因为示例 prompt 与 registry 都要求它存在。
- 但证据说明里明确写出：
  - Codex starter 目录缺少对应 skill 文件；
  - implementer 运行约束只能回落到 `templates/SKILL.md.minimal-fix`。

这不是小问题，所以我把它列为 unresolved uncertainty，而不是悄悄补成“仓库里已经有 Codex minimal-fix skill”。

### 5. verifier 是独立 checker，不实现修复

直接证据：

- `starters/pr-babysitter/.codex/agents/verifier.toml:1-15`
  - `Never implements fixes`
  - 默认 `REJECT`
  - 必须检查 scope、intent、tests、no cheating、risk
  - 输出 `APPROVE | REJECT | ESCALATE_HUMAN`
- `templates/SKILL.md.verifier:12-48`
  - 强化同一 maker/checker 约束：reject unless evidence is strong、自己跑 tests、不能信 implementer 自报通过、不能跑就 escalate。

建模判断：

- 图里 `verifier -> 主 Agent run` 分成两条关系：
  - `返回 APPROVE`
  - `返回 REJECT / 升级`
- 这样可以把“通过后评论提案”和“拒绝后评论升级”拆成不同分支，不把 verdict 混成一句泛泛的“返回结果”。

### 6. 终点只到 PR 评论、状态回写、人工门禁，绝不自动 merge

直接证据：

- `examples/codex/pr-babysitter.md:21-22`
  - `Comment on PR with proposal — do not merge`
  - `If attempts >= 3 or high-risk labels: Triage inbox + escalate`
- `starters/pr-babysitter/README.md:20-23`
  - `Never merge — propose only`
  - `Sign PR comments`
- `starters/pr-babysitter/README.md:35`
  - `No auto-merge by default`
- `starters/pr-babysitter/LOOP.md:9-16`
  - `Max fix attempts per PR: 3`
  - `Auto-merge: disabled`
  - human gates 包括 security/auth/payments/infrastructure 与 `>10 files changed`
- `patterns/pr-babysitter.md:54`
  - `The loop only proposes; a human actually merges.`

建模判断：

- 图里 outcome 被拆成两个参与者：
  - `PR 评论 / 升级通知`
  - `人工审阅 / 合并`
- 没有任何 `auto-merge`、`merge PR`、`push merge button` 之类的参与者或关系。
- 这不是省略，而是本场景的硬约束。

## 为什么没有画的内容

### 1. 没画 rebase-and-clean

原因：

- `patterns/pr-babysitter.md:15-17` 把它列为 required skill。
- 但用户这次明确要求聚焦：
  - `pr-babysitter-state.md`
  - `GitHub PR/CI/Review`
  - `pr-review-triage`
  - `minimal-fix`
  - `verifier.toml`
  - `LOOP.md`
- Codex 示例 prompt 里也没有把 rebase-and-clean 放进这条具体动作链。

所以本图不把 rebase path 画进来，避免把“存在于 pattern 列表里”和“这个具体 Codex 场景明确执行”混为一谈。

### 2. 没画 ready-to-merge label

原因：

- `patterns/pr-babysitter.md:42` 提到 ready 时可以加 `"ready to merge" label or ping human`。
- 但用户此次要求的落点是“最终只评论/回写状态/升级人工，绝不自动 merge”。
- Codex 示例本身也强调的是 `Comment on PR with proposal — do not merge`。

因此我把 ready-to-merge label 视为本图范围外的次要 outcome，没有强行并入。

## unresolved uncertainty

1. `Codex Automations -> 主 Agent run` 是受约束推断，不是仓库内可执行实现；若后续拿到 Codex automation runtime 文档，可能需要把这条边从 `inferred` 改成显式实现边。
2. `Triage inbox + escalate` 在当前仓库里没有更细的 Codex UI 证据，因此结果面被收敛为 `PR 评论 / 升级通知`；如果后续补到 inbox 结构，可把 outcome lane 再拆细。
3. `starters/pr-babysitter/.codex/skills/minimal-fix/SKILL.md` 缺失；当前 implementer 约束只能来自模板技能文件，而不是 starter 自带实现。

## 最终建模判断

这张图最核心的判断只有两条：

1. `Codex Automations` 不是直接触发多个 agent，而是定时触发一个主 Agent run。
2. `worktree / implementer / verifier` 都是主 run 在 triage 命中、attempts 未超限、且未踩 human gate 时才派生出来的条件分支；无论分支结果如何，闭环都止于 PR 评论、state 回写与人工门禁，不会自动 merge。

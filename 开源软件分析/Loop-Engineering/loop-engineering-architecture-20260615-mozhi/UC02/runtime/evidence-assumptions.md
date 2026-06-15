# UC02 Runtime 证据与假设

## 结论先说

UC02「执行 Loop」在这个仓库里不是“进入某个统一 runtime controller”，而是：

1. 先由不同运行面触发执行
2. 再装载同一套 loop 合约
3. 由 agent/harness 执行 triage 或小修复
4. 可选地进入 verifier/worktree 分支
5. 最后把结果写回 STATE / budget / run-log，并暴露给人工复核

因此本轮 runtime 中间模型选择了 4 条主路径：

- Grok `/loop`
- Claude Code `/loop`
- Codex Automations
- GitHub Actions

而不是按目录、工具包或 7 个 pattern 各自拆成 7 套运行时图。

## 直接证据（代码 / 文档直接支持）

### 1. 入口面与触发方式

- `docs/primitives.md`
  - 直接列出 `/loop`、Claude scheduled tasks、GitHub Actions + `repository_dispatch`、custom harness。
  - 这是“有哪些运行面”的顶层证据。

- `examples/grok/README.md`
  - 把 Grok 的原生 primitives 说成 `/loop`、scheduler、skills、MCP、sub-agents。
  - 支撑 Grok `/loop` 是 UC02 的真实入口面。

- `examples/claude-code/daily-triage.md`
  - 直接给出 Claude `/loop 1d ...` 命令。
  - 支撑 Claude Code 路径。

- `examples/codex/daily-triage.md`
  - 直接要求在 Codex `Automations` tab 配 cadence、environment、prompt。
  - 支撑 Codex Automations 路径。

- `examples/github-actions/README.md`
  - 明说 event-driven / scheduled loops 没有 TUI session，要在 workflow 中 gather context、update state、delegate to your agent harness。
  - 支撑 GitHub Actions 路径。

- `examples/github-actions/daily-triage.yml`
  - 直接给出 `schedule`、`workflow_dispatch`、gather context、ensure `STATE.md` exists、upload artifact 等步骤。
  - 这是 GitHub Actions runtime path 最硬的代码级证据。

### 2. 共享的 runtime 合约

- `patterns/registry.yaml`
  - pattern 被统一建模为 `tools`、`skills`、`state`、`phases`、`human_gates`、`starter`、`week_one_mode`、`token_cost`。
  - 说明不同 loop 运行时共享的是同一套“模式元数据 + 合约”，而不是各玩各的。

- `tools/loop-init/src/cli.ts`
  - 会复制 `STATE.md`、`LOOP.md`、skills、verifier、`loop-budget.md`、`loop-run-log.md`。
  - 还会生成各运行面的 first loop command。
  - 说明仓库把运行时知识固化在 starter/skills/LOOP 约定里。

- `LOOP.md`
  - 把 active loops、cadence、state、worktrees、connectors、budget、run history、kill switch 写成统一操作规则。
  - 这是“生命周期 owner 在哪里”的直接证据之一。

### 3. 执行、校验、状态回写

- `examples/grok/daily-triage.md`
  - 直接写明 triage 后可打开 isolated worktree，跑 minimal-fix，再交 reviewer sub-agent 验证，并更新 `STATE.md`。

- `examples/claude-code/daily-triage.md`
  - 直接写明 implementer(worktree) -> verifier -> 更新 `STATE.md` -> 升级模糊项。

- `examples/codex/daily-triage.md`
  - 直接写明 high-priority single-file bugfix -> isolated worktree -> verifier subagent。
  - 也直接给出 `STATE.md` 更新规则与 `Triage inbox` 结果面。

- `docs/operating-loops.md`
  - 直接规定 `loop-budget.md`、`loop-run-log.md`、kill switch、L1/L2/L3 升级、暂停条件。
  - 支撑“校验 / 状态 / 预算”必须是 runtime 视图里的显式参与者。

- `tools/loop-audit/src/auditor.ts`
  - 把 state file、`LOOP.md`、skills、verifier、workflows、budget doc、run log、真实 activity 当成 readiness 运行信号。
  - 说明这些不是静态文档，而是 runtime 生命周期的控制面。

## 推断部分（已在 JSON 中标记 inferred）

### 1. `GitHub Actions -> Loop 合约`

为什么是推断：

- `daily-triage.yml` 的 “Run triage agent” 仍是占位注释，没有真实 CLI 命令。
- `examples/github-actions/README.md` 只告诉你“换成 Codex CLI / API、repository_dispatch、custom harness”，没有给出统一实现。

为什么仍然要建模：

- UC02 要解释“workflow 触发后，loop 怎么真正跑起来”。
- 如果不补这层，就只剩“workflow 收集上下文并上传 artifact”，解释不了 loop 执行本身。

因此本轮把这条边建模为：

- `GitHub Actions -> Loop 合约`：本机 CLI / 脚本调用（`inferred: true`）

### 2. `外部 runner / dispatch 接收端 -> Loop 合约`

为什么是推断：

- 仓库没有外部 runner 的源码或协议实现。
- 只有 `repository_dispatch` 作为 wiring 选项被文档显式提到。

为什么仍然保留：

- 这是唯一能解释“GitHub Actions 只负责触发，真正执行发生在别处”的边界跨越。
- 用户任务明确要求覆盖 `repository_dispatch / Codex CLI / custom harness`。

### 3. `Verifier / Worktree 分支 -> STATE / budget / run-log`

为什么是推断：

- 文档反复说 verifier 存在、worktree 存在、run log/budget 要记录，但没有一处统一源码把“verifier verdict 怎么写回账本”写死。
- 不同运行面也可能把 verdict 写进 `STATE.md`、PR 评论、artifact、run log，形式不完全一样。

为什么仍然建模：

- 如果 verifier 只被画成一次“校验”而不回流到状态面，运行闭环就断了。
- `operating-loops.md` 和 `loop-audit` 都把 run log / budget / activity 当成 readiness 的一部分，因此 verifier 结果回流到这些持久面是合理且必要的架构推断。

## 为什么没有统一 runtime controller

这是本轮最重要的限制。

仓库里没有看到一个统一托管下面职责的控制器实现：

- 接收 Grok / Claude / Codex / GitHub Actions 的所有事件
- 统一装载 pattern
- 统一调度 triage/fix/verifier
- 统一管理 state/budget/run-log 写回

相反，仓库给出的是：

- pattern registry
- starter 目录
- `LOOP.md`
- skills / verifier 模板
- `loop-init`
- `loop-audit`
- GitHub Actions wiring 示例
- 各工具的示例 prompt / command

所以本轮 runtime view 把 `Loop 合约（pattern / starter / skills）` 抽象成一个共享参与者，而不是声称仓库里存在某个单体 runtime 服务。

## 本轮省略

- 不单独为 7 个 pattern 各画一条完整运行路径。
- 不展开 MCP connector 的每个外部系统。
- 不展开 Codex Triage inbox、Actions artifact、PR 评论、Issue 评论的具体 UI/协议差异，只抽象为一个“反馈面”。
- 不展开供应商产品内部的 scheduler/session/runtime 实现。

## 哪些不确定性仍可能影响后续渲染

1. GitHub Actions 主路径里，“本机 CLI / 脚本调用”与“repository_dispatch 外派”哪个应作为视觉主线，取决于主代理更想强调 repo 内还是 repo 外责任边界。
2. `反馈面` 目前是抽象参与者；若主代理后续想把 Codex Triage inbox 与 Actions artifact 分开画，需要把 outcome lane 再拆细。
3. `Verifier / Worktree 分支` 现在作为所有路径共享的条件分支；若后续只想表现 L1 report-only，则可以在渲染前把该分支折叠掉。

# UC01 Runtime 证据与假设

## 本轮建模结论

`定义 Loop` 不是一个隐藏在仓库内部的单体 runtime，而是采用者手动驱动的三段协作：

1. 在 `README` / `pattern-picker` / `loop-design-checklist` 上做选型与 rollout 设计
2. 用 `loop-init` 把 starter、state、budget、run-log、verifier 与 first-loop command 落到目标工作区
3. 用 `loop-cost` / `loop-audit` 形成成本与 readiness 反馈，再把升级边界、human gates、pause/kill 规则补回工作区

所以运行视图必须讲“一次定义 Loop 如何发生”，而不是把 `tools/`、`starters/`、`docs/` 画成静态模块图。

## 为什么拆成三条主路径

### 1. 人工选型与边界设计

这一段的生命周期 owner 不是某个后台进程，而是文档决策面：

- `README.md` 给出采用顺序：`Pattern Picker -> loop-init -> loop-cost -> loop-audit -> start report-only`
- `docs/pattern-picker.md` 负责把“症状 -> pattern -> cadence / 成本 / first loop”串起来
- `docs/loop-design-checklist.md` 和 `docs/operating-loops.md` 负责把 L1/L2/L3、maker/checker、state、MCP、cost、pause/kill、safety 变成显式门禁
- `stories/l1-to-l2-graduation.md` 把 L1 先校准、verifier/worktree 先人工验证、`loop-audit >= 58` 再升 L2 的经验门槛写清楚

因此第一条 path 的重点不是“哪个代码模块调用哪个模块”，而是“采用者如何先把 pattern、tool、week-one mode、升级边界设计清楚”。

### 2. `loop-init` 脚手架路径

第二条 path 的 owner 很明确，就是 `tools/loop-init/src/cli.ts`。

证据点：

- `PATTERN_STARTERS` / `STATE_FILES` / `PATTERN_BUDGET` 把 pattern 对应的 starter、state 文件与预算骨架静态编码出来
- `copyTemplateVerifier`、`copyL2Templates`、`scaffoldObservability` 会复制 verifier、budget skill、`loop-budget.md`、`loop-run-log.md`
- `firstLoopCommand` 会按 pattern + tool 回首条运行命令
- `main()` 最后打印 next steps：先跑 `loop-audit`、再跑 `loop-cost`、再按 first-loop command 接到外部运行面

这说明 `loop-init` 真正做的是“定义阶段脚手架”，不是运行 loop 本身。

## 3. 成本估算与 readiness 反馈

这一段是两个并列工具，不是一个统一控制器里的两个子步骤：

- `loop-cost` 读取 `registry.json` 或 `patterns/registry.yaml`
- `estimator.ts` 把 cadence、L1/L2/L3、early-exit、worst-case 与 realistic blend 编成成本模型
- `loop-audit` 扫目标工作区里的 state、skills、verifier、budget、run-log、activity，并给出 score / level / recommendations
- `auditor.ts` 明确把 `budgetDoc + runLog + LOOP.md budget + loopActivity` 作为 L3 的门槛条件

所以第三条 path 不是“cost 调 audit”或“audit 调 cost”，而是采用者分别运行两个反馈工具，再把结果写回工作区配置。

## 为什么把工作区当成核心参与者

UC01 的产物不是一份口头建议，而是一组真正写进目标仓库的可运行骨架：

- `STATE.md` 或 pattern-specific state
- `LOOP.md`
- `.codex/.claude/.grok` 下的 triage skill / verifier
- `loop-budget.md`
- `loop-run-log.md`
- `AGENTS.md`（如缺失）

而且 pause / kill / budget / activity proof 也都依赖这些文件存在并被后续 loop 消费。所以工作区不是被动结果页，而是定义阶段的状态边界。

## 明确不确定性

### 没有统一 runtime controller

仓库没有一个“Define Loop Controller”统一调度文档、starter、cost、audit。

真实情况是：

- 文档提供决策与规则
- `loop-init` 负责脚手架
- `loop-cost` 负责估算
- `loop-audit` 负责 readiness gating
- 人类采用者负责把这些动作串起来

因此我没有编造一个不存在的 orchestrator 节点。

### GitHub Actions 只是后续接线面

`examples/github-actions/README.md` 明确写的是：

- workflow 负责 gather context / update state
- “Invoke agent” 这一步需要用户自己替换成 Codex CLI / API、`repository_dispatch` 或外部 runner

所以 Actions 在本图里只能作为“后续运行面”分支，而不能冒充 UC01 的生命周期 owner。

### `loop-init` 输出的是 first-loop command，不是实际执行

`firstLoopCommand` 和 starter README 会给出：

- Grok / Claude 的 `/loop ...`
- Codex 的 Automation prompt
- 后续可接到 GitHub Actions / harness 的提示

但这些都属于“定义完成后如何开跑”的 handoff，不等于仓库内已经存在一个执行时主循环。

## 本轮明确省略

- 不展开 UC02 的周期执行细节
- 不分别绘制 7 个 pattern 的执行 runtime
- 不把发布/npm/CI dogfood 画进 UC01
- 不渲染 drawio，不产最终报告

# UC02 开发视图证据与假设

## 建模范围

本次只为 UC02「执行 Loop」产出 development view 中间模型，不做 draw.io 渲染，不输出图片。

切片起点严格沿用已有 use-case 结论里的 entry surfaces：

- `patterns/README.md`
- `patterns/registry.yaml`
- `examples/grok/README.md`
- `examples/claude-code/daily-triage.md`
- `examples/codex/daily-triage.md`
- `examples/github-actions/README.md`

在这条线之上，再向代码与脚手架层追到真正实现 UC02 的维护单元。

## 模块切分原则

本轮没有把目录一层层照抄成节点，而是按“开发者会把哪些文件当成同一个维护单元”来折叠：

1. `Pattern Registry`
   - 合并 `patterns/registry.yaml`、`patterns/*.md`、`patterns/README.md`、`patterns/registry.schema.json`、`scripts/validate-registry.mjs`
   - 原因：它们共同定义 UC02 可以跑哪些 loop，以及这些 loop 的 cadence / skills / starter / cost

2. `loop-init CLI`
   - 单列 `tools/loop-init`
   - 原因：它不是静态文档，而是把 pattern 选择翻译成 starter + state + budget + run-log + verifier 布置的装配器

3. `Starter Assets`
   - 合并 `starters/*` 与 `templates/*`
   - 原因：开发者会把它理解为一套 copyable 骨架资产，而不是十几个彼此独立的小模块

4. `Runtime Surface Examples`
   - 合并 `examples/grok`、`examples/claude-code`、`examples/codex`
   - 原因：三者共享同一 loop 语义与状态契约，只是把调度语法和 agent 布置方式写成不同文档

5. `GitHub Actions Harness`
   - 单列 `examples/github-actions`
   - 原因：它是 UC02 的独立运行面，且比交互式 `/loop` 更像可插拔 automation 壳层

6. `Loop Control Contract`
   - 合并 `templates/STATE.md.template`、`templates/loop-budget.md.template`、`templates/loop-run-log.md.template`、`skills/loop-budget/SKILL.md`、`skills/loop-verifier/SKILL.md`、`scripts/append-run-log.mjs`、代表性 `LOOP.md`
   - 原因：这些文件共同定义跨工具共享的状态、预算、run-log、kill switch 和 maker/checker 契约

7. `Audit & Cost CLIs`
   - 合并 `tools/loop-audit` 与 `tools/loop-cost`
   - 原因：二者都在为“这条 loop 能不能持续运行”提供可检查的 guardrail，只是一个偏 readiness，一个偏预算

## 为什么没有继续细拆

- 没把 7 个 pattern 文档拆成 7 个节点：
  development view 关注的是模式定义单元如何被代码和脚手架消费，而不是 pattern 展示目录。

- 没把 Grok / Claude / Codex 各拆成 3 个一级节点：
  它们共享同一 `STATE / verifier / worktree / triage` 契约，差异主要落在文档化的 prompt、目录前缀和调度方式。

- 没把 `loop-budget`、`loop-verifier`、`append-run-log` 各拆成独立节点：
  这些支撑件一起构成“Loop Control Contract”，拆开会把图面变密，但不会明显增强 UC02 的可解释性。

- 没把 `scripts/check-loop-init-sync.mjs`、`scripts/validate-registry.mjs` 单列：
  它们被保留为证据和暴露接口，而不是单独的开发者心智模块。

## 关系判定依据

### 显式关系

以下关系有直接代码或文档证据，因此未标 inferred：

- `loop-init CLI -> Pattern Registry`
  - `tools/loop-init/src/cli.ts`
  - `scripts/check-loop-init-sync.mjs`

- `loop-init CLI -> Starter Assets`
  - `tools/loop-init/src/cli.ts`
  - `tools/loop-init/README.md`

- `loop-init CLI -> Loop Control Contract`
  - `tools/loop-init/src/cli.ts` 会创建 `loop-budget.md`、`loop-run-log.md`，并布置 `loop-budget` / verifier

- `Audit & Cost CLIs -> Pattern Registry`
  - `tools/loop-cost/scripts/bundle-registry.mjs`
  - `tools/loop-audit/src/auditor.ts`

- `Audit & Cost CLIs -> Loop Control Contract`
  - `tools/loop-audit/src/auditor.ts`
  - `tools/loop-cost/src/estimator.ts`

### 推断关系

以下关系保留，但显式标注 `inferred: true`：

1. `GitHub Actions Harness -> Runtime Surface Examples`
   - 仓库没有一个统一的可 import runtime，把交互式 `/loop` 和 Actions 绑定在一套代码里
   - 但 `docs/primitives.md`、`examples/README.md`、`examples/github-actions/README.md` 都说明它们是在复用同一 triage 语义与状态 schema，只是换了调度外壳

2. `GitHub Actions Harness -> Loop Control Contract`
   - `daily-triage.yml` 直接确保 `STATE.md` 存在并上传状态工件
   - 但 budget / run-log / verifier 在 workflow 模板里不是逐行硬编码，而是作为仓库级共享契约由使用者接线时继续沿用

## 裁剪依据

本轮按 skill 规则优先裁掉低信息模块：

- 已裁掉：
  - `docs/index.html`
  - `assets/visuals/*`
  - `stories/*`
  - `web-captures/*`
  - `tools/*/dist`
  - 根目录 dogfood 日志与状态文件作为独立节点

- 保留但折叠：
  - `patterns/*.md` 折叠到 `Pattern Registry`
  - `templates/*` 折叠到 `Starter Assets` 或 `Loop Control Contract`
  - `examples/grok`、`examples/claude-code`、`examples/codex` 折叠到 `Runtime Surface Examples`
  - `tools/loop-audit` + `tools/loop-cost` 折叠到 `Audit & Cost CLIs`

这样做是为了保住 UC02 的核心解释链：

`Pattern Registry -> loop-init / Starter Assets -> Runtime Surface Examples -> GitHub Actions Harness -> Loop Control Contract -> Audit & Cost CLIs`

## 关键证据文件

- `patterns/registry.yaml`
- `patterns/README.md`
- `scripts/validate-registry.mjs`
- `tools/loop-init/src/cli.ts`
- `tools/loop-init/README.md`
- `scripts/check-loop-init-sync.mjs`
- `starters/README.md`
- `starters/minimal-loop/README.md`
- `starters/minimal-loop/LOOP.md`
- `examples/README.md`
- `examples/grok/README.md`
- `examples/claude-code/daily-triage.md`
- `examples/codex/daily-triage.md`
- `examples/github-actions/README.md`
- `examples/github-actions/daily-triage.yml`
- `skills/loop-budget/SKILL.md`
- `skills/loop-verifier/SKILL.md`
- `scripts/append-run-log.mjs`
- `tools/loop-audit/src/auditor.ts`
- `tools/loop-cost/src/estimator.ts`
- `tools/loop-cost/scripts/bundle-registry.mjs`

## 未解决不确定性

1. 仓库刻意把真正的 agent 执行留在 `Invoke agent` 占位点，因此 GitHub Actions 与具体 agent runtime 的绑定深度只能建模到 harness 级别。
2. `loop-init` 中的预算常量目前是手写镜像而非自动生成；如果未来 registry cost 变化，development view 的这条依赖仍成立，但同步风险会上升。
3. `issue-triage` 没有专属 starter，本轮保守地把它视为 `minimal-loop` 的一个 pattern 变体，而不是新的脚手架模块。

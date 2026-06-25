# Anthropic Sub-Agent 官方材料分析

归档日期：2026-06-25

创建者：codex

## 归档范围

本目录归档本次分析中 Anthropic 官方工程博客相关的 Sub-Agent / Multi-Agent / Harness Design 来源理解交付件。

## 核心结论

Anthropic 的建议更偏架构与可靠性：Sub-Agent / Multi-Agent 适合高价值、可并行、上下文容量压力大、需要独立评估或开放式研究的任务；它不是默认架构，而是用额外 token、上下文窗口和编排复杂度换取覆盖面与质量。

适合使用 Sub-Agent 的场景：

- 开放式研究、线索多、资料量大、不同方向可并行探索。
- 长任务中需要 planner、generator、evaluator 或 QA 分工。
- 需要独立 evaluator 避免生成者自评过度乐观。
- 需要通过独立上下文窗口扩大有效搜索和压缩能力。

需谨慎的场景：

- 强共享上下文、依赖链密集或实时协作要求高的任务。
- 低价值任务，无法覆盖更高 token 与协调成本。
- 没有明确任务边界、输出格式和综合机制的多 agent 任务。

## 来源分析文件

| 来源 | 归档文件 |
| --- | --- |
| Harness design for long-running application development | `source-understanding/anthropic-harness-design.html` |
| How we built our multi-agent research system | `source-understanding/anthropic-multi-agent-research.html` |

## 官方链接

- https://www.anthropic.com/engineering/harness-design-long-running-apps
- https://www.anthropic.com/engineering/multi-agent-research-system

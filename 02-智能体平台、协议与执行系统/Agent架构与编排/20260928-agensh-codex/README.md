# Agensh

## 一句话总结

微软研究院等于2026年9月发布的 Agensh 是由共享工作区、消息接口和共享上下文支撑的无中央编排器多智能体协作框架，在 GPT-5.6-sol (high)、6小时预算的 pandoc 单题实验中，将最终测试通过率由1个智能体的33.89%提升至1,024个智能体的55.06%。

## 任务信息

- 序号：170
- 任务编号：DSH-20260924-019
- 热点编号：HS-20260924-dsh-tech-insight
- 周期：2026-W39
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：核心贡献是多智能体协作架构、任务认领与并行编排，归入 Agent架构与编排。
- 任务正文：📌Agensh：微软研究院提出无中央编排器的自组织多智能体协作框架，1,024 智能体下 pandoc 通过率提升 21.17 pp
原文标题：Agensh: Scaling Organizational Intelligence to 1,024 Agents
元信息：战略 · 2026/09/24 · 编号 #19 · 19.31%；The loop is supported by the agentic organization
要点：
- 协作循环由三类 agentic 组织基础设施支撑——共享 workspace（提案/进行中/已完成工作）、消息接口（组织广播 + 直信）、共享 context（可复用发现与工作意图）The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions
- 1→128 智能体使 ProgramBench 平均最终 test-pass rate 由 19.31% 升至 28.78%，相对提升约 49%Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement
- 在 pandoc 上，1→1,024 智能体使最终 test-pass rate 由 33.89% 升至 55.06%On pandoc, scaling from 1 to 1,024 agents raises the final test-pass rate from 33.89% to 55.06%
技术效果：效果 · 推理强化：基准性能：据 arXiv:2609.26781v1：在 ProgramBench 五难任务 + GPT-5.6-sol (high) / 6h 预算下，平均最终 test-pass rate 由 1 智能体 19.31% 升至 8 智能体 20.68%、32 智能体 26.52%、128 智能体 28.78%，绝对 +9.47 pp（相对约 49%）；架构创新：据 arXiv:2609.26781v1：Agensh 为"无中央编排器的自组织多智能体 harness"，通过五步协作循环（gather context / claim sub-task / take action / verify results / merge progress）异步运行并发 worker；据 arXiv:2609.26781v1：合作循环由各 worker 提示词中的工作流指令实现而非硬编码运行时，且仅通过轻量 harness适配器即可接入 Copilot、Claude Code 等不同底层 harness
背景补充：据 arXiv:2609.26781v1：pandoc 任务同 6h 预算下 test-pass rate 从 1 智能体 33.89% 升至 128 智能体 50.94%、1,024 智能体 55.06%；1,024 智能体配置下多个 worker 自发分化为 integrator（接触候选后选首个有效响应、取消其余请求再交接代码）。代码已开源（github.com/microsoft/Agensh）。
源链接：https://arxiv.org/abs/2609.26781
- 任务来源：[原任务来源](https://arxiv.org/abs/2609.26781)

## 交付件说明

- [Agensh.html](./Agensh.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Agensh.pptx](./Agensh.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Agensh: Scaling Organizational Intelligence to 1,024 Agents](https://arxiv.org/abs/2609.26781v1)：用于核对五步协作循环、三类共享基础设施及 ProgramBench/pandoc 实验口径。

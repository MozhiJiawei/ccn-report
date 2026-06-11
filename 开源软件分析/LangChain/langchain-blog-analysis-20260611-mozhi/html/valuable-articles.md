# LangChain Blog 高价值文章清单

筛选口径：内容详实，有关键技术展示，且对 LangChain 年度方向或行业落地有较大影响。

共 43 篇。

## 1. Choosing the Right Multi-Agent Architecture

- Date: January 14, 2026
- Local: agent-07/choosing-the-right-multi-agent-architecture/index.html
- URL: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
- 标注理由: 多 agent 架构选择文章，结构化比较 supervisor、swarm 等模式。
- 为什么：单 agent 最简单，但当能力数量、上下文和团队边界膨胀时，系统需要更清晰的协调方式来避免 prompt 混乱。
- 是什么：文章给出四种基础架构模式：subagents、skills、handoffs、routers，并用控制权、状态、上下文隔离和延迟成本来区分。
- 怎么做到：从最关键约束反推选择：需要集中控制选 subagents，需要轻量专业化选 skills，需要用户直达专家选 handoffs，需要确定分类选 routers。

## 2. How we built Agent Builder’s memory system

- Date: January 16, 2026
- Local: agent-07/how-we-built-agent-builders-memory/index.html
- URL: https://www.langchain.com/blog/how-we-built-agent-builders-memory
- 标注理由: 早期 Agent Builder memory 技术说明，和 2026 memory system 形成演进线。
- 为什么：Agent Builder 面向重复执行同类工作的定制 agent，没有记忆会让用户跨会话反复解释偏好、规则和工具边界。
- 是什么：文章说明 Agent Builder 把记忆设计成文件系统形态，并用 AGENTS.md、skills、tools.json 和知识文件对应 procedural、semantic 等记忆类型。
- 怎么做到：底层并不使用真实文件系统，而是把文件存进 Postgres，再通过 Deep Agents 的 virtual filesystem 暴露给模型，让 agent 能读写记忆并在热路径中更新。

## 3. From Traces to Insights: Understanding Agent Behavior at Scale

- Date: January 20, 2026
- Local: agent-07/from-traces-to-insights-understanding-agent-behavior-at-scale/index.html
- URL: https://www.langchain.com/blog/from-traces-to-insights-understanding-agent-behavior-at-scale
- 标注理由: 从 traces 到 insights，展示规模化理解 agent 行为的方法。
- 为什么：生产 agent 每天会生成成千上万条 traces，人工逐条阅读无法回答用户如何使用、哪里失败、模式如何变化。
- 是什么：文章把 LangSmith Insights Agent 定位为 agent analytics：它从非结构化对话中发现 usage patterns、error modes 和指定维度的聚类。
- 怎么做到：先用 traces 记录真实交互，再用聚类和探索式分析把海量会话归并为可解释模式，补足传统产品分析和已知问题 eval 的盲区。

## 4. Agent observability powers agent evaluation

- Date: January 27, 2026
- Local: agent-07/agent-observability-powers-agent-evaluation/index.html
- URL: https://www.langchain.com/blog/agent-observability-powers-agent-evaluation
- 标注理由: 说明 observability 如何转化为 evaluation，是 LangSmith 思路的关键连接。
- 为什么：Agent 失败常常藏在多步推理、工具调用、上下文和状态变化里，单看日志很难知道系统为什么偏离目标。
- 是什么：文章的核心判断是 observability 与 evaluation 在 agent 时代合并成同一套闭环：traces 同时支撑调试、测试、线上监控和事后洞察。
- 怎么做到：用 runs 捕获单步决策，用 traces 还原完整轨迹，用 threads 连接多轮上下文，再按 single-step、full-turn、multi-turn 与 offline、online、ad-hoc 粒度评估。

## 5. The two patterns by which agents connect sandboxes

- Date: 2026-02-10
- Local: agent-06/the-two-patterns-by-which-agents-connect-sandboxes/index.html
- URL: https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes
- 标注理由: 清楚拆解 agent 连接 sandbox 的两种模式，技术边界明确。
- 为什么：越来越多 agent 需要一台隔离的 computer 来运行代码、安装包和访问文件，关键问题从是否 sandbox 变成如何连接 sandbox。
- 是什么：文章区分两种架构：Agent IN Sandbox 和 Sandbox as Tool，前者贴近本地开发但密钥和通信复杂，后者隔离 agent state 与执行环境但会引入网络延迟。
- 怎么做到：deepagents 可通过配置支持两种模式；选择依据是环境耦合度、迭代速度、API key 边界、state 分离和 provider 通信能力。

## 6. Improving Deep Agents with harness engineering

- Date: 2026-02-17
- Local: agent-06/improving-deep-agents-with-harness-engineering/index.html
- URL: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- 标注理由: 把 Deep Agents 质量提升归因到 harness engineering，方向性强。
- 为什么：模型能力很强但输出尖峰明显，agent 质量常由 prompt、tools、middleware 等 harness 决定。
- 是什么：LangChain 在模型固定为 gpt-5.2-codex 的情况下，仅通过 harness engineering 让 deepagents-cli 在 Terminal Bench 2.0 从 52.8 提升到 66.5。
- 怎么做到：他们用 LangSmith traces 做失败分析，围绕 self-verification、环境上下文注入、loop detection 和 reasoning budget 调整迭代。

## 7. How we built Agent Builder's memory system

- Date: 2026-02-21
- Local: agent-06/how-we-built-agent-builders-memory-system/index.html
- URL: https://www.langchain.com/blog/how-we-built-agent-builders-memory-system
- 标注理由: Agent Builder memory 的文件化设计、Postgres 存储和人工确认机制都很具体。
- 为什么：Agent Builder 面向重复执行同类任务的自定义 agent，没有记忆会让用户在不同会话里反复校正同一件事。
- 是什么：LangChain 把记忆实现为 agent 可读写的文件形态，并映射到 COALA 的 procedural、semantic、episodic 记忆分类。
- 怎么做到：底层用 Postgres 存储并暴露成虚拟文件系统，AGENTS.md、skills、tools.json 和知识文件分别承载指令、专门知识与工具配置，所有记忆更新通过人工确认降低注入风险。

## 8. You don’t know what your agent will do until it’s in production

- Date: February 26, 2026
- Local: agent-07/production-monitoring/index.html
- URL: https://www.langchain.com/blog/production-monitoring
- 标注理由: 强调生产监控的不确定性，是 agent observability 的重要论点。
- 为什么：传统监控假设输入和代码路径相对固定，但 agent 面对自然语言、非确定性模型和多步工具调用，上线后才会暴露真实行为。
- 是什么：文章认为生产监控需要从 latency、error rate 扩展到输入、输出、推理轨迹、工具选择、用户反馈和质量变化。
- 怎么做到：用 LangSmith traces 捕获自然语言交互和工具链路，再把生产数据聚合为在线评价、失败模式、数据集和持续改进信号。

## 9. Evaluating Skills

- Date: March 5, 2026
- Local: agent-06/evaluating-skills/index.html
- URL: https://www.langchain.com/blog/evaluating-skills
- 标注理由: 有实验数据和结论，展示 skills 如何影响 agent 表现。
- 为什么：技能会改变编码 agent 的行为，凭感觉判断很容易漏掉退化。
- 是什么：LangChain 把技能评估做成一组可对照的实验：无技能、全技能、合并技能、拆分技能。
- 怎么做到：在干净沙箱中运行固定用例，用完成率、调用率、轮次和耗时衡量结果，再用 LangSmith 追踪每一步失败原因。

## 10. How we built LangChain’s GTM Agent

- Date: March 9, 2026
- Local: agent-08/how-we-built-langchains-gtm-agent/index.html
- URL: https://www.langchain.com/blog/how-we-built-langchains-gtm-agent
- 标注理由: 内部 GTM agent 案例，展示 Deep Agents、文件系统、工具链和 LangSmith 观测如何组合。
- 为什么：LangChain 的 GTM 团队需要把分散在 CRM、网页、新闻和内部材料里的公司线索变成可行动的账户研究，而不是让销售手工拼上下文。
- 是什么：文章展示了一个面向 go-to-market 的研究 agent：它围绕目标账户收集资料、生成摘要、识别触发事件，并把结果写回团队使用的业务系统。
- 怎么做到：实现上用 Deep Agents 的文件系统和技能组织长任务，用 LangSmith 观察工具调用和结果质量，并把搜索、内部数据访问、CRM 更新等能力包装成可控工具链。

## 11. The Anatomy of an Agent Harness

- Date: March 10, 2026
- Local: agent-05/the-anatomy-of-an-agent-harness/index.html
- URL: https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
- 标注理由: 系统拆解 harness 构成，是理解 LangChain agent 架构的基础文章。
- 为什么：原始模型不能持久记忆、访问实时知识、搭环境或执行复杂工作。
- 是什么：文章把 agent 定义为 Model + Harness，harness 是模型之外的代码、配置和执行逻辑。
- 怎么做到：它从期望行为倒推组件：filesystem、sandbox、tools、skills、MCPs、planning、subagents、middleware 和约束共同把模型智能变成 work engine。

## 12. Autonomous context compression

- Date: March 11, 2026
- Local: agent-05/autonomous-context-compression/index.html
- URL: https://www.langchain.com/blog/autonomous-context-compression
- 标注理由: 展示 agent 自主压缩上下文的机制，是 context engineering 的关键技术展示。
- 为什么：固定阈值压缩上下文会忽略工作节奏，可能在复杂工作中间发生。
- 是什么：Deep Agents 增加 context compression tool，让模型在合适时机主动压缩自己的工作记忆。
- 怎么做到：agent 在工作边界、提取结论后、读取大量新上下文前或进入多步流程前，把旧消息压成保留进度的 summary。

## 13. Open SWE: An Open-Source Framework for Internal Coding Agents

- Date: March 17, 2026
- Local: agent-05/open-swe-an-open-source-framework-for-internal-coding-agents/index.html
- URL: https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents
- 标注理由: Open SWE 展示内部异步 coding agent 框架，是开发者工作流重点。
- 为什么：多家公司内部 coding agent 已经收敛到相似生产架构，但每家从零搭建成本高。
- 是什么：Open SWE 是基于 Deep Agents 和 LangGraph 的开源框架，复用 sandbox、curated tools、workflow invocation 和 orchestration 模式。
- 怎么做到：它用持久云 sandbox、AGENTS.md + source context、subagents、middleware safety nets，把 Slack、Linear 和 GitHub 请求变成可审查的 PR 工作流。

## 14. How Moda Builds Production-Grade AI Design Agents with Deep Agents

- Date: March 24, 2026
- Local: agent-05/how-moda-builds-production-grade-ai-design-agents-with-deep-agents/index.html
- URL: https://www.langchain.com/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents
- 标注理由: 视觉设计 agent 案例复杂度高，覆盖多轮任务、可编辑画布和产品工作流。
- 为什么：AI 做视觉设计的难点不是生成一张漂亮图，而是让非设计师在品牌、版式和多轮修改里保持控制。
- 是什么：Moda 用 Deep Agents、LangSmith 和可编辑 2D 矢量画布，把专业级演示文稿、社媒图、手册和 PDF 变成可协作的 agent 工作流。
- 怎么做到：系统把工作分给设计、研究、品牌三类 agent，并通过自定义布局表示、动态技能与工具加载、按画布规模调节上下文来控制质量、成本和延迟。

## 15. customers-kensho

- Date: March 26, 2026
- Local: agent-04/customers-kensho/index.html
- URL: https://www.langchain.com/blog/customers-kensho
- 标注理由: 金融多 agent 检索案例，强调可信数据和复杂查询流程。
- 为什么：金融数据分散在多个系统中，专业用户花大量时间查找、验证和整合信息；AI agent 若没有可信数据层，答案很难被信任。
- 是什么：Kensho 用 LangGraph 构建 Grounding multi-agent framework，为 S&P Global 数据提供统一 agentic access layer，并通过 Data Retrieval Agents 连接不同数据源。
- 怎么做到：系统以 centralized entry point 接收查询，router 聚合多个单职责 DRA 的结果，使用 custom data retrieval protocol 保持来源、结构和可验证性。

## 16. how-middleware-lets-you-customize-your-agent-harness

- Date: March 26, 2026
- Local: agent-04/how-middleware-lets-you-customize-your-agent-harness/index.html
- URL: https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
- 标注理由: middleware 是 LangChain agent loop 定制的关键抽象。
- 为什么：标准 agent loop 很简洁，但生产场景常需要 PII 检测、工具选择、上下文管理等应用特定逻辑；只改 prompt 和 tools 不够。
- 是什么：LangChain middleware 提供 hooks，让开发者在 agent harness 的关键步骤前后插入自定义逻辑，同时保留 create_agent 和 Deep Agents 的基础结构。
- 怎么做到：middleware 可以围绕 model call、tool call、state/context 处理等位置工作；Deep Agents 自身也通过 middleware 组合出 planner、filesystem、subagents 等能力。

## 17. how-we-build-evals-for-deep-agents

- Date: March 26, 2026
- Local: agent-04/how-we-build-evals-for-deep-agents/index.html
- URL: https://www.langchain.com/blog/how-we-build-evals-for-deep-agents
- 标注理由: Deep Agents eval 构建方法详实，是评测工程代表。
- 为什么：Deep Agents 的行为由 evals 牵引；如果 eval 数据和指标不贴近生产行为，分数提升可能只是错觉。
- 是什么：文章介绍 LangChain 如何为 Deep Agents 构建 targeted evals：从 dogfooding、traces 和真实失败中取样，按行为分组，并用 LangSmith 共享 traces 反复分析。
- 怎么做到：团队先 catalog 生产中重要行为，再围绕文件检索、多步工具调用等行为写 eval；每次 eval run 都 trace 到 LangSmith，团队据此调整 prompt、tool description 或 harness。

## 18. agent-evaluation-readiness-checklist

- Date: March 27, 2026
- Local: agent-04/agent-evaluation-readiness-checklist/index.html
- URL: https://www.langchain.com/blog/agent-evaluation-readiness-checklist
- 标注理由: 把 agent evaluation 前置条件拆成 checklist，适合团队落地复用。
- 为什么：agent evaluation 和传统测试不同，需要先看运行轨迹、失败模式和行为目标；直接堆测试会得到脆弱信号。
- 是什么：文章给出 agent eval checklist，覆盖 error analysis、dataset construction、grader design、offline/online evals、iteration 和 production readiness。
- 怎么做到：先用少量 end-to-end eval 建 baseline，再从 traces 和人工分析构建数据集；grader 明确 rubric 和边界；offline eval 支持迭代，online eval 监控生产行为。

## 19. traces-start-agent-improvement-loop

- Date: March 31, 2026
- Local: agent-04/traces-start-agent-improvement-loop/index.html
- URL: https://www.langchain.com/blog/traces-start-agent-improvement-loop
- 标注理由: 把 trace 定义为改进闭环起点，是 LangSmith 年度主线之一。
- 为什么：agent 出错时，代码只能说明它被允许做什么，不能说明某次运行实际发生了什么；系统性改进需要运行证据。
- 是什么：文章把 trace 定义为 agent improvement loop 的原材料：collect traces、enrich with evals/human feedback、identify patterns、make targeted changes、validate before shipping。
- 怎么做到：LangSmith 用 online evaluators、insights/reports、annotation queues 和 offline eval datasets 把 traces 转成可行动数据，再让工程师或 coding agents 改 prompt、context、orchestration 或模型。

## 20. open-models-have-crossed-a-threshold

- Date: April 2, 2026
- Local: agent-04/open-models-have-crossed-a-threshold/index.html
- URL: https://www.langchain.com/blog/open-models-have-crossed-a-threshold
- 标注理由: 用模型能力变化解释 open models 进入 agent 场景的阈值变化。
- 为什么：agent 工作如果总用最强闭源模型，成本和延迟会成为规模化瓶颈；开源/开放权重模型是否能承担核心 agent 行为，需要 eval 证据。
- 是什么：LangChain 的 Deep Agents harness evals 显示，GLM-5 和 MiniMax M2.7 等 open models 在文件操作、工具调用、指令跟随等核心行为上已接近闭源 frontier models，并有成本/延迟优势。
- 怎么做到：文章用 harness evaluations 比较模型在实际 agent 行为上的表现，并建议按 cost、latency、task performance 组合使用 open 与 closed models。

## 21. how-my-agents-self-heal-in-production

- Date: April 3, 2026
- Local: agent-04/how-my-agents-self-heal-in-production/index.html
- URL: https://www.langchain.com/blog/how-my-agents-self-heal-in-production
- 标注理由: 生产自愈 agent 的 failure detection、triage、repair 流程很完整。
- 为什么：部署后的回归问题通常需要人工看日志、判断是否由本次改动引入、再写修复；这正是 coding agent 可以闭环处理的生产运维工作。
- 是什么：作者为 GTM Agent 搭了 self-healing deployment pipeline：每次部署后自动捕获 build/server 日志，检测回归，triage 因果，再让 Open SWE 开修复 PR。
- 怎么做到：流程分两路处理 Docker build failure 与 post-deploy server errors；服务器错误用 Poisson test 判断本次部署后是否显著上升，再由 triage agent 和 Open SWE 连接诊断与修复。

## 22. better-harness-a-recipe-for-harness-hill-climbing-with-evals

- Date: April 8, 2026
- Local: agent-04/better-harness-a-recipe-for-harness-hill-climbing-with-evals/index.html
- URL: https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals
- 标注理由: 提出 harness hill-climbing，把 agent harness 与 eval 迭代绑定。
- 为什么：agent 质量往往不是只改模型就能提升，真正可更新的是 harness；但 autonomous harness improvement 需要可靠学习信号。
- 是什么：Better-Harness 把 evals 当作 harness engineering 的训练数据，用数据 sourcing、实验设计、优化、review & acceptance 形成 hill-climbing loop。
- 怎么做到：系统从真实失败、人工 curated evals 和 traces 中构造信号，约束过拟合，保存长期 traces，并让 agent 提议 harness changes 后进入人工 review。

## 23. Human judgment in the agent improvement loop

- Date: April 9, 2026
- Local: agent-03/human-judgment-in-the-agent-improvement-loop/index.html
- URL: https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop
- 标注理由: 把人类判断转成 evaluator 和实验闭环，是 agent improvement loop 的关键文章。
- 为什么：Agent 失败往往不是简单的对错题，自动指标很难完整表达专家对质量、风险和业务语境的判断。
- 是什么：文章强调 human judgment 是 agent improvement loop 的核心输入：专家反馈需要被结构化，转化为 evals、数据集和可重复的改进信号。
- 怎么做到：LangSmith 通过人工标注、反馈、数据集管理和评估流程，把专家判断从一次性评论变成可反复运行的测试资产。

## 24. Reusable Evaluators and Evaluator Templates in LangSmith

- Date: April 16, 2026
- Local: agent-03/reusable-langsmith-evaluator-templates/index.html
- URL: https://www.langchain.com/blog/reusable-langsmith-evaluator-templates
- 标注理由: 展示评估资产复用化，对团队规模化做 eval 有直接影响。
- 为什么：Agent 评估常常卡在重复写 evaluator、团队标准不一致和难以复用上，导致改进循环慢且不可比较。
- 是什么：LangSmith 推出 reusable evaluators 和 evaluator templates，让团队把常用评估逻辑保存、参数化并跨数据集或实验复用。
- 怎么做到：团队可以在 LangSmith 中创建 evaluator，配置模板变量和评分规则，再把它们应用到实验、数据集和 CI 式评估流程中。

## 25. Running Subagents in the Background

- Date: April 16, 2026
- Local: agent-03/running-subagents-in-the-background/index.html
- URL: https://www.langchain.com/blog/running-subagents-in-the-background
- 标注理由: 聚焦 background subagents、上下文隔离和并行执行，是多 agent runtime 的重要方向。
- 为什么：复杂 agent 不适合把所有工作分支都阻塞在主对话里，尤其是研究、检索、代码检查这类耗时工作会拖慢交互。
- 是什么：文章介绍 background subagents：主 agent 可以派发并行分支，让子 agent 在后台运行，再把结果汇总回主流程。
- 怎么做到：通过调度、状态跟踪、结果回收和上下文隔离，background subagents 让深度 agent 在保持用户交互的同时处理耗时分支。

## 26. A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

- Date: April 16, 2026
- Local: agent-03/secure-agents-cisco-ai-defense/index.html
- URL: https://www.langchain.com/blog/secure-agents-cisco-ai-defense
- 标注理由: 展示安全防护如何接入 LangChain agent middleware，企业安全意义强。
- 为什么：企业 agent 接入工具和数据后，安全团队需要在开发早期就检测 prompt injection、数据泄露和不安全输出，而不是上线后补救。
- 是什么：文章演示 Cisco AI Defense 与 LangChain agent 的快速集成，用策略检查和安全扫描为 agent 加上防护层。
- 怎么做到：开发者在 LangChain 调用链路中加入 Cisco AI Defense 相关检查，对输入、输出或工具交互进行检测，并在 LangSmith 中观察运行行为。

## 27. The Runtime Behind Production Deep Agents

- Date: April 20, 2026
- Local: agent-03/runtime-behind-production-deep-agents/index.html
- URL: https://www.langchain.com/blog/runtime-behind-production-deep-agents
- 标注理由: 系统展示 durable execution、streaming、human-in-the-loop、background execution 和 memory。
- 为什么：Deep Agents 要从 demo 进入生产，瓶颈不只是模型能力，而是长时工作、并发工具、状态恢复和人类介入这些运行时问题。
- 是什么：文章把 production deep agents 的底座定义为 durable execution、streaming、human-in-the-loop、background execution 和可观测状态管理。
- 怎么做到：LangGraph runtime 通过持久化 checkpoint、interrupt/resume、并发控制、流式事件和状态图，把 agent 的长时运行变成可恢复、可检查的工程流程。

## 28. tuning-deep-agents-different-models

- Date: April 29, 2026
- Local: agent-03/tuning-deep-agents-different-models/index.html
- URL: https://www.langchain.com/blog/tuning-deep-agents-different-models
- 标注理由: 模型 profile 和 benchmark 结合，说明 Deep Agents 如何适配不同模型。
- 为什么：Deep Agents 过去用一套通用 prompts、tools 和 middleware 覆盖所有大模型，但不同模型的提示指南和工具约定差异很大。
- 是什么：LangChain 引入 model-specific harness profiles，并内置 OpenAI、Anthropic、Google profiles；在 tau2-bench 子集上，相比默认 harness 提升 10 到 20 个百分点。
- 怎么做到：Profile 作为声明式覆盖层，按模型调整 system prompt、工具包含与命名、middleware、subagent 配置和 skills，同时保持 create_deep_agent 调用方式不变。

## 29. Building a Company Due Diligence Agent with Deep Agents, LangSmith, and Parallel

- Date: May 8, 2026
- Local: agent-02/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel/index.html
- URL: https://www.langchain.com/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel
- 标注理由: 把 Deep Agents、LangSmith 和外部研究 API 组合成完整 due diligence agent，技术链条完整。
- 为什么：公司尽调需要多步网页研究、证据收集、来源比较和综合判断，是浅层单次调用 agent 容易失效的典型任务。
- 是什么：文章用 Deep Agents、LangSmith 和 Parallel 构建公司尽调 agent，让它研究一家公司并输出结构化尽调结果。
- 怎么做到：Deep Agents 负责规划和文件式工作状态，Parallel 提供网页研究能力，LangSmith traces/evals 用来检查和改进整个流程。

## 30. The Agent Development Lifecycle: Build, Test, Deploy & Monitor AI Agents | LangChain

- Date: May 9, 2026
- Local: agent-02/the-agent-development-lifecycle/index.html
- URL: https://www.langchain.com/blog/the-agent-development-lifecycle
- 标注理由: 把 build/test/deploy/monitor 串成 agent 工程生命周期，是年度平台叙事的骨架。
- 为什么：团队可以很快做出 agent 原型，但生产表现取决于测试、部署、监控和持续迭代；把 agent 当成一次性 prompt 会留下质量和可靠性缺口。
- 是什么：文章提出 agent development lifecycle：build、test、deploy、monitor 四个阶段，并用它组织 LangChain 平台能力。
- 怎么做到：LangChain 把开发、评测、部署和监控放到同一循环里：先构建 agent，再用数据集和评估测试，通过平台部署，最后用生产观测信号继续改进。

## 31. Delta Channels: How We’re Evolving our Runtime for Long-Running Agents

- Date: May 12, 2026
- Local: agent-02/delta-channels-evolving-agent-runtime/index.html
- URL: https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
- 标注理由: 长运行 agent runtime 的增量事件机制，是 LangGraph 运行时演进的重要技术展示。
- 为什么：持久化 agent runtime 需要 checkpoint 来支持恢复、中断、streaming 和 human-in-the-loop，但长运行会让完整状态快照成本暴涨。
- 是什么：Delta Channels 演进了 LangGraph runtime 的状态模型，让长运行 agent 保持持久性，同时不必每一步都写入完整快照。
- 怎么做到：它不再每次 checkpoint 都保存完整 channel value，而是记录变化量，并通过基础状态加 diff 重建运行状态。

## 32. LangSmith LLM Gateway: runtime governance built into the agent lifecycle

- Date: May 13, 2026
- Local: agent-02/introducing-llm-gateway/index.html
- URL: https://www.langchain.com/blog/introducing-llm-gateway
- 标注理由: LLM Gateway 把治理嵌入 agent lifecycle，影响企业生产部署。
- 为什么：agent 进入生产后，团队需要在运行时控制模型供应商访问、成本、路由、可靠性和策略，而不是让每个应用各自处理。
- 是什么：LangSmith LLM Gateway 是 agent lifecycle 中的运行时治理层，集中管理模型访问、用量可见性、路由和策略控制。
- 怎么做到：Gateway 位于 agent 应用和模型供应商之间，标准化调用、记录用量、执行集中规则，并允许团队不改每个 agent 就调整治理行为。

## 33. Managed Deep Agents: the fastest way to ship a production deep agent

- Date: May 13, 2026
- Local: agent-02/introducing-managed-deep-agents/index.html
- URL: https://www.langchain.com/blog/introducing-managed-deep-agents
- 标注理由: Managed Deep Agents 是 Deep Agents 产品化和托管化的关键节点。
- 为什么：团队采用 deep agents 时会被长流程执行、sandbox、可观测性、部署和运维拖住，而他们真正想投入的是领域行为。
- 是什么：Managed Deep Agents 是托管化的生产 deep agent 发布路径，把 Deep Agents 背后的运行和运维组件产品化。
- 怎么做到：它组合 Deep Agents、LangGraph runtime、LangSmith observability、托管部署和 sandboxed execution，让团队不用自己拼装每一层。

## 34. We built SmithDB, the data layer for agent observability

- Date: May 13, 2026
- Local: agent-02/introducing-smithdb/index.html
- URL: https://www.langchain.com/blog/introducing-smithdb
- 标注理由: SmithDB 是 agent observability 数据层，技术含量和平台影响都高。
- 为什么：agent 可观测性会产生高容量、深层嵌套的 traces，包含运行、消息、工具调用、反馈和评测数据，通用存储很难支撑快速调试和分析。
- 是什么：SmithDB 是 LangChain 为 LangSmith agent observability 构建的数据层，面向 trace 结构而不是普通日志设计。
- 怎么做到：它围绕嵌套运行、查询性能和分析需求优化存储与检索，让团队能更快从大量 agent 行为记录中定位问题。

## 35. How We Built LangSmith Engine, Our Agent for Improving Agents

- Date: May 19, 2026
- Local: agent-01/how-we-built-langsmith-engine-our-agent-for-improving-agents/index.html
- URL: https://www.langchain.com/blog/how-we-built-langsmith-engine-our-agent-for-improving-agents
- 标注理由: LangSmith Engine 代表 LangChain 用 agent 改进 agent 的核心产品方向。
- 为什么：生产 agent 可能反复使用错工具、参数错误、低效执行或漏用工具，单条 trace 难以变成系统改进。
- 是什么：LangSmith Engine 把 traces 中的 recurring failure 转成 issue board、evaluator、dataset example 和 fix proposal。
- 怎么做到：它在 sandbox 中运行，使用 LangSmith CLI 拉取 traces 和 issue 状态，借 subagents 先筛查压缩 trajectory、再深查可疑 trace，并用 Agent Overview 保留跨轮记忆。

## 36. How Auth Proxy secures network access for LangSmith agent sandboxes

- Date: May 21, 2026
- Local: agent-01/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes/index.html
- URL: https://www.langchain.com/blog/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes
- 标注理由: 把 sandbox 出站网络安全、runtime 边界和密钥转发讲成具体架构。
- 为什么：sandbox 里的 agent 仍要联网和鉴权，直接把长期 secret 放进 runtime 会扩大泄露面。
- 是什么：LangSmith Auth Proxy 把凭据注入和 egress policy 移到网络边界，让 agent 发普通请求，却读不到 API key。
- 怎么做到：proxy 按目标 host/path 检查策略、注入 workspace_secret/plaintext/opaque headers，或通过 callback 获取短期凭据；异常时拒绝请求而不是无凭据放行。

## 37. From Token Streams to Agent Streams

- Date: May 21, 2026
- Local: agent-01/token-streams-to-agent-streams/index.html
- URL: https://www.langchain.com/blog/token-streams-to-agent-streams
- 标注理由: 从 token stream 到 agent stream，是 agent UI 和 observability 的关键抽象变化。
- 为什么：graph-shaped agent 的运行过程包含工具、subagent、状态、审批和媒体，token delta stream 不再够用。
- 是什么：新 streaming 模型把输出组织成 typed events、channels、namespaces、projections 和 scoped subscriptions。
- 怎么做到：应用订阅自己渲染的 projection，运行时负责组装、排序、重连和 replay；同一协议覆盖本地/远程运行及 React、Vue、Svelte、Angular SDK。

## 38. How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith

- Date: May 27, 2026
- Local: agent-01/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith/index.html
- URL: https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith
- 标注理由: 客户案例中平台化程度高，展示 LangGraph/LangSmith 在客服 agent 平台中的真实落地。
- 为什么：Lyft 客服场景扩张后，靠 MLE 把领域专家需求翻译成 agent 配置的模式太慢。
- 是什么：他们用 LangGraph 构建自助式多 agent 平台，并用 LangSmith 跟踪、评估和监控生产质量； configurable agent 开发从约 6 个月降到约 2 周。
- 怎么做到：meta agent 路由 rider/driver 请求到专门 subgraph，配置型 agent 由 JSON 和 Prompt Hub 动态生成，DynamoDB checkpoint、生产 traces、LLM-as-a-judge 和 dashboard 共同守住质量。

## 39. Building workflows for agents with Skills and Interpreters

- Date: May 29, 2026
- Local: agent-01/interpreter-skills/index.html
- URL: https://www.langchain.com/blog/interpreter-skills
- 标注理由: 展示 skill 从说明文档升级为可执行 TypeScript API 的关键技术路径。
- 为什么：只靠文字说明包装流程时，agent 在长任务中容易跳步、压缩流程或临场改写实现。
- 是什么：Interpreter skills 把 skill 变成“说明 + TypeScript API”，让确定性部分进入可测试代码，模型只负责判断何时调用和如何使用结果。
- 怎么做到：SKILL.md 继续负责发现与约束，index.ts 暴露模块函数；agent 在解释器里 import 后执行，函数可处理状态、工具结果和 subagent 调度。

## 40. How Rippling built production AI in 6 months with Deep Agents and LangSmith

- Date: June 1, 2026
- Local: agent-02/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith/index.html
- URL: https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith
- 标注理由: 企业级产品线 AI native 转型案例，影响面和落地密度都高。
- 为什么：公司级 AI 推进不能靠孤立原型；要快速覆盖多个产品，需要共享 agent 模式、调试能力、评测和运维可见性。
- 是什么：Rippling 用 Deep Agents 和 LangSmith 在六个月内把生产 AI 推进到多个产品线，案例强调的是规模化 agent 开发能力。
- 怎么做到：Deep Agents 提供可复用的 agent 结构和执行模式，LangSmith 提供 tracing、evaluation 和观测，让不同产品团队能在同一工程闭环中迭代。

## 41. Designing Efficient Verifiers for Legal Agents

- Date: June 2, 2026
- Local: agent-01/designing-efficient-verifiers-for-legal-agents/index.html
- URL: https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents
- 标注理由: 法律 agent 的 verifier / rubric / RL 成本问题讲得细，是评测从人工规则走向可训练验证器的代表。
- 为什么：法律工作跨文档、标准细、误放行代价高；LAB 里很多工作项含 50+ 条 criteria，逐条调用 frontier verifier 会让评测和 RL 后训练成本迅速放大。
- 是什么：Harvey 与 LangChain Labs 的实验显示，batch verifier 和 open model verifier 能把成本降一个数量级到三个数量级，但要接受不同程度的 label drift。
- 怎么做到：文章以 Opus 4.7 per-criterion 为参照，在 40 个 LAB 公开工作项、2,348 条 criteria 上比较模型与评分方式，再用 trace 驱动提示词调优来压低 false pass。

## 42. Introducing Rubrics: Build Agents that Evaluate and Correct Their Work

- Date: June 2, 2026
- Local: agent-01/introducing-rubrics-for-deepagents/index.html
- URL: https://www.langchain.com/blog/introducing-rubrics-for-deepagents
- 标注理由: rubric 让 agent 能评价并修正自己，是 Deep Agents 评测闭环的重要拼图。
- 为什么：复杂 agent 往往方向正确却没有真正达标，开发者还要手动检查、重跑和诊断。
- 是什么：RubricMiddleware 把“完成”的定义变成 grader 子 agent 可执行的 rubric，让 agent 在逐条反馈下继续修正。
- 怎么做到：把 middleware 接到 Deep Agents，并在调用时传入 rubric；grader 可调用测试等工具取证，循环到通过、达到迭代上限或失败状态为止。

## 43. Fault Tolerance in LangGraph: Retries, Timeouts, and Error Handlers

- Date: June 4, 2026
- Local: agent-01/fault-tolerance-in-langgraph/index.html
- URL: https://www.langchain.com/blog/fault-tolerance-in-langgraph
- 标注理由: 集中展示 LangGraph 在 retry、timeout、error handler 和 checkpoint 上的生产可靠性机制。
- 为什么：生产 agent 会遇到网络故障、工具错误、LLM 限流和长时间卡住的问题；任务跑了数小时后半路失败，重头再来不可持续。
- 是什么：文章把 LangGraph 的容错归纳为三件事：`RetryPolicy` 处理瞬时错误，`TimeoutPolicy` 防止节点无限挂起，`error_handler` 在重试耗尽后进入清理、告警、降级或补偿路径。
- 怎么做到：这些策略直接挂在 `StateGraph.add_node` 的节点上，由运行时在 checkpoint 中原子记录失败并调度处理器，使 SAGA 这类多步骤副作用流程能续跑到正确的补偿步骤。

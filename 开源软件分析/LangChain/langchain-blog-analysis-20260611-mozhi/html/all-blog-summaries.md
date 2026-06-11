# LangChain Blog 年度摘要汇总

范围：2026-01-01 至 2026-06-09。共 93 篇。

## 1. Designing Efficient Verifiers for Legal Agents

- URL: https://www.langchain.com/blog/designing-efficient-verifiers-for-legal-agents
- Local: agent-01/designing-efficient-verifiers-for-legal-agents/index.html
- Date: June 2, 2026
- Type: 技术长文
- 为什么：法律工作跨文档、标准细、误放行代价高；LAB 里很多工作项含 50+ 条 criteria，逐条调用 frontier verifier 会让评测和 RL 后训练成本迅速放大。
- 是什么：Harvey 与 LangChain Labs 的实验显示，batch verifier 和 open model verifier 能把成本降一个数量级到三个数量级，但要接受不同程度的 label drift。
- 怎么做到：文章以 Opus 4.7 per-criterion 为参照，在 40 个 LAB 公开工作项、2,348 条 criteria 上比较模型与评分方式，再用 trace 驱动提示词调优来压低 false pass。

## 2. Fault Tolerance in LangGraph: Retries, Timeouts, and Error Handlers

- URL: https://www.langchain.com/blog/fault-tolerance-in-langgraph
- Local: agent-01/fault-tolerance-in-langgraph/index.html
- Date: June 4, 2026
- Type: 技术长文
- 为什么：生产 agent 会遇到网络故障、工具错误、LLM 限流和长时间卡住的问题；任务跑了数小时后半路失败，重头再来不可持续。
- 是什么：文章把 LangGraph 的容错归纳为三件事：`RetryPolicy` 处理瞬时错误，`TimeoutPolicy` 防止节点无限挂起，`error_handler` 在重试耗尽后进入清理、告警、降级或补偿路径。
- 怎么做到：这些策略直接挂在 `StateGraph.add_node` 的节点上，由运行时在 checkpoint 中原子记录失败并调度处理器，使 SAGA 这类多步骤副作用流程能续跑到正确的补偿步骤。

## 3. Introducing Rubrics: Build Agents that Evaluate and Correct Their Work

- URL: https://www.langchain.com/blog/introducing-rubrics-for-deepagents
- Local: agent-01/introducing-rubrics-for-deepagents/index.html
- Date: June 2, 2026
- Type: release / 技术说明
- 为什么：复杂 agent 往往方向正确却没有真正达标，开发者还要手动检查、重跑和诊断。
- 是什么：RubricMiddleware 把“完成”的定义变成 grader 子 agent 可执行的 rubric，让 agent 在逐条反馈下继续修正。
- 怎么做到：把 middleware 接到 Deep Agents，并在调用时传入 rubric；grader 可调用测试等工具取证，循环到通过、达到迭代上限或失败状态为止。

## 4. Why Model Neutrality Matters More Than Cloud Neutrality

- URL: https://www.langchain.com/blog/model-neutrality
- Local: agent-01/model-neutrality/index.html
- Date: June 4, 2026
- Type: 薄观点文
- 为什么：模型本身变化太快，把业务逻辑交给单一厂商 harness 会把迁移成本压到最难拆的层。
- 是什么：文章认为 token 会继续商品化，真正的锁定发生在 agent 编排与工具层；中立 harness 需要开源、多模型、并理解不同模型 profile。
- 怎么做到：它借 Terraform 对抗云工具锁定的历史，推导出 agent 运行中也要能按步骤切换 Claude、GPT、Gemini、Llama 或自托管模型。

## 5. Building workflows for agents with Skills and Interpreters

- URL: https://www.langchain.com/blog/interpreter-skills
- Local: agent-01/interpreter-skills/index.html
- Date: May 29, 2026
- Type: 技术长文
- 为什么：只靠文字说明包装流程时，agent 在长任务中容易跳步、压缩流程或临场改写实现。
- 是什么：Interpreter skills 把 skill 变成“说明 + TypeScript API”，让确定性部分进入可测试代码，模型只负责判断何时调用和如何使用结果。
- 怎么做到：SKILL.md 继续负责发现与约束，index.ts 暴露模块函数；agent 在解释器里 import 后执行，函数可处理状态、工具结果和 subagent 调度。

## 6. How to Build a Custom Agent Harness

- URL: https://www.langchain.com/blog/how-to-build-a-custom-agent-harness
- Local: agent-01/how-to-build-a-custom-agent-harness/index.html
- Date: June 3, 2026
- Type: 技术说明
- 为什么：agent 的效果取决于 harness 是否把任务需要的上下文、工具和环境交给模型。
- 是什么：create_agent 是 LangChain 的最小 harness 原语，预置较少、可定制空间大；middleware 是定制 agent loop 的核心接口。
- 怎么做到：每个 middleware 负责一个 concern，在模型调用、工具调用、启动、结束和 stream 处理点组合起来，形成贴合具体任务的 harness。

## 7. How Lyft Built a Self-Serve AI Agent Platform for Customer Support with LangGraph and LangSmith

- URL: https://www.langchain.com/blog/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith
- Local: agent-01/lyft-built-a-self-serve-ai-agent-platform-for-customer-support-with-langgraph-and-langsmith/index.html
- Date: May 27, 2026
- Type: 案例
- 为什么：Lyft 客服场景扩张后，靠 MLE 把领域专家需求翻译成 agent 配置的模式太慢。
- 是什么：他们用 LangGraph 构建自助式多 agent 平台，并用 LangSmith 跟踪、评估和监控生产质量； configurable agent 开发从约 6 个月降到约 2 周。
- 怎么做到：meta agent 路由 rider/driver 请求到专门 subgraph，配置型 agent 由 JSON 和 Prompt Hub 动态生成，DynamoDB checkpoint、生产 traces、LLM-as-a-judge 和 dashboard 共同守住质量。

## 8. Give your agent its own computer

- URL: https://www.langchain.com/blog/give-your-ai-agent-its-own-computer
- Local: agent-01/give-your-ai-agent-its-own-computer/index.html
- Date: June 5, 2026
- Type: 产品观点 / 安全
- 为什么：会运行代码、安装依赖、处理文件和保持长会话的 agent，不能直接共享开发者电脑或普通容器边界。
- 是什么：LangSmith Sandboxes 给每个 agent 一个硬件虚拟化 microVM，兼具快速启动和有状态机器能力。
- 怎么做到：开发者用 SDK 创建 sandbox 并运行命令，依靠 snapshots/forks、blueprints、service URLs、Auth Proxy 和默认私有访问来支撑生产级执行。

## 9. How Auth Proxy secures network access for LangSmith agent sandboxes

- URL: https://www.langchain.com/blog/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes
- Local: agent-01/how-auth-proxy-secures-network-access-for-langsmith-agent-sandboxes/index.html
- Date: May 21, 2026
- Type: 技术长文 / 安全
- 为什么：sandbox 里的 agent 仍要联网和鉴权，直接把长期 secret 放进 runtime 会扩大泄露面。
- 是什么：LangSmith Auth Proxy 把凭据注入和 egress policy 移到网络边界，让 agent 发普通请求，却读不到 API key。
- 怎么做到：proxy 按目标 host/path 检查策略、注入 workspace_secret/plaintext/opaque headers，或通过 callback 获取短期凭据；异常时拒绝请求而不是无凭据放行。

## 10. Mission Control: Operating Self-Hosted LangSmith on Kubernetes

- URL: https://www.langchain.com/blog/mission-control-operating-self-hosted-langsmith-on-kubernetes
- Local: agent-01/mission-control-operating-self-hosted-langsmith-on-kubernetes/index.html
- Date: May 26, 2026
- Type: release / 部署
- 为什么：自托管 LangSmith 带来基础设施控制权，也把 Helm、kubectl、日志、dashboard 和支持脚本的切换成本交给平台团队。
- 是什么：Mission Control 是集群内运行的 LangSmith 运维层，不需要 ingress、外部控制平面或额外数据库。
- 怎么做到：它读取 Kubernetes primitives，再提供配置编辑、preflight、health、release、assistant、alerts、search、数据库检查和 diagnostic bundle 等 LangSmith-aware 工作流。

## 11. From Token Streams to Agent Streams

- URL: https://www.langchain.com/blog/token-streams-to-agent-streams
- Local: agent-01/token-streams-to-agent-streams/index.html
- Date: May 21, 2026
- Type: 技术长文
- 为什么：graph-shaped agent 的运行过程包含工具、subagent、状态、审批和媒体，token delta stream 不再够用。
- 是什么：新 streaming 模型把输出组织成 typed events、channels、namespaces、projections 和 scoped subscriptions。
- 怎么做到：应用订阅自己渲染的 projection，运行时负责组装、排序、重连和 replay；同一协议覆盖本地/远程运行及 React、Vue、Svelte、Angular SDK。

## 12. EU macroeconomic analysis with Deep Agents, LangSmith, and the You.com Finance Research API

- URL: https://www.langchain.com/blog/financial-ai-that-investigates-macro-trends-eu-economic-analysis-with-you-com-and-langchain
- Local: agent-01/financial-ai-that-investigates-macro-trends-eu-economic-analysis-with-you-com-and-langchain/index.html
- Date: May 20, 2026
- Type: 案例 / 技术长文
- 为什么：宏观金融研究既要全域数据覆盖，又要深挖异常国家和保留审计链；把所有问题塞进一个大查询会稀释检索预算。
- 是什么：文章展示 EU 2025 GDP 研究 agent，用 You.com Finance Research API、Deep Agents 和 LangSmith 生成带 citations、workpapers 和最终报告的分析。
- 怎么做到：orchestrator 把 Shape A 数据表、异常检测、分解和 country investigation 分给多个 subagent，并用 LangSmith trace 把每个结论追溯到 API call 与来源 URL。

## 13. How We Built LangSmith Engine, Our Agent for Improving Agents

- URL: https://www.langchain.com/blog/how-we-built-langsmith-engine-our-agent-for-improving-agents
- Local: agent-01/how-we-built-langsmith-engine-our-agent-for-improving-agents/index.html
- Date: May 19, 2026
- Type: 技术长文
- 为什么：生产 agent 可能反复使用错工具、参数错误、低效执行或漏用工具，单条 trace 难以变成系统改进。
- 是什么：LangSmith Engine 把 traces 中的 recurring failure 转成 issue board、evaluator、dataset example 和 fix proposal。
- 怎么做到：它在 sandbox 中运行，使用 LangSmith CLI 拉取 traces 和 issue 状态，借 subagents 先筛查压缩 trajectory、再深查可疑 trace，并用 Agent Overview 保留跨轮记忆。

## 14. Everything we shipped at Interrupt

- URL: https://www.langchain.com/blog/interrupt-2026-overview
- Local: agent-02/interrupt-2026-overview/index.html
- Date: May 14, 2026
- Type: release roundup
- 为什么：Agent 团队从原型走向生产时，瓶颈不只在模型调用，还包括发现失败、运行长流程、管理上下文和治理整个生命周期。
- 是什么：Interrupt 2026 集中发布 LangSmith Engine、SmithDB、Managed Deep Agents、Sandboxes GA、Context Hub、LLM Gateway、Fleet、Deep Agents 0.6 和 LangChain Labs，呈现一套生产 agent 平台叙事。
- 怎么做到：这些发布把 traces、运行时基础设施、上下文管理、治理、封装 agent 和应用研究连接起来：Engine 从 traces 生成修复和 evals，Sandboxes 与 Managed Deep Agents 承担执行层，Context Hub 与 Gateway 把行为上下文和策略并入同一流程。

## 15. New in Deep Agents v0.6

- URL: https://www.langchain.com/blog/deep-agents-0-6
- Local: agent-02/deep-agents-0-6/index.html
- Date: May 13, 2026
- Type: release / technical product update
- 为什么：长流程 agent 的瓶颈已经不只是模型答案质量，而是模型成本、上下文膨胀、检查点存储和前端可观测性一起限制生产化。
- 是什么：Deep Agents v0.6 把 code interpreter、harness profiles、streaming v3、DeltaChannel 和 ContextHubBackend 打包成同一条性能主线。
- 怎么做到：它让工具调用在运行时中完成、按模型版本化调优 harness、用类型化事件流暴露进度、用 diff 存检查点，并把 agent 行为文件放进可版本化的 Context Hub。

## 16. Introducing LangSmith Context Hub

- URL: https://www.langchain.com/blog/introducing-context-hub
- Local: agent-02/introducing-context-hub/index.html
- Date: May 13, 2026
- Type: release / product update
- 为什么：生产 agent 的行为越来越依赖 AGENTS.md、skills、policy、examples 这类文件，散落在个人电脑或仓库里会让复用、审阅和环境切换变难。
- 是什么：LangSmith Context Hub 提供一个集中位置来存储、版本化和协作管理这些影响 agent 行为的上下文文件。
- 怎么做到：它把文件组织成 repo，支持 commit history、diff、branch、tag、review、environment promotion，并通过 SDK、MCP 和 Deep Agents 后端接入运行时。

## 17. Introducing Langsmith Engine

- URL: https://www.langchain.com/blog/introducing-langsmith-engine
- Local: agent-02/introducing-langsmith-engine/index.html
- Date: May 13, 2026
- Type: release / product update
- 为什么：agent 团队虽然能收集 traces，但 trace 本身不会说明该修什么；团队需要把已观察到的失败转成评测、prompt 改动、harness 更新和验证结果。
- 是什么：LangSmith Engine 是一个用于改进 agent 的 AI agent，会分析 LangSmith traces、识别失败模式，并帮助团队从调试证据走向具体修复。
- 怎么做到：Engine 把可观测数据用于诊断、评估器生成、改动建议和验证循环，让 agent 改进更自动化，同时仍以 trace 作为依据。

## 18. LangSmith LLM Gateway: runtime governance built into the agent lifecycle

- URL: https://www.langchain.com/blog/introducing-llm-gateway
- Local: agent-02/introducing-llm-gateway/index.html
- Date: May 13, 2026
- Type: release / governance product update
- 为什么：agent 进入生产后，团队需要在运行时控制模型供应商访问、成本、路由、可靠性和策略，而不是让每个应用各自处理。
- 是什么：LangSmith LLM Gateway 是 agent lifecycle 中的运行时治理层，集中管理模型访问、用量可见性、路由和策略控制。
- 怎么做到：Gateway 位于 agent 应用和模型供应商之间，标准化调用、记录用量、执行集中规则，并允许团队不改每个 agent 就调整治理行为。

## 19. Managed Deep Agents: the fastest way to ship a production deep agent

- URL: https://www.langchain.com/blog/introducing-managed-deep-agents
- Local: agent-02/introducing-managed-deep-agents/index.html
- Date: May 13, 2026
- Type: release / managed runtime
- 为什么：团队采用 deep agents 时会被长流程执行、sandbox、可观测性、部署和运维拖住，而他们真正想投入的是领域行为。
- 是什么：Managed Deep Agents 是托管化的生产 deep agent 发布路径，把 Deep Agents 背后的运行和运维组件产品化。
- 怎么做到：它组合 Deep Agents、LangGraph runtime、LangSmith observability、托管部署和 sandboxed execution，让团队不用自己拼装每一层。

## 20. We built SmithDB, the data layer for agent observability

- URL: https://www.langchain.com/blog/introducing-smithdb
- Local: agent-02/introducing-smithdb/index.html
- Date: May 13, 2026
- Type: technical product architecture
- 为什么：agent 可观测性会产生高容量、深层嵌套的 traces，包含运行、消息、工具调用、反馈和评测数据，通用存储很难支撑快速调试和分析。
- 是什么：SmithDB 是 LangChain 为 LangSmith agent observability 构建的数据层，面向 trace 结构而不是普通日志设计。
- 怎么做到：它围绕嵌套运行、查询性能和分析需求优化存储与检索，让团队能更快从大量 agent 行为记录中定位问题。

## 21. LangSmith Sandboxes are Generally Available

- URL: https://www.langchain.com/blog/langsmith-sandboxes-generally-available
- Local: agent-02/langsmith-sandboxes-generally-available/index.html
- Date: May 13, 2026
- Type: release / infrastructure
- 为什么：生产 agent 越来越需要执行代码、操作文件和调用工具，因此隔离、清理、可靠性和可观测性都变成平台问题。
- 是什么：LangSmith Sandboxes 正式 GA，把隔离执行环境变成 LangSmith 支持的 agent 工作负载基础能力。
- 怎么做到：Sandboxes 为 agent 提供受控的代码执行和文件工作空间，并与 LangSmith 观测、生命周期管理和调试流程连接起来。

## 22. Delta Channels: How We’re Evolving our Runtime for Long-Running Agents

- URL: https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
- Local: agent-02/delta-channels-evolving-agent-runtime/index.html
- Date: May 12, 2026
- Type: technical longform
- 为什么：持久化 agent runtime 需要 checkpoint 来支持恢复、中断、streaming 和 human-in-the-loop，但长运行会让完整状态快照成本暴涨。
- 是什么：Delta Channels 演进了 LangGraph runtime 的状态模型，让长运行 agent 保持持久性，同时不必每一步都写入完整快照。
- 怎么做到：它不再每次 checkpoint 都保存完整 channel value，而是记录变化量，并通过基础状态加 diff 重建运行状态。

## 23. The Agent Development Lifecycle: Build, Test, Deploy & Monitor AI Agents | LangChain

- URL: https://www.langchain.com/blog/the-agent-development-lifecycle
- Local: agent-02/the-agent-development-lifecycle/index.html
- Date: May 9, 2026
- Type: framework / lifecycle guide
- 为什么：团队可以很快做出 agent 原型，但生产表现取决于测试、部署、监控和持续迭代；把 agent 当成一次性 prompt 会留下质量和可靠性缺口。
- 是什么：文章提出 agent development lifecycle：build、test、deploy、monitor 四个阶段，并用它组织 LangChain 平台能力。
- 怎么做到：LangChain 把开发、评测、部署和监控放到同一循环里：先构建 agent，再用数据集和评估测试，通过平台部署，最后用生产观测信号继续改进。

## 24. Building a Company Due Diligence Agent with Deep Agents, LangSmith, and Parallel

- URL: https://www.langchain.com/blog/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel
- Local: agent-02/building-a-company-due-diligence-agent-with-deep-agents-langsmith-and-parallel/index.html
- Date: May 8, 2026
- Type: technical case / tutorial
- 为什么：公司尽调需要多步网页研究、证据收集、来源比较和综合判断，是浅层单次调用 agent 容易失效的典型任务。
- 是什么：文章用 Deep Agents、LangSmith 和 Parallel 构建公司尽调 agent，让它研究一家公司并输出结构化尽调结果。
- 怎么做到：Deep Agents 负责规划和文件式工作状态，Parallel 提供网页研究能力，LangSmith traces/evals 用来检查和改进整个流程。

## 25. How Madrigal Built a Flexible and Scalable Multi-Agent Research and Intelligence Platform for Pharma with LangChain and LangSmith

- URL: https://www.langchain.com/blog/customers-madrigal
- Local: agent-02/customers-madrigal/index.html
- Date: April 29, 2026
- Type: customer case
- 为什么：制药研究和情报工作横跨科学、临床、市场和商业来源，人工综合速度慢，一次性自动化也很难适应不断变化的问题。
- 是什么：Madrigal 用 LangChain 和 LangSmith 构建灵活、可扩展的多 agent 研究与情报平台，用于整合多来源信息。
- 怎么做到：LangChain 支撑多 agent workflow 和工具编排，LangSmith 提供 tracing、evaluation 和 observability，让团队能持续迭代质量。

## 26. How Harmonic rebuilt Scout on Deep Agents and 4x’d retention with LangSmith

- URL: https://www.langchain.com/blog/how-harmonic-rebuilt-scout-on-deep-agents-and-4xd-retention-with-langsmith
- Local: agent-02/how-harmonic-rebuilt-scout-on-deep-agents-and-4xd-retention-with-langsmith/index.html
- Date: June 3, 2026
- Type: customer case
- 为什么：Scout 这类创业公司发现产品需要足够深入的研究能力，用户才会把它当成可信工作流，而不是一次性搜索框。
- 是什么：Harmonic 用 Deep Agents 重构 Scout，并借助 LangSmith 报告了 4 倍留存提升，案例把 agent 架构和可观测性连接到产品结果。
- 怎么做到：Deep Agents 提供更适合研究任务的循环、规划和状态管理，LangSmith 则提供 tracing 与 evaluation，用来调试、衡量和改进产品体验。

## 27. How Rippling built production AI in 6 months with Deep Agents and LangSmith

- URL: https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith
- Local: agent-02/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith/index.html
- Date: June 1, 2026
- Type: customer case
- 为什么：公司级 AI 推进不能靠孤立原型；要快速覆盖多个产品，需要共享 agent 模式、调试能力、评测和运维可见性。
- 是什么：Rippling 用 Deep Agents 和 LangSmith 在六个月内把生产 AI 推进到多个产品线，案例强调的是规模化 agent 开发能力。
- 怎么做到：Deep Agents 提供可复用的 agent 结构和执行模式，LangSmith 提供 tracing、evaluation 和观测，让不同产品团队能在同一工程闭环中迭代。

## 28. tuning-deep-agents-different-models

- URL: https://www.langchain.com/blog/tuning-deep-agents-different-models
- Local: agent-03/tuning-deep-agents-different-models/index.html
- Date: April 29, 2026
- Type: 技术长文 / product announcement
- 为什么：Deep Agents 过去用一套通用 prompts、tools 和 middleware 覆盖所有大模型，但不同模型的提示指南和工具约定差异很大。
- 是什么：LangChain 引入 model-specific harness profiles，并内置 OpenAI、Anthropic、Google profiles；在 tau2-bench 子集上，相比默认 harness 提升 10 到 20 个百分点。
- 怎么做到：Profile 作为声明式覆盖层，按模型调整 system prompt、工具包含与命名、middleware、subagent 配置和 skills，同时保持 create_deep_agent 调用方式不变。

## 29. april-2026-langchain-newsletter

- URL: https://www.langchain.com/blog/april-2026-langchain-newsletter
- Local: agent-03/april-2026-langchain-newsletter/index.html
- Date: April 27, 2026
- Type: newsletter
- 为什么：四月内容围绕 Interrupt 倒计时，把社区注意力集中到 agent improvement loop、开放 harness 与生产部署。
- 是什么：本期重点不是零散新闻，而是三组信号：Deep Agents 的开放控制面、LangSmith 的人工反馈到 evals 链路、客户案例里的可量化业务效果。
- 怎么做到：LangChain 用博客、meetups 和客户故事把“构建、观察、评估、改进、部署”串成一条工程化路径。

## 30. How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements

- URL: https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act
- Local: agent-03/langsmith-langchain-oss-eu-ai-act/index.html
- Date: April 27, 2026
- Type: 合规 / product guide
- 为什么：欧盟 AI Act 的 GPAI 截止日临近，团队需要把合规义务翻译成可执行的工程控制，而不是在最后阶段补文档。
- 是什么：文章把模型可追踪、文档、版权政策、安全评估和事件上报等义务，映射到 LangSmith 与 LangChain OSS 的可观察、评估和治理能力。
- 怎么做到：LangSmith 负责运行记录、数据集、评估、追踪和监控，LangChain OSS 负责可控的应用编排与工具调用，使团队能用同一条开发链路留下合规证据。

## 31. Fixing agent failures in production: Interrupt 2026 recap | LangChain Newsletter

- URL: https://www.langchain.com/blog/may-2026-langchain-newsletter
- Local: agent-03/may-2026-langchain-newsletter/index.html
- Date: May 27, 2026
- Type: newsletter
- 为什么：五月通讯承接 Interrupt 2026，把主题从发布清单收束到一个问题：生产 agent 失败后，团队怎样更快定位、修复并规模化复用改进。
- 是什么：本期核心信号是 LangSmith Engine、Context Hub、LLM Gateway、Managed Deep Agents、Sandboxes GA 和 SmithDB 共同补齐生产生命周期，而不是单点功能更新。
- 怎么做到：LangChain 用大会发布、产品 recap 和客户实践把观察、上下文、治理、执行环境与数据层串成生产 agent 的闭环。

## 32. How Credit Genie used Insights Agent to improve their AI financial assistant

- URL: https://www.langchain.com/blog/credit-genie-insights-agent-financial-assistant
- Local: agent-03/credit-genie-insights-agent-financial-assistant/index.html
- Date: April 22, 2026
- Type: 案例
- 为什么：Credit Genie 的 AI 金融助手已经在生产中服务用户，但团队需要知道失败集中在哪里，才能把客服压力和用户困惑转成可修复的产品问题。
- 是什么：Insights Agent 从 LangSmith 轨迹中发现 36% 客服请求来自同一类产品缺口，让团队把模糊反馈变成具体改进机会。
- 怎么做到：Credit Genie 用 LangSmith 收集运行轨迹，再让 Insights Agent 聚类、解释和定位失败模式，帮助团队优先处理高频问题。

## 33. The Runtime Behind Production Deep Agents

- URL: https://www.langchain.com/blog/runtime-behind-production-deep-agents
- Local: agent-03/runtime-behind-production-deep-agents/index.html
- Date: April 20, 2026
- Type: 技术长文
- 为什么：Deep Agents 要从 demo 进入生产，瓶颈不只是模型能力，而是长时工作、并发工具、状态恢复和人类介入这些运行时问题。
- 是什么：文章把 production deep agents 的底座定义为 durable execution、streaming、human-in-the-loop、background execution 和可观测状态管理。
- 怎么做到：LangGraph runtime 通过持久化 checkpoint、interrupt/resume、并发控制、流式事件和状态图，把 agent 的长时运行变成可恢复、可检查的工程流程。

## 34. Agentic Engineering: How Swarms of AI Agents Are Redefining Software Engineering

- URL: https://www.langchain.com/blog/agentic-engineering-redefining-software-engineering
- Local: agent-03/agentic-engineering-redefining-software-engineering/index.html
- Date: April 20, 2026
- Type: 观点 / 趋势
- 为什么：软件工程正在从单个 copilots 走向多 agent 协作，团队需要重新理解工程组织方式，而不是只把 AI 当成代码补全。
- 是什么：文章提出 agentic engineering：多个专门 agent 可以并行承担设计、实现、测试、审查和迭代，软件团队的关键能力转向编排与评价 agent 工作。
- 怎么做到：它通过工作拆分、agent swarm、反馈循环和工程控制面，把人类工程师放到目标设定、验收和系统设计的位置。

## 35. Reusable Evaluators and Evaluator Templates in LangSmith

- URL: https://www.langchain.com/blog/reusable-langsmith-evaluator-templates
- Local: agent-03/reusable-langsmith-evaluator-templates/index.html
- Date: April 16, 2026
- Type: release / product guide
- 为什么：Agent 评估常常卡在重复写 evaluator、团队标准不一致和难以复用上，导致改进循环慢且不可比较。
- 是什么：LangSmith 推出 reusable evaluators 和 evaluator templates，让团队把常用评估逻辑保存、参数化并跨数据集或实验复用。
- 怎么做到：团队可以在 LangSmith 中创建 evaluator，配置模板变量和评分规则，再把它们应用到实验、数据集和 CI 式评估流程中。

## 36. Running Subagents in the Background

- URL: https://www.langchain.com/blog/running-subagents-in-the-background
- Local: agent-03/running-subagents-in-the-background/index.html
- Date: April 16, 2026
- Type: 技术长文
- 为什么：复杂 agent 不适合把所有工作分支都阻塞在主对话里，尤其是研究、检索、代码检查这类耗时工作会拖慢交互。
- 是什么：文章介绍 background subagents：主 agent 可以派发并行分支，让子 agent 在后台运行，再把结果汇总回主流程。
- 怎么做到：通过调度、状态跟踪、结果回收和上下文隔离，background subagents 让深度 agent 在保持用户交互的同时处理耗时分支。

## 37. A Developer’s First 10 Minutes: Secure LangChain Agents with Cisco AI Defense

- URL: https://www.langchain.com/blog/secure-agents-cisco-ai-defense
- Local: agent-03/secure-agents-cisco-ai-defense/index.html
- Date: April 16, 2026
- Type: partner guide / security
- 为什么：企业 agent 接入工具和数据后，安全团队需要在开发早期就检测 prompt injection、数据泄露和不安全输出，而不是上线后补救。
- 是什么：文章演示 Cisco AI Defense 与 LangChain agent 的快速集成，用策略检查和安全扫描为 agent 加上防护层。
- 怎么做到：开发者在 LangChain 调用链路中加入 Cisco AI Defense 相关检查，对输入、输出或工具交互进行检测，并在 LangSmith 中观察运行行为。

## 38. How We Made Our Docs Test Themselves

- URL: https://www.langchain.com/blog/our-docs-test-themselves
- Local: agent-03/our-docs-test-themselves/index.html
- Date: April 15, 2026
- Type: 工程实践
- 为什么：文档里的代码示例很容易随 API 演进失效，读者遇到坏示例时会直接损失信任和开发时间。
- 是什么：LangChain 把文档示例纳入自动测试，让 docs 能够持续验证自身代码片段是否仍然可运行。
- 怎么做到：团队从文档中提取示例、构建测试环境、运行检查并把失败反馈到维护流程，使文档和代码演进保持同步。

## 39. Deep Agents Deploy: an open alternative to Claude Managed Agents

- URL: https://www.langchain.com/blog/deep-agents-deploy-an-open-alternative-to-claude-managed-agents
- Local: agent-03/deep-agents-deploy-an-open-alternative-to-claude-managed-agents/index.html
- Date: April 9, 2026
- Type: release / deployment
- 为什么：团队想要托管式 coding/deep agent 的便利性，但也需要开放、可迁移、可自定义的部署路径。
- 是什么：Deep Agents Deploy 被定位为 Claude Managed Agents 的开放替代方案，让开发者部署自己的 deep agents，而不被单一托管形态限制。
- 怎么做到：它把 deep agent harness、运行时、环境配置和部署流程打包成可运行服务，使团队能保留工具、模型、上下文和基础设施选择权。

## 40. Human judgment in the agent improvement loop

- URL: https://www.langchain.com/blog/human-judgment-in-the-agent-improvement-loop
- Local: agent-03/human-judgment-in-the-agent-improvement-loop/index.html
- Date: April 9, 2026
- Type: 观点 / evaluation
- 为什么：Agent 失败往往不是简单的对错题，自动指标很难完整表达专家对质量、风险和业务语境的判断。
- 是什么：文章强调 human judgment 是 agent improvement loop 的核心输入：专家反馈需要被结构化，转化为 evals、数据集和可重复的改进信号。
- 怎么做到：LangSmith 通过人工标注、反馈、数据集管理和评估流程，把专家判断从一次性评论变成可反复运行的测试资产。

## 41. Interrupt Preview: Meet the MC

- URL: https://www.langchain.com/blog/interrupt-preview-meet-the-mc
- Local: agent-03/interrupt-preview-meet-the-mc/index.html
- Date: April 9, 2026
- Type: event preview / 薄观点文
- 为什么：Interrupt 2026 不只是产品大会预告，文章通过主持人视角提前设定会议的讨论气质和关注问题。
- 是什么：这篇短文介绍 MC，并把大会定位在 agent 从实验走向企业规模化的现场交流，而不是单向发布。
- 怎么做到：通过人物介绍、会议议程语境和社区邀请，文章把参会者注意力引向现场对话、案例和 agent 工程实践。

## 42. introducing-langchain-labs

- URL: https://www.langchain.com/blog/introducing-langchain-labs
- Local: agent-04/introducing-langchain-labs/index.html
- Date: May 14, 2026
- Type: thin viewpoint / company announcement
- 为什么：agent 每次运行都会留下 traces、反馈、eval 结果和生产行为，但难点是把这些信号转成可复用改进。
- 是什么：LangChain Labs 是围绕 continual learning 的应用研究计划，和 Harvey、NVIDIA、Prime Intellect、Fireworks、Baseten 一起推进开放研究。
- 怎么做到：它从 LangSmith 擅长捕获和整理的数据出发，研究数据挖掘、成本/延迟/效果权衡、评测与仿真环境、跨模型提示优化。

## 43. previewing-interrupt-2026-agents-at-enterprise-scale

- URL: https://www.langchain.com/blog/previewing-interrupt-2026-agents-at-enterprise-scale
- Local: agent-04/previewing-interrupt-2026-agents-at-enterprise-scale/index.html
- Date: April 9, 2026
- Type: event preview / company announcement
- 为什么：去年 Interrupt 的生产化答案已经是 yes；今年真正悬而未决的是，当 agent 不再是概念验证，企业级系统要怎样运行。
- 是什么：Interrupt 2026 定在 5 月 13-14 日旧金山 The Midway，主题聚焦 agents at enterprise scale，并用 keynotes、fireside chats 和生产案例展开。
- 怎么做到：文章把答案落到三类证据：企业平台与数据层讨论、Lyft/LinkedIn 等生产实践、以及围绕 LangSmith、LangGraph、Deep Agents 的 hands-on 环节。

## 44. arcade-dev-tools-now-in-langsmith-fleet

- URL: https://www.langchain.com/blog/arcade-dev-tools-now-in-langsmith-fleet
- Local: agent-04/arcade-dev-tools-now-in-langsmith-fleet/index.html
- Date: April 7, 2026
- Type: release / partner announcement
- 为什么：Fleet 里的 agent 要跨 Salesforce、Notion、Slack 等工具工作，真正的瓶颈不是多接几个 API，而是连接、授权和治理会迅速膨胀。
- 是什么：LangSmith Fleet 接入 Arcade.dev，把 7,500+ agent-optimized tools 放到一个安全 MCP gateway 后面，并支持 60+ 预配置模板。
- 怎么做到：Arcade 提供单一 gateway、面向 agent 缩窄过的工具描述，以及 per-user/session-scoped authorization；Fleet 决定凭据以用户身份还是共享身份流入 Arcade。

## 45. deep-agents-v0-5

- URL: https://www.langchain.com/blog/deep-agents-v0-5
- Local: agent-04/deep-agents-v0-5/index.html
- Date: April 7, 2026
- Type: release
- 为什么：长时间研究、代码分析和多步骤操作会阻塞 supervisor agent，单线程等待让 Deep Agents 难以处理更重的工作。
- 是什么：Deep Agents v0.5 发布 async subagents，并扩展虚拟文件系统的多模态读取能力。
- 怎么做到：supervisor 可以启动远程 agent 后拿到 运行 ID 继续工作；远程端通过 Agent Protocol 的 threads/runs 模型承接状态，read_file 则自动按扩展名传递 PDF、音频、视频等 MIME content block。

## 46. how-my-agents-self-heal-in-production

- URL: https://www.langchain.com/blog/how-my-agents-self-heal-in-production
- Local: agent-04/how-my-agents-self-heal-in-production/index.html
- Date: April 3, 2026
- Type: technical longform
- 为什么：部署后的回归问题通常需要人工看日志、判断是否由本次改动引入、再写修复；这正是 coding agent 可以闭环处理的生产运维工作。
- 是什么：作者为 GTM Agent 搭了 self-healing deployment pipeline：每次部署后自动捕获 build/server 日志，检测回归，triage 因果，再让 Open SWE 开修复 PR。
- 怎么做到：流程分两路处理 Docker build failure 与 post-deploy server errors；服务器错误用 Poisson test 判断本次部署后是否显著上升，再由 triage agent 和 Open SWE 连接诊断与修复。

## 47. open-models-have-crossed-a-threshold

- URL: https://www.langchain.com/blog/open-models-have-crossed-a-threshold
- Local: agent-04/open-models-have-crossed-a-threshold/index.html
- Date: April 2, 2026
- Type: technical viewpoint
- 为什么：agent 工作如果总用最强闭源模型，成本和延迟会成为规模化瓶颈；开源/开放权重模型是否能承担核心 agent 行为，需要 eval 证据。
- 是什么：LangChain 的 Deep Agents harness evals 显示，GLM-5 和 MiniMax M2.7 等 open models 在文件操作、工具调用、指令跟随等核心行为上已接近闭源 frontier models，并有成本/延迟优势。
- 怎么做到：文章用 harness evaluations 比较模型在实际 agent 行为上的表现，并建议按 cost、latency、task performance 组合使用 open 与 closed models。

## 48. march-2026-langchain-newsletter

- URL: https://www.langchain.com/blog/march-2026-langchain-newsletter
- Local: agent-04/march-2026-langchain-newsletter/index.html
- Date: April 1, 2026
- Type: newsletter
- 为什么：三月更新很多，单条公告分散；newsletter 用一个月度视角把产品、开源、活动和客户动态合到一起。
- 是什么：本期主线是 LangSmith Fleet 成型：Polly GA、Agent Builder 更名 Fleet、Skills、Sandboxes、Deploy CLI、ABAC、NVIDIA 集成与 Interrupt 2026 售票同步推进。
- 怎么做到：文章按 Product Updates、Open Source、Interrupt、Speak the Lang、Events、Customer & integration highlights 聚合，把生态进展压成一组可扫描信号。

## 49. announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust

- URL: https://www.langchain.com/blog/announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust
- Local: agent-04/announcing-the-langchain-mongodb-partnership-the-ai-agent-stack-that-runs-on-the-database-you-already-trust/index.html
- Date: March 31, 2026
- Type: partner announcement
- 为什么：agent 原型进入生产后会遇到持久状态、企业数据检索、结构化查询、部署和观测问题，而这些数据通常已经在 MongoDB Atlas 里。
- 是什么：LangChain 与 MongoDB 合作，把 Atlas Vector Search、MongoDB Checkpointer、Text-to-MQL、LangSmith observability 和 LangGraph/LangChain 集成成一套 agent backend。
- 怎么做到：LangChain 侧提供 retriever、agent state、query generation、deployment 和 tracing 链路；MongoDB Atlas 承接向量搜索、 operational data、memory 与企业数据层。

## 50. better-harness-a-recipe-for-harness-hill-climbing-with-evals

- URL: https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals
- Local: agent-04/better-harness-a-recipe-for-harness-hill-climbing-with-evals/index.html
- Date: April 8, 2026
- Type: technical longform
- 为什么：agent 质量往往不是只改模型就能提升，真正可更新的是 harness；但 autonomous harness improvement 需要可靠学习信号。
- 是什么：Better-Harness 把 evals 当作 harness engineering 的训练数据，用数据 sourcing、实验设计、优化、review & acceptance 形成 hill-climbing loop。
- 怎么做到：系统从真实失败、人工 curated evals 和 traces 中构造信号，约束过拟合，保存长期 traces，并让 agent 提议 harness changes 后进入人工 review。

## 51. traces-start-agent-improvement-loop

- URL: https://www.langchain.com/blog/traces-start-agent-improvement-loop
- Local: agent-04/traces-start-agent-improvement-loop/index.html
- Date: March 31, 2026
- Type: technical longform
- 为什么：agent 出错时，代码只能说明它被允许做什么，不能说明某次运行实际发生了什么；系统性改进需要运行证据。
- 是什么：文章把 trace 定义为 agent improvement loop 的原材料：collect traces、enrich with evals/human feedback、identify patterns、make targeted changes、validate before shipping。
- 怎么做到：LangSmith 用 online evaluators、insights/reports、annotation queues 和 offline eval datasets 把 traces 转成可行动数据，再让工程师或 coding agents 改 prompt、context、orchestration 或模型。

## 52. agent-evaluation-readiness-checklist

- URL: https://www.langchain.com/blog/agent-evaluation-readiness-checklist
- Local: agent-04/agent-evaluation-readiness-checklist/index.html
- Date: March 27, 2026
- Type: technical longform / checklist
- 为什么：agent evaluation 和传统测试不同，需要先看运行轨迹、失败模式和行为目标；直接堆测试会得到脆弱信号。
- 是什么：文章给出 agent eval checklist，覆盖 error analysis、dataset construction、grader design、offline/online evals、iteration 和 production readiness。
- 怎么做到：先用少量 end-to-end eval 建 baseline，再从 traces 和人工分析构建数据集；grader 明确 rubric 和边界；offline eval 支持迭代，online eval 监控生产行为。

## 53. customers-kensho

- URL: https://www.langchain.com/blog/customers-kensho
- Local: agent-04/customers-kensho/index.html
- Date: March 26, 2026
- Type: case study
- 为什么：金融数据分散在多个系统中，专业用户花大量时间查找、验证和整合信息；AI agent 若没有可信数据层，答案很难被信任。
- 是什么：Kensho 用 LangGraph 构建 Grounding multi-agent framework，为 S&P Global 数据提供统一 agentic access layer，并通过 Data Retrieval Agents 连接不同数据源。
- 怎么做到：系统以 centralized entry point 接收查询，router 聚合多个单职责 DRA 的结果，使用 custom data retrieval protocol 保持来源、结构和可验证性。

## 54. how-middleware-lets-you-customize-your-agent-harness

- URL: https://www.langchain.com/blog/how-middleware-lets-you-customize-your-agent-harness
- Local: agent-04/how-middleware-lets-you-customize-your-agent-harness/index.html
- Date: March 26, 2026
- Type: technical explainer
- 为什么：标准 agent loop 很简洁，但生产场景常需要 PII 检测、工具选择、上下文管理等应用特定逻辑；只改 prompt 和 tools 不够。
- 是什么：LangChain middleware 提供 hooks，让开发者在 agent harness 的关键步骤前后插入自定义逻辑，同时保留 create_agent 和 Deep Agents 的基础结构。
- 怎么做到：middleware 可以围绕 model call、tool call、state/context 处理等位置工作；Deep Agents 自身也通过 middleware 组合出 planner、filesystem、subagents 等能力。

## 55. how-we-build-evals-for-deep-agents

- URL: https://www.langchain.com/blog/how-we-build-evals-for-deep-agents
- Local: agent-04/how-we-build-evals-for-deep-agents/index.html
- Date: March 26, 2026
- Type: technical longform
- 为什么：Deep Agents 的行为由 evals 牵引；如果 eval 数据和指标不贴近生产行为，分数提升可能只是错觉。
- 是什么：文章介绍 LangChain 如何为 Deep Agents 构建 targeted evals：从 dogfooding、traces 和真实失败中取样，按行为分组，并用 LangSmith 共享 traces 反复分析。
- 怎么做到：团队先 catalog 生产中重要行为，再围绕文件检索、多步工具调用等行为写 eval；每次 eval run 都 trace 到 LangSmith，团队据此调整 prompt、tool description 或 harness。

## 56. How Moda Builds Production-Grade AI Design Agents with Deep Agents

- URL: https://www.langchain.com/blog/how-moda-builds-production-grade-ai-design-agents-with-deep-agents
- Local: agent-05/how-moda-builds-production-grade-ai-design-agents-with-deep-agents/index.html
- Date: March 24, 2026
- Type: 案例
- 为什么：AI 做视觉设计的难点不是生成一张漂亮图，而是让非设计师在品牌、版式和多轮修改里保持控制。
- 是什么：Moda 用 Deep Agents、LangSmith 和可编辑 2D 矢量画布，把专业级演示文稿、社媒图、手册和 PDF 变成可协作的 agent 工作流。
- 怎么做到：系统把工作分给设计、研究、品牌三类 agent，并通过自定义布局表示、动态技能与工具加载、按画布规模调节上下文来控制质量、成本和延迟。

## 57. Agent observability needs feedback to power learning

- URL: https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning
- Local: agent-05/agent-observability-needs-feedback-to-power-learning/index.html
- Date: May 5, 2026
- Type: 薄观点文
- 为什么：只看 trace 能定位 agent 做了什么，却无法判断结果是否有用。
- 是什么：文章把 agent observability 的核心从调试扩展为学习：trace 加 feedback 才能形成改进信号。
- 怎么做到：团队把用户反馈、行为信号、LLM-as-judge 和规则检查贴到同一条 run、trace 或 thread 上，再用这些信号改模型、harness、context、评测集和规则。

## 58. Continual learning for AI agents

- URL: https://www.langchain.com/blog/continual-learning-for-ai-agents
- Local: agent-05/continual-learning-for-ai-agents/index.html
- Date: April 5, 2026
- Type: 薄观点文
- 为什么：continual learning 不该只等同于更新模型权重，因为 agent 的行为还由运行框架和上下文共同决定。
- 是什么：文章把 agent 学习拆成 model、harness、context 三层，每层都有不同的改进对象和风险。
- 怎么做到：团队用 traces 驱动模型训练、harness 优化和 memory 更新，并按 agent、用户或组织层级管理 context。

## 59. Join LangChain at Google Cloud Next 2026

- URL: https://www.langchain.com/blog/join-langchain-at-google-cloud-next-2026
- Local: agent-05/join-langchain-at-google-cloud-next-2026/index.html
- Date: March 23, 2026
- Type: 活动公告
- 为什么：参会者需要快速判断 LangChain 在 Google Cloud Next 2026 能提供哪些 agent 生产化帮助。
- 是什么：文章给出 Booth #5006、LangSmith 产品演示、Harrison Chase 会面和两场 session。
- 怎么做到：现场路径被组织为展台技术交流、路线图对话和围绕安全 runtime 与开放生态的 breakout session。

## 60. Two different types of agent authorization

- URL: https://www.langchain.com/blog/two-different-types-of-agent-authorization
- Local: agent-05/two-different-types-of-agent-authorization/index.html
- Date: March 23, 2026
- Type: 薄观点文
- 为什么：agent 调用企业工具时，最危险的模糊地带是它以谁的身份取数和行动。
- 是什么：文章把授权拆成两类：Assistant 代表最终用户，Claw 使用 agent 自己的固定凭证。
- 怎么做到：LangSmith Fleet 用渠道身份映射、共享权限和 human-in-the-loop guardrails，把这两类 agent 放进不同使用场景。

## 61. Your harness, your memory

- URL: https://www.langchain.com/blog/your-harness-your-memory
- Local: agent-05/your-harness-your-memory/index.html
- Date: April 11, 2026
- Type: 薄观点文
- 为什么：agent memory 决定体验是否持续变好，但 memory 不是可随意替换的插件。
- 是什么：文章主张 harness 和 memory 绑定在一起，封闭 harness 会把长期记忆、压缩摘要和上下文策略锁进单一平台。
- 怎么做到：它从 Agent = Model + Harness 出发，比较 stateful API、闭源 harness 和完整托管 harness 的可见性与迁移风险。

## 62. Introducing LangSmith Fleet

- URL: https://www.langchain.com/blog/introducing-langsmith-fleet
- Local: agent-05/introducing-langsmith-fleet/index.html
- Date: March 19, 2026
- Type: release
- 为什么：自然语言创建 agent 降低了门槛，也把治理焦点推到分享、凭证和审计。
- 是什么：LangSmith Fleet 是企业工作区，用来创建、使用和管理一组带 memory、tools、skills 和 channel 的 agents。
- 怎么做到：它用 clone/run/edit 权限、Claw/Assistant 凭证模型、Slack bot identity、Inbox 审批和 tracing 形成管理闭环。

## 63. Polly is generally available everywhere you work in LangSmith

- URL: https://www.langchain.com/blog/polly-langsmith-ga
- Local: agent-05/polly-langsmith-ga/index.html
- Date: March 18, 2026
- Type: release
- 为什么：agent 调试的难点是失败原因藏在很长的 trace、prompt 和 conversation 中。
- 是什么：Polly GA 后出现在 LangSmith 所有页面，能保持跨页面上下文并直接采取行动。
- 怎么做到：它读取 trace/thread/experiment/evaluator 的当前上下文，帮助定位失败、写评估器、比较实验和修改 prompt。

## 64. Open SWE: An Open-Source Framework for Internal Coding Agents

- URL: https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents
- Local: agent-05/open-swe-an-open-source-framework-for-internal-coding-agents/index.html
- Date: March 17, 2026
- Type: 技术长文
- 为什么：多家公司内部 coding agent 已经收敛到相似生产架构，但每家从零搭建成本高。
- 是什么：Open SWE 是基于 Deep Agents 和 LangGraph 的开源框架，复用 sandbox、curated tools、workflow invocation 和 orchestration 模式。
- 怎么做到：它用持久云 sandbox、AGENTS.md + source context、subagents、middleware safety nets，把 Slack、Linear 和 GitHub 请求变成可审查的 PR 工作流。

## 65. Introducing deploy cli

- URL: https://www.langchain.com/blog/introducing-deploy-cli
- Local: agent-05/introducing-deploy-cli/index.html
- Date: March 16, 2026
- Type: release
- 为什么：agent 上线不该卡在手动搭 Docker 和基础设施。
- 是什么：deploy cli 在 langgraph-cli 中提供 langgraph deploy、list、logs、delete 等命令。
- 怎么做到：它为本地 LangGraph 项目构建 Docker image，并配置 Postgres 持久化与 Redis streaming，方便接入 GitHub Actions、GitLab CI 或 Bitbucket Pipelines。

## 66. LangChain Announces Enterprise Agentic AI Platform Built with NVIDIA

- URL: https://www.langchain.com/blog/nvidia-enterprise
- Local: agent-05/nvidia-enterprise/index.html
- Date: March 16, 2026
- Type: 合作公告
- 为什么：企业 agent 从原型走向生产时，瓶颈常是基础设施、观测、部署和模型选择。
- 是什么：LangChain 与 NVIDIA 发布企业 agentic AI 平台，把 LangSmith、开源框架、NVIDIA Agent Toolkit、Nemotron、NIM 和 NeMo 组合成完整栈。
- 怎么做到：平台按 build、accelerate、deploy、monitor、evaluate 覆盖生命周期，并用 LangSmith traces 与 NeMo telemetry 连接应用级和基础设施级视图。

## 67. How Coding Agents Are Reshaping Engineering, Product and Design

- URL: https://www.langchain.com/blog/how-coding-agents-are-reshaping-engineering-product-and-design
- Local: agent-05/how-coding-agents-are-reshaping-engineering-product-and-design/index.html
- Date: March 10, 2026
- Type: 薄观点文
- 为什么：当 coding agents 让初版代码非常便宜，EPD 的核心工作不再只是把 PRD 交给工程实现。
- 是什么：文章认为瓶颈转向 review，Product、Engineering、Design 都要判断原型是否架构合理、解决真实痛点且易用。
- 怎么做到：团队用更快的 prototype 作为讨论对象，让 generalists 和高 product sense 的 reviewer 决定哪些代码进入产品。

## 68. The Anatomy of an Agent Harness

- URL: https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
- Local: agent-05/the-anatomy-of-an-agent-harness/index.html
- Date: March 10, 2026
- Type: 技术长文
- 为什么：原始模型不能持久记忆、访问实时知识、搭环境或执行复杂工作。
- 是什么：文章把 agent 定义为 Model + Harness，harness 是模型之外的代码、配置和执行逻辑。
- 怎么做到：它从期望行为倒推组件：filesystem、sandbox、tools、skills、MCPs、planning、subagents、middleware 和约束共同把模型智能变成 work engine。

## 69. Autonomous context compression

- URL: https://www.langchain.com/blog/autonomous-context-compression
- Local: agent-05/autonomous-context-compression/index.html
- Date: March 11, 2026
- Type: 技术长文
- 为什么：固定阈值压缩上下文会忽略工作节奏，可能在复杂工作中间发生。
- 是什么：Deep Agents 增加 context compression tool，让模型在合适时机主动压缩自己的工作记忆。
- 怎么做到：agent 在工作边界、提取结论后、读取大量新上下文前或进入多步流程前，把旧消息压成保留进度的 summary。

## 70. Evaluating Skills

- URL: https://www.langchain.com/blog/evaluating-skills
- Local: agent-06/evaluating-skills/index.html
- Date: March 5, 2026
- Type: 技术长文
- 为什么：技能会改变编码 agent 的行为，凭感觉判断很容易漏掉退化。
- 是什么：LangChain 把技能评估做成一组可对照的实验：无技能、全技能、合并技能、拆分技能。
- 怎么做到：在干净沙箱中运行固定用例，用完成率、调用率、轮次和耗时衡量结果，再用 LangSmith 追踪每一步失败原因。

## 71. LangChain Skills

- URL: https://www.langchain.com/blog/langchain-skills
- Local: agent-06/langchain-skills/index.html
- Date: March 4, 2026
- Type: release / 薄观点文
- 为什么：通用编码 agent 在 LangChain 生态里会缺少领域操作知识。
- 是什么：LangChain 发布 11 个按需加载的 skills，把 LangChain、LangGraph、Deep Agents 的构建经验打包给 coding agent。
- 怎么做到：通过 markdown、脚本和资源做渐进披露，并用 LangSmith evals 对比通过率，从 25% 提升到 95%。

## 72. LangSmith CLI & Skills

- URL: https://www.langchain.com/blog/langsmith-cli-skills
- Local: agent-06/langsmith-cli-skills/index.html
- Date: 2026-03-04
- Type: release / 薄观点文
- 为什么：LangSmith 的调试、数据集和评估流程正在进入 terminal-first 的 agent 开发循环。
- 是什么：LangChain 发布 LangSmith CLI 与 3 个 LangSmith skills，让 Claude Code 在基础 LangSmith 任务上的通过率从 17% 升到 92%。
- 怎么做到：CLI 负责抓 traces、整理 datasets、运行 experiments；skills 用渐进披露提供 trace、dataset、evaluator 三类操作指南。

## 73. February 2026: LangChain Newsletter

- URL: https://www.langchain.com/blog/febraury-2026-langchain-newsletter
- Local: agent-06/febraury-2026-langchain-newsletter/index.html
- Date: 2026-03-03
- Type: newsletter
- 为什么：2 月动态集中在把 agent 从实验推向日常构建、监控和活动社区。
- 是什么：本期聚合 Agent Builder 更新、trace 表格配置、Insights Agent 报告、experiment baseline、deepagents v0.4 sandbox、Interrupt 2026 和 monday.com 案例。
- 怎么做到：LangChain 用产品小步发布、技术文章、课程和线下 meetup，把 Agent Builder、LangSmith observability/evals 与生产经验连接起来。

## 74. How we built Agent Builder's memory system

- URL: https://www.langchain.com/blog/how-we-built-agent-builders-memory-system
- Local: agent-06/how-we-built-agent-builders-memory-system/index.html
- Date: 2026-02-21
- Type: 技术长文
- 为什么：Agent Builder 面向重复执行同类任务的自定义 agent，没有记忆会让用户在不同会话里反复校正同一件事。
- 是什么：LangChain 把记忆实现为 agent 可读写的文件形态，并映射到 COALA 的 procedural、semantic、episodic 记忆分类。
- 怎么做到：底层用 Postgres 存储并暴露成虚拟文件系统，AGENTS.md、skills、tools.json 和知识文件分别承载指令、专门知识与工具配置，所有记忆更新通过人工确认降低注入风险。

## 75. How to Use Memory in Agent Builder

- URL: https://www.langchain.com/blog/how-to-use-memory-in-agent-builder
- Local: agent-06/how-to-use-memory-in-agent-builder/index.html
- Date: 2026-02-19
- Type: 薄观点文 / how-to
- 为什么：Agent Builder 的记忆会随着反馈变好，但用户需要理解怎样把短期对话沉淀成长期行为。
- 是什么：文章给出三种用法：让 agent 记住有效做法、用 skills 承载专门上下文、直接查看和编辑记忆文件。
- 怎么做到：短期文件只存在当前 thread，长期文件保存在 `/memories/`；agent 会把明确反馈写入 markdown 指令或按主题创建 skill，并在保存前请求用户确认。

## 76. monday Service + LangSmith: Building a Code-First Evaluation Strategy from Day 1

- URL: https://www.langchain.com/blog/customers-monday
- Local: agent-06/customers-monday/index.html
- Date: 2026-02-18
- Type: 案例
- 为什么：monday Service 的 ReAct service agents 会在多步推理和工具调用中级联出错，质量不能等 Alpha 用户发现。
- 是什么：团队把 evaluations 作为 Day 0 要求，形成 offline safety net 与 online monitor 两层体系，并把反馈循环从 162 秒压到 18.6 秒，快 8.7 倍。
- 怎么做到：offline 层用 LangSmith + Vitest 跑 curated datasets、deterministic checks 和 LLM-as-judge；online 层用 Multi-Turn Evaluators 评估生产会话，并把 judges 作为 TypeScript 代码通过 CI/CD 同步到 LangSmith。

## 77. New in Agent Builder: all new agent chat, file uploads + tool registry

- URL: https://www.langchain.com/blog/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry
- Local: agent-06/new-in-agent-builder-all-new-agent-chat-file-uploads-tool-registry/index.html
- Date: 2026-02-18
- Type: release / 产品更新
- 为什么：创建专门 agent 之前，用户常常只想先用已有工具完成一个临时任务。
- 是什么：Agent Builder 新增常驻 Chat、conversation-to-agent、文件上传和统一 tool registry，把即兴工作和可复用 agent 创建接在一起。
- 怎么做到：Chat 可调用 workspace 中 Slack、Gmail、Linear、Pylon 或 remote MCP server 等工具，任务过程中请求审批；有效对话可一键变成手动、定时或事件触发的 agent。

## 78. Improving Deep Agents with harness engineering

- URL: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
- Local: agent-06/improving-deep-agents-with-harness-engineering/index.html
- Date: 2026-02-17
- Type: 技术长文
- 为什么：模型能力很强但输出尖峰明显，agent 质量常由 prompt、tools、middleware 等 harness 决定。
- 是什么：LangChain 在模型固定为 gpt-5.2-codex 的情况下，仅通过 harness engineering 让 deepagents-cli 在 Terminal Bench 2.0 从 52.8 提升到 66.5。
- 怎么做到：他们用 LangSmith traces 做失败分析，围绕 self-verification、环境上下文注入、loop detection 和 reasoning budget 调整迭代。

## 79. Join us for Interrupt: The Agent Conference

- URL: https://www.langchain.com/blog/join-us-for-interrupt-the-agent-conference
- Local: agent-06/join-us-for-interrupt-the-agent-conference/index.html
- Date: 2026-02-12
- Type: event / 薄观点文
- 为什么：LangChain 想把过去一年客户、伙伴和 builder 的 agent 生产经验集中到一个线下场景。
- 是什么：Interrupt 将于 2026 年 5 月 13-14 日在 San Francisco 的 The Midway 举办，议程覆盖 keynote、企业案例、新产品首发、workshops、builder conversations 和 sponsor demos。
- 怎么做到：Harrison Chase、Andrew Ng 及 Clay、Rippling、Monday.com 等团队会分享经验，LangChain product experts 负责 hands-on workshops。

## 80. On Agent Frameworks and Agent Observability

- URL: https://www.langchain.com/blog/on-agent-frameworks-and-agent-observability
- Local: agent-06/on-agent-frameworks-and-agent-observability/index.html
- Date: 2026-02-12
- Type: 薄观点文 / 架构观点
- 为什么：agent frameworks 常被质疑会被模型进步淘汰，但团队仍需要更快构建、更少重复代码和可生产化路径。
- 是什么：LangChain 的立场是 frameworks 仍有用，但要随模型演进；同时 LangSmith observability 与 evals 不绑定 LangChain 或 LangGraph。
- 怎么做到：LangChain 把 framework 演进分为 chaining、LangGraph runtime、Deep Agents harness 三代，并让 LangSmith 通过多框架集成和 OpenTelemetry tracing 支持任意 agent。

## 81. The two patterns by which agents connect sandboxes

- URL: https://www.langchain.com/blog/the-two-patterns-by-which-agents-connect-sandboxes
- Local: agent-06/the-two-patterns-by-which-agents-connect-sandboxes/index.html
- Date: 2026-02-10
- Type: 技术长文
- 为什么：越来越多 agent 需要一台隔离的 computer 来运行代码、安装包和访问文件，关键问题从是否 sandbox 变成如何连接 sandbox。
- 是什么：文章区分两种架构：Agent IN Sandbox 和 Sandbox as Tool，前者贴近本地开发但密钥和通信复杂，后者隔离 agent state 与执行环境但会引入网络延迟。
- 怎么做到：deepagents 可通过配置支持两种模式；选择依据是环境耦合度、迭代速度、API key 边界、state 分离和 provider 通信能力。

## 82. LangSmith is Now Available in Google Cloud Marketplace

- URL: https://www.langchain.com/blog/langsmith-is-now-available-in-google-cloud-marketplace
- Local: agent-06/langsmith-is-now-available-in-google-cloud-marketplace/index.html
- Date: 2026-02-09
- Type: release / marketplace
- 为什么：企业在 Google Cloud 上构建 AI 应用时，希望采购、计费、合规部署和既有数据基础设施能保持在同一云环境。
- 是什么：LangSmith 已上线 Google Cloud Marketplace，覆盖 observability、evaluation、deployment、Agent Builder，并延续 LangChain 与 Google Cloud 在 Gemini、A2A Protocol、MCP Toolbox for Databases 等方向的合作。
- 怎么做到：客户可通过 marketplace 采购，用现有 Google Cloud invoice 和 committed spend，并在 SaaS、hybrid 或 GKE self-hosted 配置中部署 LangSmith。

## 83. January 2026: LangChain Newsletter

- URL: https://www.langchain.com/blog/january-2026-langchain-newsletter
- Local: agent-07/january-2026-langchain-newsletter/index.html
- Date: January 29, 2026
- Type: newsletter
- 为什么：一月更新回答的是同一个运营问题：agent 不只要更容易搭出来，还要能被观察、评估和持续改进。
- 是什么：本期把 LangSmith Agent Builder GA、实验对比、自托管 Insights Agent、LangChain JS 与 deepagents 更新放在同一条主线上。
- 怎么做到：LangChain 用产品发布、开源改进、课程、支持门户和全球活动，把 agent 构建从一次性上线推进到持续运营。

## 84. Agent observability powers agent evaluation

- URL: https://www.langchain.com/blog/agent-observability-powers-agent-evaluation
- Local: agent-07/agent-observability-powers-agent-evaluation/index.html
- Date: January 27, 2026
- Type: 技术长文
- 为什么：Agent 失败常常藏在多步推理、工具调用、上下文和状态变化里，单看日志很难知道系统为什么偏离目标。
- 是什么：文章的核心判断是 observability 与 evaluation 在 agent 时代合并成同一套闭环：traces 同时支撑调试、测试、线上监控和事后洞察。
- 怎么做到：用 runs 捕获单步决策，用 traces 还原完整轨迹，用 threads 连接多轮上下文，再按 single-step、full-turn、multi-turn 与 offline、online、ad-hoc 粒度评估。

## 85. You don’t know what your agent will do until it’s in production

- URL: https://www.langchain.com/blog/production-monitoring
- Local: agent-07/production-monitoring/index.html
- Date: February 26, 2026
- Type: 技术长文
- 为什么：传统监控假设输入和代码路径相对固定，但 agent 面对自然语言、非确定性模型和多步工具调用，上线后才会暴露真实行为。
- 是什么：文章认为生产监控需要从 latency、error rate 扩展到输入、输出、推理轨迹、工具选择、用户反馈和质量变化。
- 怎么做到：用 LangSmith traces 捕获自然语言交互和工具链路，再把生产数据聚合为在线评价、失败模式、数据集和持续改进信号。

## 86. Deploy agents instantly with Agent Builder templates

- URL: https://www.langchain.com/blog/introducing-agent-builder-template-library
- Local: agent-07/introducing-agent-builder-template-library/index.html
- Date: January 21, 2026
- Type: release
- 为什么：很多团队知道想自动化什么，却不想从空白 prompt 开始连接工具、写指令和调试流程。
- 是什么：Agent Builder Template Library 提供可部署、可定制的预置 agent，并通过 Tavily、PagerDuty、Exa、Box、Arcade 等伙伴覆盖常见工作。
- 怎么做到：模板内置工具连接和 agent instructions，用户可修改指令、增加工具、设置审批，并通过 Arcade MCP Gateway 扩展到 8,000 个工具。

## 87. From Traces to Insights: Understanding Agent Behavior at Scale

- URL: https://www.langchain.com/blog/from-traces-to-insights-understanding-agent-behavior-at-scale
- Local: agent-07/from-traces-to-insights-understanding-agent-behavior-at-scale/index.html
- Date: January 20, 2026
- Type: 技术长文
- 为什么：生产 agent 每天会生成成千上万条 traces，人工逐条阅读无法回答用户如何使用、哪里失败、模式如何变化。
- 是什么：文章把 LangSmith Insights Agent 定位为 agent analytics：它从非结构化对话中发现 usage patterns、error modes 和指定维度的聚类。
- 怎么做到：先用 traces 记录真实交互，再用聚类和探索式分析把海量会话归并为可解释模式，补足传统产品分析和已知问题 eval 的盲区。

## 88. How Remote uses LangChain and LangGraph to onboard thousands of customers with AI

- URL: https://www.langchain.com/blog/customers-remote
- Local: agent-07/customers-remote/index.html
- Date: January 19, 2026
- Type: 案例
- 为什么：Remote 的客户入职涉及大型 HR、薪资和合规数据迁移，直接把 50MB Excel 或 SQL 导出塞进 LLM 会撞上上下文和幻觉风险。
- 是什么：Remote 在 AI Service 中构建 Code Execution Agent，把模型推理和确定性 Python 执行拆开，用于自动化客户数据迁移。
- 怎么做到：LangChain 负责工具调用和多模型抽象，LangGraph 表达节点与边的执行流，WebAssembly Python sandbox 运行 Pandas 转换并只把摘要回传给模型。

## 89. How we built Agent Builder’s memory system

- URL: https://www.langchain.com/blog/how-we-built-agent-builders-memory
- Local: agent-07/how-we-built-agent-builders-memory/index.html
- Date: January 16, 2026
- Type: 技术长文
- 为什么：Agent Builder 面向重复执行同类工作的定制 agent，没有记忆会让用户跨会话反复解释偏好、规则和工具边界。
- 是什么：文章说明 Agent Builder 把记忆设计成文件系统形态，并用 AGENTS.md、skills、tools.json 和知识文件对应 procedural、semantic 等记忆类型。
- 怎么做到：底层并不使用真实文件系统，而是把文件存进 Postgres，再通过 Deep Agents 的 virtual filesystem 暴露给模型，让 agent 能读写记忆并在热路径中更新。

## 90. Choosing the Right Multi-Agent Architecture

- URL: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
- Local: agent-07/choosing-the-right-multi-agent-architecture/index.html
- Date: January 14, 2026
- Type: 技术长文
- 为什么：单 agent 最简单，但当能力数量、上下文和团队边界膨胀时，系统需要更清晰的协调方式来避免 prompt 混乱。
- 是什么：文章给出四种基础架构模式：subagents、skills、handoffs、routers，并用控制权、状态、上下文隔离和延迟成本来区分。
- 怎么做到：从最关键约束反推选择：需要集中控制选 subagents，需要轻量专业化选 skills，需要用户直达专家选 handoffs，需要确定分类选 routers。

## 91. Now GA: LangSmith Agent Builder

- URL: https://www.langchain.com/blog/langsmith-agent-builder-generally-available
- Local: agent-07/langsmith-agent-builder-generally-available/index.html
- Date: January 13, 2026
- Type: release
- 为什么：非开发同事也需要把日常研究、跟进、更新和跨工具操作自动化，但传统 workflow builder 约束先画清每一步。
- 是什么：LangSmith Agent Builder GA，把自然语言目标转成可部署 agent，自动生成指令、选择工具，并在需要时使用 subagents。
- 怎么做到：用户用反馈迭代 agent，借 memory 学习偏好，通过 MCP 接工具、共享克隆、选择模型，并可嵌入产品或 API 调用。

## 92. In software, the code documents the app. In AI, the traces do.

- URL: https://www.langchain.com/blog/in-software-the-code-documents-the-app-in-ai-the-traces-do
- Local: agent-07/in-software-the-code-documents-the-app-in-ai-the-traces-do/index.html
- Date: January 10, 2026
- Type: 薄观点文
- 为什么：传统软件的决策逻辑写在代码里，agent 的关键决策却在模型运行时发生，读代码只能看到脚手架。
- 是什么：文章提出新的 source of truth：traces 才记录 agent 实际做了什么、为什么这么做，以及哪些推理或工具调用导致结果。
- 怎么做到：调试、测试、优化、监控和协作都要围绕 traces 展开，用 trace replay、playground、dataset 和 production monitoring 取代只读代码的工作方式。

## 93. How we built LangChain’s GTM Agent

- URL: https://www.langchain.com/blog/how-we-built-langchains-gtm-agent
- Local: agent-08/how-we-built-langchains-gtm-agent/index.html
- Date: March 9, 2026
- Type: 案例
- 为什么：LangChain 的 GTM 团队需要把分散在 CRM、网页、新闻和内部材料里的公司线索变成可行动的账户研究，而不是让销售手工拼上下文。
- 是什么：文章展示了一个面向 go-to-market 的研究 agent：它围绕目标账户收集资料、生成摘要、识别触发事件，并把结果写回团队使用的业务系统。
- 怎么做到：实现上用 Deep Agents 的文件系统和技能组织长任务，用 LangSmith 观察工具调用和结果质量，并把搜索、内部数据访问、CRM 更新等能力包装成可控工具链。

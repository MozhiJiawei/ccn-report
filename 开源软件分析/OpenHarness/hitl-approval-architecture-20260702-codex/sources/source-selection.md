输入类型：web

原始来源清单：
1. Harness层中人机协同（HITL）设计：Agent高风险操作的审批架构技术线索 — https://juejin.cn/post/7653305987720052782
   选择理由：用户指定的核心文章，直接讨论 Harness 层 HITL 与 Agent 高风险操作审批架构。
2. LangChain Human-in-the-loop — https://docs.langchain.com/oss/python/langchain/human-in-the-loop
   选择理由：官方文档，直接定义并展示 HITL middleware 如何按工具调用策略中断、持久化状态并等待人工决策。
3. OpenAI Agents SDK Human-in-the-loop — https://openai.github.io/openai-agents-python/human_in_the_loop/
   选择理由：官方文档，直接定义并展示工具审批、RunState 序列化、跨 handoff/nested agent 暂停与恢复的实现路径。

对照研究/同类方案清单：
无。三篇均视作原始页面，综合研究 HITL 的定义和实现。

# Graphify

## 一句话总结

Graphify 在 v8 中以本地 tree-sitter 结构解析和可选模型语义抽取，将代码及文档组织为带来源标签的可查询知识图，为编码助手提供可追溯上下文。

## 任务信息

- 序号：124
- 任务编号：TASK-20260912023421-1020964d
- 热点编号：HS-20260912-insight-report-graphify
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/记忆与上下文系统
- 归类依据：主要贡献为关系图组织、检索及上下文提供；skill 是接入形式，研发效率是下游效果，因此归记忆与上下文系统。输入 category 为 null，无指定分类差异。
- 任务正文：Graphify-Labs/graphify — 通过 /graphify skill 接入 Claude Code、Cursor、Codex、Gemini CLI 四款编码助手。架构创新：代码层采用 tree-sitter 本地确定性 AST 解析，零 LLM、零向量存储；文档/PDF/图像走模型语义层；图中每条边带 EXTRACTED/INFERRED 来源标签，区别实读与推断。能力：支持 FastAPI 等大型代码库全量映射为可遍历 graph.html；输入覆盖 codebase、SQL schemas、configs、PDF。Apache-2.0 开源，GitHub ⭐116,997。把代码库转为可查询知识图，本地确定性 + 模型语义混合架构对代码 agent 检索质量提升明显。来源：GitHub。
- 任务来源：[原始任务来源](https://github.com/Graphify-Labs/graphify)

## 交付件说明

- [Graphify.html](./Graphify.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Graphify.pptx](./Graphify.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

官方自测并非独立评测；会话记忆指标不可外推代码任务；ERPNext只有6题且模型声明未核实；README零embedding与基准本地嵌入存在范围差异；来源标签不保证正确性，语义层与问答仍有成本。

## 引用信息源说明

- [Graphify 官方仓库 README](https://github.com/Graphify-Labs/graphify/tree/26b02b5e3430e4ab85dd7e72c7b98836d8e65c48)：项目定位、AST/语义双路径、来源标签、输出与助手接入
- [Graphify 官方基准](https://github.com/Graphify-Labs/graphify/blob/26b02b5e3430e4ab85dd7e72c7b98836d8e65c48/BENCHMARKS.md)：官方自测范围、指标及证据局限

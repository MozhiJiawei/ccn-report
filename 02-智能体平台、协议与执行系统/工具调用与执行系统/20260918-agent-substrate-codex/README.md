# AgentSubstrate

## 一句话总结

截至2026年9月18日的官方材料，Agent Substrate 是面向长时智能体工具执行的开源沙箱运行系统，通过状态快照、休眠释放CPU与内存及预热worker复用，官方称可实现每主机1,000多个休眠智能体、相对传统运行时10倍密度与低于500毫秒恢复，但未披露统一测试口径且开源仓库仍未生产就绪。

## 任务信息

- 序号：137
- 任务编号：TASK-20260916021219-b5377b66
- 热点编号：HS-20260916-dsh-tech-insight
- 周期：2026-W38
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/工具调用与执行系统
- 归类依据：输入category为null，已读取02与08分类细则并核对两项正文；主要贡献是智能体完整计算机环境、沙箱生命周期、工具执行和可靠恢复，直接命中工具调用与执行系统。GKE资源管理与microVM/gVisor隔离是底层承载，作为08板块次要关联，不改变唯一主归属；无调用方指定分类差异。
- 任务正文：📌Google 开源 Agent Substrate：GKE 上 10× 密度、亚 500ms 恢复的智能体运行时
原文标题：Agent Substrate brings high-density, scalable, trusted infrastructure to GKE
元信息：战略 · 2026/09/15 · 编号 #32 · 500ms；Agent Substrate is an open-source, secure-by-defau
要点：
- Agent Substrate 是开源、默认安全的智能体执行运行时，可承载「数百万沙箱、密度达标准容器运行时 10×」Agent Substrate is an open-source, secure-by-default agent execution runtime engineered to run millions of sandboxes with 10x higher density than standard container runtimes
- 工具访问摩擦：智能体需要完整计算机环境以调用命令行工具、无头浏览器与文件系统工作区Tool access friction: Agents need full computer environments to invoke command-line tools, headless browsers, and filesystem workspaces
- 执行层直接管理沙箱化智能体环境生命周期：默认安全——硬件隔离 Cloud Hypervisor microVM 或 gVisor 沙箱，配合出口代理From there, the execution layer directly manages the lifecycle of sandboxed agent environments with: Security by default: Hardware-isolated Cloud Hypervisor microVMs or gVisor sandboxes, paired with egress proxi
技术效果：效果 · 推理强化：架构创新：据 Google Cloud 博客：Agent Substrate 为开源、默认安全的智能体执行运行时，通过「snapshot-to-local-disk-and-Cloud-Storage」挂起/恢复机制实现「每主机 1,000+ 休眠智能体、相对传统容器 10× 算力密度」；据 Google Cloud 博客：性能目标为「亚 500ms 恢复 + 超 500 次挂起/恢复/秒」，底层提供硬件隔离 Cloud Hypervisor microVM 与 gVisor 两种沙箱后端及零信任内核与网络隔离；据 GitHub agent-substrate/substrate：项目为 Apache-2.0、2026-05-13 创建，明确非智能体 SDK 而是规模化运行系统，框架无关并原生支持 ADK、LangChain、Claude Code、CodeX、Antigravity 与 MCP
背景补充：仓库自述「尚处早期开发、未生产就绪、API 几乎必然变更」；Nous Research 为早期设计合作方。
源链接：https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke/
- 任务来源：[原始任务来源](https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke/)

## 交付件说明

- [AgentSubstrate.html](./AgentSubstrate.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [AgentSubstrate.pptx](./AgentSubstrate.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

10倍密度、每主机1000多个休眠智能体、低于500毫秒恢复及每秒超过500次挂起恢复均为官方自报，未给硬件、状态大小、并发和分位数，不能视为独立实测或普遍SLA；休眠密度不等于活跃并发吞吐或模型推理加速。博客说明普通GKE客户面向非生产，生产支持需allowlist；固定提交仓库仍称早期开发、未生产就绪、API不保证兼容且非Google官方支持产品。博客渲染稳定日期为2026-09-16，与任务09-15相差一天。

## 引用信息源说明

- [Google Cloud: Agent Substrate brings high-density, scalable, trusted infrastructure to GKE](https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke/)：支撑执行层架构、快照与恢复生命周期、三项官方自报指标、GKE集成及生产支持边界。
- [Agent Substrate official repository at 8ca99ccec99380a0acb91184eb2fb4ad766a4454](https://github.com/agent-substrate/substrate/tree/8ca99ccec99380a0acb91184eb2fb4ad766a4454)：支撑actor/worker复用机制、框架无关定位、演示边界与早期开发/API兼容性声明；2026-09-18读取。

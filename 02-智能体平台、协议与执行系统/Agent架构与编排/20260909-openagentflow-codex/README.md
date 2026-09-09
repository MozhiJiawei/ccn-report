# OpenAgentFlow

## 一句话总结

OpenAgentFlow 是面向异构智能体协作的执行前策略检查架构，2026 年 9 月 2 日 arXiv v2 通过 AgentEvent 与共享 PEP 统一接入动作的规则、来源和会话上下文，在 300 例受控套件中取得 94.00% 判定准确率和 95.35% 攻击拦截率，为已接入执行路径提供跨动作约束，并以 Android 模拟器实验验证部分执行场景。

## 任务信息

- 序号：71
- 任务编号：TASK-20260909014558-e21d6caa
- 热点编号：HS-20260909-openagentflow
- 周期：2026-W37
- 指定分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：严格遵循任务指定分类；正文以控制面、动作面和共享执行前边界组织异构智能体治理，亦关联工具调用与执行系统和 AI 安全，但不改变调用方指定的 Agent架构与编排 归属。
- 任务正文：OpenAgentFlow 提出控制面/动作面（control-plane/action-plane）架构，在异构智能体中实现 94% 动作级安全拦截。arXiv 论文 2609.00015v2：将 GUI/API/Tool/LLM 动作统一归一为 AgentEvent 流，由共享的 pre-execution Policy Enforcement Point (PEP) 拦截；300 例受控套件 94.00% accuracy + 95.35% attack-block rate；AgentDojo-Traj (TS-Bench, 1220 例) 97.62% accuracy, 96.59% unsafe-action recall, 1.96% safe false-intervention rate；支持 post-deployment policy 更新；已实测真机 Android。
- 任务来源：[原始任务来源](https://arxiv.org/pdf/2609.00015v2)

## 交付件说明

- [OpenAgentFlow.html](./OpenAgentFlow.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [OpenAgentFlow.pptx](./OpenAgentFlow.pptx)：基于已验收来源理解报告的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [OpenAgentFlow: Enabling System-Wide Safety Boundaries for Heterogeneous AI Agent Fleets](https://arxiv.org/abs/2609.00015v2)：支撑 AgentEvent、共享 PEP、分阶段判定与控制面架构，以及受控、AgentDojo-Traj 和 Android 模拟器结果；纠正任务摘要中准确率与拦截率混用及物理真机表述。

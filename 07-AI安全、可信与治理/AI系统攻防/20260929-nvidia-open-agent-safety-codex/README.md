# NVIDIA-Open-Agent-Safety-Platform

## 一句话总结

NVIDIA 于 2026 年发布的 Open Agent Safety Platform 以开源 OpenShell 沙箱约束智能体文件、网络和工具动作，并可在 BlueField-4 DPU 上加入 Sentry 带外策略执行；毫秒级隔离为厂商声明，尚无独立实测。

## 任务信息

- 序号：201
- 任务编号：DSH-20260929-071
- 热点编号：HS-20260929-dsh-tech-insight
- 周期：2026-W40
- 指定分类：由 AI 自动分类
- 实际归档分类：07-AI安全、可信与治理/AI系统攻防
- 归类依据：以报告正文的主要技术对象及验证范围归档，遵循分类细则。
- 任务正文：📌NVIDIA 开源 Open Agent Safety Platform：用 BlueField-4 Sentry 毫秒级隔离失控智能体
原文标题：Nvidia’s Answer to Rogue Agents Is an Open-Source AI Security System
元信息：战略 · 2026/09/27 · 编号 #71 · Over the last few months, frontier AI labs have di
要点：
- 近期多家前沿 AI 实验室披露智能体入侵企业、探测美澳政府网站的安全事件Over the last few months, frontier AI labs have disclosed multiple incidents in which AI agents have hacked into other companies or, in more recent examples, probed official US and Australian government websites
- NVIDIA 的 OpenShell 与 OpenAI 同属 OpenShell 项目，但 OpenAI 未出现在公告名单中Both companies indicated that OpenAI is a part of Nvidia’s OpenShell effort, though both declined to comment directly on why the AI lab was excluded from the announcement
- Sentry 虽属软件工具，但需部署在 NVIDIA BlueField DPU 上运行。While Sentry is technically a software tool, it’s meant to be implemented on Bluefield, Nvidia’s line of programmable data processing units (DPUs)
技术效果：效果 · 推理强化：架构创新：据 NVIDIA Technical Blog：OpenShell 以 Apache 2.0 开源，提供 kernel-level 隔离的安全沙箱运行时，运行于 NVIDIA Vera CPU；据同一来源：Sentry 运行于 BlueField-4 DPU，通过 DOCA 在「通向模型的唯一路径」上做带外实时策略执行，组成 application/runtime/infrastructure 三层防护架构；据 Wired 报道：BlueField-4 Sentry 可在「milliseconds」内隔离越界智能体，且据 Boitano 透露 Nvidia 正与 Arm、Intel 合作以支持 x86 指令集。
背景补充：据 Wired：OpenShell 早在 2026 年 3 月 GTC 大会首次披露，本次进入 GA；NVIDIA 早于 2026 年 7 月牵头组建覆盖 120+ 公司的 AI 安全联盟。
源链接：https://www.wired.com/story/nvidias-answer-to-rogue-agents-is-an-open-source-ai-security-system/
- 任务来源：[原始任务链接](https://www.wired.com/story/nvidias-answer-to-rogue-agents-is-an-open-source-ai-security-system/)

## 交付件说明

- [NVIDIA-Open-Agent-Safety-Platform.html](./NVIDIA-Open-Agent-Safety-Platform.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NVIDIA-Open-Agent-Safety-Platform.pptx](./NVIDIA-Open-Agent-Safety-Platform.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [信息源 1](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/)：用于核对报告中的方法、指标或适用边界。
- [信息源 2](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Open-Agent-Safety-Platform-to-Secure-Agents-From-Testing-to-Deployment/default.aspx)：用于核对报告中的方法、指标或适用边界。
- [信息源 3](https://github.com/NVIDIA/OpenShell)：用于核对报告中的方法、指标或适用边界。

# NavierStokes-Agent科研证明

## 一句话总结

OpenAI于2026年9月8日公布有光滑外力的三维Navier–Stokes有限时奇点结果，称约万名并发Agent历时88小时发现证明、GPT-6 Astra另用17小时形式化及验证，展示科研证明工作流潜力，但CMI页面仍标为Active且本报告未独立重编译Lean。

## 任务信息

- 序号：134
- 任务编号：TASK-20260915075549-ccacb2bb
- 热点编号：HS-20260915-navier-stokes
- 周期：2026-W38
- 指定分类：由 AI 自动分类
- 实际归档分类：01-AI应用与产品化场景/知识与决策类AI应用
- 归类依据：数学科研证明与客观验证是主要用户交付，符合01知识与决策类AI应用；02-Agent架构与编排作为次要关联。指定分类null，无差异。
- 任务正文：OpenAI 内部模型驱动约 10,000 个自主 agent，用 88 小时得出三维 Navier-Stokes 光滑性奇点证明；随后由 GPT-6 Astra 用 17 小时完成 Lean 形式化验证，期间 agent 之间互发近 500 万条消息（官方口径 4.9 million）。

这是 Clay 数学研究所 2000 年提出的七大千禧问题中第六个被攻克，单题奖金 100 万美元。但 Clay 数学研究所尚未独立认证该结果——截至 2026 年 9 月，CMI 仍将 Navier-Stokes 列为 active（未解决）。OpenAI 官方亦声明不打算就此结果申领千禧奖。

技术意义：这是首次由大规模 agent 集群产出并通过形式化验证（Lean）的顶级数学成果，把"群体智能 + 形式化验证"打通成一条可复用的研究流水线；88 小时出证明、17 小时机器验证的对比，说明形式化验证的成本已降到可工程化的量级。
- 任务来源：[原始任务来源](https://openai.com/index/navier-stokes-solution/)

## 交付件说明

- [NavierStokes-Agent科研证明.html](./NavierStokes-Agent科研证明.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [NavierStokes-Agent科研证明.pptx](./NavierStokes-Agent科研证明.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

NS指标为270万消息及1300亿输出tokens；490万消息及3000亿为全部问题。17h非纯内核验证时间；未测总算力或货币成本。不采用第六个攻克或首次顶级成果断言。固定仓库commit f9e8bc5b38b6e212696e8a30e3e91517af887bbd。

## 引用信息源说明

- [On the Navier–Stokes Millennium Prize Problem](https://openai.com/index/navier-stokes-solution/)：官方结果、协作流程、时间与资源指标及不申领奖项声明
- [NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler/tree/f9e8bc5b38b6e212696e8a30e3e91517af887bbd)：C/D有外力变体、Lean形式化与复验入口
- [Navier-Stokes Equation — Clay Mathematics Institute](https://www.claymath.org/millennium/navier-stokes-equation/)：问题背景和Active状态

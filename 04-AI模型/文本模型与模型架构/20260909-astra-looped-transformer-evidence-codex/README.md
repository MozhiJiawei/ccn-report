# Astra-循环深度证据

## 一句话总结

循环 Transformer 是一种面向语言模型、通过复用同组权重反复更新隐状态来增加有效计算深度的方法，Raschka 于 2026 年 9 月 2 日以 22 层复用两轮的例子解释其参数与计算权衡，而截至 9 月 3 日已核对的 OpenAI 公告与系统卡尚未正式确认 Astra 采用该架构，因而本报告将机制解释、官方能力评测与监控结论分开呈现。

## 任务信息

- 序号：72
- 任务编号：TASK-20260909015130-039b9c6f
- 热点编号：HS-20260909-openai-astra
- 周期：2026-W37
- 指定分类：04-AI模型/文本模型与模型架构
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：严格遵循任务指定的文本模型与模型架构分类，主要解释共享层循环与计算深度；安全能力及监控结果仅用于区分证据等级和架构因果边界，不改归安全评测板块。
- 任务正文：OpenAI Astra 采用循环深度（recurrent depth / looped transformer）架构，用计算深度换参数规模：把同一组 Transformer 层重复执行多次处理同一段文本，权重不复制但有效深度成倍增加。The Information 2026-09-01 首发报道，OpenAI 未在 system card 正式确认。类似方案包括 Nanbeige 4.2（22 层堆栈复用 2 次 → 等效 44 层、3B 参数 28T tokens 预训练）、Mixture-of-Recursions（token 级路由递归）。Astra 已确认事实：首个达到 Critical cybersecurity 阈值；ExploitBench 100%、发现两个 0day；91.5% 拒绝 disallowed cyber 请求（vs GPT-5.6 Sol 59%）；附加强 CoT 监控。Sebastian Raschka 等独立分析指出：latent computation 增加 → 监控可读性下降 → 监控对齐能力减弱。
- 任务来源：[原始任务来源](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)

## 交付件说明

- [Astra-循环深度证据.html](./Astra-循环深度证据.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Astra-循环深度证据.pptx](./Astra-循环深度证据.pptx)：基于已验收来源理解报告的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [OpenAI Astra and Looped Transformers](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)：作为作者原始技术评论，支撑共享层循环机制、Nanbeige 例子及循环不必然隐藏思维链的澄清；不作为 Astra 内部架构的官方确证。
- [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra/)：支撑 2026 年 9 月 1 日的 Critical cyber 认定、ExploitBench 与 Internal Port 评测对象，以及 Daybreak Blue 配置限定；不将特定测试结果扩展为任意现实系统的表现。
- [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)：支撑 2026 年 9 月 3 日系统卡的监控输入范围、非对抗与对抗评测、Figure 22、思维链缩短及监控性变化；区分 CoT-only、action-only、full-context 与模型对齐行为。

## 核验说明

The Information 原始报道未在本轮直接访问，不作为独立确证；Nanbeige 与 Mixture-of-Recursions 只作为原作者的机制例子，不进行模型横评。系统卡静态正文和图表已核对，未从抓取未保留的交互控件推断数字；本报告没有建立循环架构导致监控退化的因果关系。

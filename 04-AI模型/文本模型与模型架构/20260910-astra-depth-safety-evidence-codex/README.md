# Astra-循环深度与安全评测边界

## 一句话总结

截至2026年9月10日本轮核验，循环深度通过复用同一Transformer层堆栈增加执行深度而不复制该堆栈权重，Astra采用该架构仍未经官方确认，官方公开ExploitBench的100%和网络越狱评估集91.5%的拒绝率须按各自评测条件理解，用于区分架构推测与已披露能力证据。

## 任务信息

- 序号：73
- 任务编号：TASK-20260909070627-09c2bbd9
- 热点编号：HS-20260909-openai-astra-v2
- 周期：2026-W37
- 指定分类：04-AI模型/文本模型与模型架构
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：主对象为文本模型的循环深度架构及其证据边界，安全评测与监控作为关联内容；严格遵循指定二级分类。
- 任务正文：OpenAI Astra 采用循环深度（recurrent depth / looped transformer）架构，用计算深度换参数规模：同一组 Transformer 层被重复执行多次（典型如 22 层堆栈复用 2 次 → 等效 44 层），权重不复制但有效深度成倍增加，类似 Nanbeige 4.2 与 Mixture-of-Recursions。模型在准确率和安全能力上同时取得提升——能力维度：Astra 首个达到 Critical cybersecurity 阈值；ExploitBench 100%，评估中发现两个 0day；computation-graph depth within 2× of GPT-4。安全维度：拒绝 disallowed cyber 请求从 GPT-5.6 Sol 的 59% 提升至 91.5%；附带额外 chain-of-thought 监控。The Information 2026-09-01 报道 OpenAI 采用此架构，OpenAI 在 system card 中未正式确认，独立分析师 Raschka 提示 latent computation 增加 → 监控可读性下降 → 监控对齐能力减弱，需关注可解释性回退。
- 任务来源：[原始任务来源](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)

## 交付件说明

- [Astra-循环深度与安全评测边界.html](./Astra-循环深度与安全评测边界.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Astra-循环深度与安全评测边界.pptx](./Astra-循环深度与安全评测边界.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

证据边界：22层复用两次是Nanbeige示例；公开ExploitBench与内部20漏洞移植版分开，Daybreak Blue注释显式对应内部评测图；没有证据证明循环架构导致能力、拒答或监控变化。

## 引用信息源说明

- [OpenAI Astra and Looped Transformers](https://sebastianraschka.com/blog/2026/openai-astra-looped-transformers.html)：支持通用循环深度原理、Nanbeige示例及架构报道的证据边界。
- [Path to Astra](https://openai.com/index/path-to-astra/)：支持公开与内部网络能力评测、访问配置及网络越狱拒绝率。
- [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra/vision)：支持思维链、行动及完整消息监控的实验结果和局限。

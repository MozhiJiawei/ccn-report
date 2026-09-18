# GPT-Live-1

## 一句话总结

截至2026-09-18官方文档，GPT-Live-1 是支持同时听说的实时话音模型，提供 Responses 和 client 两种后端委派模式，使语音交互在推理与工具任务执行期间继续进行，应用仍负责任务状态和权限。

## 任务信息

- 序号：123
- 任务编号：TASK-20260912023406-2037da87
- 热点编号：HS-20260912-insight-report-gpt-live-1
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/话音模型与模型架构
- 归类依据：category=null自动分类；主题贡献为全双工话音模型与交互机制，按04板块模态规则归话音；客服工作流是示例，不以应用产品化或评测方法为主要贡献。
- 任务正文：OpenAI GPT-Live-1 — 全双工 (full-duplex) 实时语音模型。2026/07 在 ChatGPT 内首发，2026/09/10 开放 API 调用（API + OpenAI Presence 企业平台双渠道）。基准性能：Tau3 语音智能体基准（航空/零售/电信客服任务）得分 86.2%，显著高于 GPT-Realtime-2.1 的 45.7% 与 GPT-Realtime-2 的 42.4%；Full Duplex Bench 相对 GPT-Realtime-2.1 提升 30%；改善轮替延迟与交互行为，可与 GPT-6 Astra 等后端模型协同处理语音对话与工具调用。意义：AI 对话从 turn-based 走向真流式实时双向。来源：The Register 2026-09-10。
- 任务来源：[原始任务来源](https://www.theregister.com/ai-and-ml/2026/09/10/openai-arms-devs-with-ai-conversation-tool-that-can-talk-and-listen-at-the-same-time/5295708)

## 交付件说明

- [GPT-Live-1.html](./GPT-Live-1.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [GPT-Live-1.pptx](./GPT-Live-1.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

基于官方文档核验机制与支持范围，未独立复测；任务媒体中的Tau3与Full Duplex Bench指标缺批准来源中的原始实验配置，未作为已证实效果。

## 引用信息源说明

- [GPT-Live 1 Model](https://developers.openai.com/api/docs/models/gpt-live-1)：模型定位、模态与计费边界
- [Getting started with GPT-Live](https://developers.openai.com/api/docs/guides/live)：全双工与语音/后端分工
- [Delegation and tools in GPT-Live](https://developers.openai.com/api/docs/guides/live-delegation)：两种委派模式、独立执行与应用权限责任

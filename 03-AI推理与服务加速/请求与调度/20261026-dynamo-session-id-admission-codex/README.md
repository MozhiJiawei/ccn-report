# Dynamo-SessionID准入

## 一句话总结

NVIDIA于2026年10月8日披露Dynamo以稳定session_id关联智能体多轮请求，并由单独启用的会话感知准入策略在工具边界暂停和恢复会话、减少KV驱逐重算，在SWE-bench单节点8×H100、两个TP4 MiniMax-M2副本的中高并发测试中较单独KV路由提高约12%–16%吞吐。

## 任务信息

- 序号：292
- 任务编号：TASK-20261026152242-05a80514
- 热点编号：HS-20261026-article1792999363041604
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/请求与调度
- 归类依据：API指定分类null，自动分类。已加载03与02板块细则；直接优化动作是按会话工作集控制准入、工具边界暂停恢复与worker placement，03/请求与调度的Cache亲和调度明确承接；KV缓存是协同机制，Agent身份是输入信号，不属于智能体运行时记忆或新模型。无指定分类差异。历史同主题云栖报告来源与实验不同，以SessionID准入消歧。
- 任务正文：NVIDIA Dynamo 引入会话级 session_id，智能体推理吞吐提升约 12%–16%技术线索
- 任务来源：[原始任务来源](https://aihot.news/items/v0etl74hps4tfznhm4lhp83if)

## 交付件说明

- [Dynamo-SessionID准入.html](./Dynamo-SessionID准入.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Dynamo-SessionID准入.pptx](./Dynamo-SessionID准入.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Session-Aware Agentic Inference with NVIDIA Dynamo](https://pytorch.org/blog/session-aware-agentic-inference-with-nvidia-dynamo/)：2026-10-08技术博客：稳定会话身份、工具边界准入、SWE-bench 12–16%吞吐的配置与基线、trace/replay、原Figure1与3，以及共享缓存和KvHint成熟度。
- [Session IDs（NVIDIA Dynamo dev）](https://docs.nvidia.com/dynamo/dev/agents/session-i-ds)：2026-10-26抓取：身份header映射与优先级，session_id passive metadata，不会单凭header启用路由策略。
- [ThunderAgent Program Scheduler（NVIDIA Dynamo dev）](https://docs.nvidia.com/dynamo/dev/agents/thunder-agent-program-scheduler)：Experimental原生插件的双角色YAML启用、frontend局部状态，以及native和Python prototype的预算与能力差异；不将dev配置混为博客评测版本。

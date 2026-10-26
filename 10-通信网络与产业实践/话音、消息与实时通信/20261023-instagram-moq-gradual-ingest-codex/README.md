# Instagram-MoQ渐进迁移

## 一句话总结

2026年10月12日，Meta公布将基于QUIC的媒体传输协议MoQ（具体部署草案版本未披露）用于Instagram iOS/Android直播推流入口，通过边缘MoQ到RUSH转换复用既有后端，并在放量采用的质量与可靠性指标上定性持平RUSH，具体指标值未公开。

## 任务信息

- 序号：274
- 任务编号：TASK-20261022153635-0bb04af5
- 热点编号：HS-20261022-article1792654596462102
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：10-通信网络与产业实践/话音、消息与实时通信
- 归类依据：任务category为null，自动归类。正式正文主问题是实时视频直播推流在生产环境的协议渐进迁移与可靠性验证，故归10-通信网络与产业实践/话音、消息与实时通信。11标准板块承接规范发布而非本业务部署，12通用系统板块不如本业务责任精确；调用方未指定，与约束无差异。
- 任务正文：Meta在Instagram Live推流上线Media over QUIC，实现与RUSH指标持平技术线索
- 任务来源：[原始任务来源](https://engineering.fb.com/2026/10/12/video-engineering/shipping-media-over-quic-at-meta-scale-for-instagram-live-ingest/)

## 交付件说明

- [Instagram-MoQ渐进迁移.html](./Instagram-MoQ渐进迁移.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Instagram-MoQ渐进迁移.pptx](./Instagram-MoQ渐进迁移.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Shipping Media Over QUIC at Meta Scale for Instagram Live Ingest](https://engineering.fb.com/2026/10/12/video-engineering/shipping-media-over-quic-at-meta-scale-for-instagram-live-ingest/)：支撑Instagram iOS/Android推流部署、Track/relay机制、边缘MoQ到RUSH迁移、会话级回退、定性parity及未来边界；原始概念图只支持协议设计目标。

# Boogu-Image-0.1 来源理解归档

## SMART 技术一句话

截至 2026-08-04，Boogu-Image-0.1 是面向图像生成与编辑研究者的 Apache-2.0 开放模型家族，公开 Base、Turbo、Edit、Edit-Turbo 4 个 10B 参数变体并支持最高 2K 分辨率；论文披露完整训练流程使用 208.62M 张去重图像、Base 模型 theoretical training cost 约 US$400K，其直接价值是展示“需求理解—提示改写—模型路由—生成/编辑”的开放研究路径，但成本数字不包含完整研发投入，结果仍需独立复现与场景化验证。

## 归档信息

- 任务编号：TASK-20260804181149-e7dceeb8
- 热点编号：HS-20260803-article111840
- 周期：2026-W32
- 原始任务来源：https://www.me.news/news/301312
- 一手论文来源：https://arxiv.org/abs/2607.13125
- 一手项目来源：https://github.com/boogu-project/Boogu-Image
- 归档日期：2026-08-04

## 正式交付件

- `source_understanding.html`：已导出为 dependency-free SingleFile HTML，可离线打开。

## 来源与证据边界

- 官方技术报告是 10B 参数、208.62M 张去重图像、训练方法、评估结果及约 US$400K 成本口径的主要证据。
- 约 US$400K 仅表示论文报告的 theoretical training cost，不包含数据获取与清洗、人员、失败实验、工程、评估或发布维护等完整研发成本。
- 官方 GitHub 用于核验模型家族、Apache-2.0 许可、部署配置、hotfix、研究项目声明和已知限制。
- ME News 只用于理解传播口径；Boogu Arena 为作者自建评测，不等同于独立第三方榜单。

## QA 状态

- `ppt-deep-search` 来源选择 gate：已由 CCN 快报 Loop 主 agent 批准。
- 独立视觉 QA：PASS；未发现破图、标题裁切、卡片遮挡或非预期横向滚动。
- Source Understanding 审批 gate：已批准并固化 baseline。

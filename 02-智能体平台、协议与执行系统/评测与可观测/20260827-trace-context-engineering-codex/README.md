# TRACE：从执行轨迹定位上下文故障

## 一句话总结

TRACE 将用户不满意信号转成可审计的上下文维修闭环：Detector 提取期望—实际差异，Root Cause Agent 沿执行轨迹反向归因，Recommender 主动读取原始上下文并生成带路径和证据的 CRUD 建议，再由人工审批回写；论文在 60 条合成、可验证故障轨迹上报告根因节点 Acc@1 为 72.7%、CRUD 操作准确率为 96%、端到端修复有效率为 82%，但该原型结果不能直接外推为生产全自动修复率。

## 任务信息

- 序号：34
- 任务编号：TASK-20260827174727-e61a3064
- 热点编号：HS-001
- 周期：2026-W32
- 任务正文：TRACE 自动化上下文工程，轨迹挖掘诊断智能体上下文故障技术线索
- 任务来源：[https://arxiv.org/abs/2608.09153](https://arxiv.org/abs/2608.09153)

## 交付件说明

- [source_understanding_review.html](./source_understanding_review.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，用于解释 DSAT 信号、轨迹反向归因、主动探索验证、CRUD 修复闭环及合成数据边界。
- [single_page_tech_report.pptx](./single_page_tech_report.pptx)：基于已验收 Source Understanding 结果制作的一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Trace: TRajectory Attribution for Automated Context Engineering](https://arxiv.org/abs/2608.09153)：用于支撑系统架构、轨迹归因方法、主动探索消融、修复指标和人工审批边界。

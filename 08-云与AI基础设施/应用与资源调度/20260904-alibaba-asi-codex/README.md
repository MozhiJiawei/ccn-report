# ASI-异构集群调度

## 一句话总结

阿里 ASI 异构集群调度是 OSDI 2026 论文基于 155,410 张 GPU、81 个内部部门的六个月生产轨迹总结的共享 AI 资源管理方案，通过 IPC 整理资源碎片、SpotGPU 可回收地借用预留容量，使论文报告的平均 GPU 分配率从仅高优先级作业的 68% 提升至加入低优先级作业后的 93%，为生产集群释放可分配容量提供实证依据。

## 任务信息

- 序号：55
- 任务编号：OSDI26-20260904-001
- 热点编号：OSDI26
- 周期：2026-09
- 任务正文：Heterogeneity at Hyperscale: Characterization and Scheduling of Large Production AI Clusters at Alibaba (Operational Systems)
- 任务来源：[USENIX OSDI 2026 官方论文页面](https://www.usenix.org/conference/osdi26/presentation/li-suyi)

## 交付件说明

- [ASI-异构集群调度.html](./ASI-异构集群调度.html)：dependency-free SingleFile Source Understanding HTML，可离线打开，包含机制解释、原始图表和证据边界。
- [ASI-异构集群调度.pptx](./ASI-异构集群调度.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX，文字和形状可编辑，论文原图以图片保留。

## 引用信息源说明

- [Heterogeneity at Hyperscale: Characterization and Scheduling of Large Production AI Clusters at Alibaba (Operational Systems)](https://www.usenix.org/system/files/osdi26-li-suyi.pdf)：支撑 ASI 生产轨迹规模、IPC 与 SpotGPU 机制、GPU 分配率和碎片整合结果，以及分配率不等于实际算力利用率的证据边界。
- [USENIX OSDI 2026 官方论文页面](https://www.usenix.org/conference/osdi26/presentation/li-suyi)：用于核对论文标题、作者、会议出处及正式全文入口。

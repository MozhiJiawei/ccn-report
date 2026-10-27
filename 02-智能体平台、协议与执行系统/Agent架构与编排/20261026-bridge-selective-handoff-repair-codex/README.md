# BRIDGE-选择性交接修复

## 一句话总结

BRIDGE是2026年10月13日arXiv v1提出的多智能体交接运行时控制框架，它从公开轨迹构建依赖图、用离线配对实验校准门控并在局部验证后提交修复，在DeepSeek-V4.1-flash的SILO-BENCH配置上将成功率从63.3%提高到75.6%，为可显式标识依赖的协作工作流减少交接故障。

## 任务信息

- 序号：283
- 任务编号：TASK-20261026145325-2ec075e5
- 热点编号：HS-20261026-article1792997605655736
- 周期：2026-W44
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/Agent架构与编排
- 归类依据：API指定null，AI自动分类。主要贡献是在线选择性修复多Agent交接、改变协作编排及运行时状态；HandoffProbe和MAST评估服务于校准与验证，并非主要评测交付物。已对照02与06分类规则，无指定值差异。
- 任务正文：BRIDGE以依赖图证据修复多智能体交接断点，SILO-BENCH成功率提升12.3个百分点技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.17805)

## 交付件说明

- [BRIDGE-选择性交接修复.html](./BRIDGE-选择性交接修复.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [BRIDGE-选择性交接修复.pptx](./BRIDGE-选择性交接修复.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [BRIDGE: Selective Boundary Repair with Dependency Graph Evidence in Multi-Agent Systems（arXiv v1）](https://arxiv.org/abs/2610.17805v1)：方法、门控与局部回滚边界、Table2四配置成功率、Appendix F/Table14双成本口径及其内部计费张力。

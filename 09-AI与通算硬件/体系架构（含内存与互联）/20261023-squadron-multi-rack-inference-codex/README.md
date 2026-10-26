# Squadron-多机架推理

## 一句话总结

d-Matrix于2026年10月12日发布Squadron多机架推理系统，通过Corsair XPU、JetStream标准以太网互联与Aviator软件集成风冷架构，配置上限为16个SquadRack和1024颗XPU，已在内部研发机房部署并向优先客户交付，公开AFD数据仅对应小规模GPU与Corsair异构实验，不能证明1024颗集群的全规模性能或成本能效收益。

## 任务信息

- 序号：268
- 任务编号：TASK-20261022153417-a345e2e1
- 热点编号：HS-20261022-article1792654458130182
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：09-AI与通算硬件/体系架构（含内存与互联）
- 归类依据：指定分类JSON原值为null，依据分类总则及09/08/03细则自动归入09-AI与通算硬件/体系架构（含内存与互联）。正式正文主对象是服务器、专用加速器、内存互联及软件协同组成的多机架硬件系统，非单芯片参数发布；08智算中心与云平台仅为机房兼容属性，未出现云平台资源管理机制；03推理部署中的AFD是局部应用佐证，未构成全文主贡献。无指定分类差异。
- 任务正文：d-Matrix推出Squadron多机架推理集群，单集群可扩至1024颗Corsair XPU技术线索
- 任务来源：[原始任务来源](https://www.unite.ai/d-matrix-unveils-squadron-multi-rack-ai-inference-clusters)

## 交付件说明

- [Squadron-多机架推理.html](./Squadron-多机架推理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Squadron-多机架推理.pptx](./Squadron-多机架推理.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [d-Matrix Announces Squadron Compute Clusters for AI Inference at Data Center Scale](https://www.d-matrix.ai/announcements/squadron-compute-clusters/)：核心来源：2026-10-12发布、16机架与1024 XPU配置上限、风冷、JetStream/Aviator、Arizona内部研发部署、优先客户交付和基础部件GA；供应商声明非独立验证。
- [Accelerating attention-FFN disaggregation with Corsair and Nvidia H100](https://www.d-matrix.ai/accelerating-ai-inference-with-attention-ffn-disaggregation/)：局部实验机制与条件：GPT-OSS-20B、SRAM专家、BS1为1H100+8Corsair，BS64为2H100共享8Corsair；845参数未知、20415/20413及BS1图文上下文不一致已就近保留，不作全规模外推。
- [d-Matrix Announces SquadRack](https://www.d-matrix.ai/announcements/squadrack/)：仅用于2025架构组成及PCIe节点内、JetStream/Ethernet节点间、Arista/Broadcom/Supermicro/Aviator责任关系，不把旧10x/3x营销指标移作2026 Squadron成绩。

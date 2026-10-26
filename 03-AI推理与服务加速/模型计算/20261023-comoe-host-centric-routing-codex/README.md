# CoMoE-主机共享路由

## 一句话总结

2026年10月19日修订的CoMoE v3以GPU直接访问主机共享缓冲的多播与逐token合并优化无P2P的专家并行通信，在8×RTX 5090、BF16、GPT-OSS-20B离线测试中，相比SGLang 0.5.9默认NCCL后端将输出吞吐由4,991.01提升至7,304.18 token/s（1.46倍），为PCIe单机MoE部署提供通信加速路径。

## 任务信息

- 序号：276
- 任务编号：TASK-20261022153834-8d71c282
- 热点编号：HS-20261022-article1792654714619885
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/模型计算
- 归类依据：指定分类为null，全文复核自动归入03-AI推理与服务加速/模型计算，直接贡献是MoE dispatch/combine通信优化，03模型计算明确包含通信优化；EP与8卡PCIe部署是前提而非主要部署切分创新，不归推理部署；不涉及租户资源池管理，不归08异构资源管理。无调用方强制分类，无判断差异。
- 任务正文：CoMoE以主机为中心路由让消费级GPU推理MoE吞吐提升最多1.46倍技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.09424)

## 交付件说明

- [CoMoE-主机共享路由.html](./CoMoE-主机共享路由.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [CoMoE-主机共享路由.pptx](./CoMoE-主机共享路由.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Democratizing MoE inference on commodity GPUs with CoMoE（arXiv v3，2026-10-19）](https://arxiv.org/abs/2610.09424v3)：支撑host-backed multicast、token级combine、8卡实验吞吐、主机与GPU开销、A800后端比较及吞吐归一GPU CapEx估算边界。

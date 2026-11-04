# CUDA13.4-GPU显存份额

## 一句话总结

NVIDIA 于2026年10月27日介绍的 CUDA 13.4 GPU 显存份额机制通过 GPU Fractioning Operator 在 Kubernetes 节点执行逐容器 request/limit 显存边界，并由 KAI Scheduler v0.18.0 的 NvFractions 集成两种计算共享模式与多GPU逐卡分配，使小于整卡的工作负载获得可执行的显存约束。

## 任务信息

- 序号：321
- 任务编号：TASK-20261103194513-7955e5e3
- 热点编号：HS-20261103-article1793706313632695
- 周期：2026-W45
- 指定分类：由 AI 自动分类
- 实际归档分类：08-云与AI基础设施/异构资源管理与抽象
- 归类依据：依据正式正文的主要技术对象判断；详见报告中的系统范围与机制说明。
- 任务正文：英伟达CUDA 13.4支持Kubernetes内存强制GPU共享，KAI调度器集成快报
- 任务来源：[原始任务来源](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/)

## 交付件说明

- [CUDA13.4-GPU显存份额.html](./CUDA13.4-GPU显存份额.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [CUDA13.4-GPU显存份额.pptx](./CUDA13.4-GPU显存份额.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/)：支撑2026-10-27发布日期、CUDA13.4显存强制边界、GPU Fractioning Operator职责、KAI v0.18.0 NvFractions集成、request/limit与逐卡多GPU示例、两种计算共享模式及错误域、同卡不能混用约束、原文Figure1；配置示例不是性能实测。。

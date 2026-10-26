# Runai-开放GPU编排

## 一句话总结

2026年10月13日，NVIDIA将Run:ai完整平台纳入DSX AI Factory开源体系，以KAI Scheduler、GPU Fractioning Operator、KAI Resource Management和Workload Map分别提供GPU调度、共享、组织配额与工作类型描述，并列出8家伙伴集成方案，为Kubernetes共享GPU基础设施提供整栈或按模块采用的资源治理路径。

## 任务信息

- 序号：264
- 任务编号：TASK-20261022153326-926caaa9
- 热点编号：HS-20261022-article1792654407379735
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/请求与调度
- 归类依据：按2026年10月26日人工审阅修订，围绕AI工作负载的排队、GPU调度与服务容量分配归入请求与调度。原AI分类为08-云与AI基础设施/应用与资源调度，侧重Kubernetes集群与租户配额治理；此处遵循人工归档选择，保留其平台级资源调度事实，不将其改写为已验证的模型内部请求调度算法。八伙伴为官方集成陈述而非生产效果；无整平台同条件收益实测，不采用相关Model Streamer加载数字代表平台性能。
- 任务正文：NVIDIA 将 Run:ai 平台整体开源，纳入 DSX AI Factory 并获八家生态伙伴集成技术线索
- 任务来源：[原始任务来源](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)

## 交付件说明

- [Runai-开放GPU编排.html](./Runai-开放GPU编排.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Runai-开放GPU编排.pptx](./Runai-开放GPU编排.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)：2026-10-13发布、完整平台与四模块、八伙伴集成、NGC Community Product及企业支持边界。
- [NVIDIA Run:ai 官方仓库固定提交](https://github.com/dsx-ai-factory/run-ai/tree/ec429eeff1c4dfecd6e33611c7645c8a8e043cce)：2026-10-23核验控制平面、集群服务、安装器与客户端源文件、原始架构图、根Apache-2.0及第三方许可和商标边界；未独立全栈构建或审计所有外部依赖。

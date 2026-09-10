# RedHat-AI3.5-生产治理

## 一句话总结

Red Hat AI 3.5是面向企业共享AI基础设施的平台版本，通过多租户隔离、优先级服务和原生观测等机制串联部署前验证、运行控制、Agent构建及运行度量四个环节，支持在混合云上运营AI服务，效果依据为2026年9月9日官方公布的功能与成熟度范围而非独立性能实测。

## 任务信息

- 序号：108
- 任务编号：TASK-20260910204906-61999699
- 热点编号：HS-20260910-article1789044546211223
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：08-云与AI基础设施/智算中心与云平台
- 归类依据：任务category为null，自动分类。正文主问题是把AI作为共享多租户服务在混合云平台运营，覆盖隔离、服务控制、开发链路和可观测，归08/智算中心与云平台。08/应用与资源调度只覆盖其中一个支撑机制；03/请求与调度不能承接跨租户及云平台治理；02/评测与可观测只覆盖Agent追踪子能力，因此不作为主归属。明确云平台主题适配二级，不一级直归。
- 任务正文：Red Hat AI 3.5发布：以多租户隔离、优先级调度和原生可观测性支撑AI Agent生产级规模化技术线索
- 任务来源：[原始任务来源](https://www.redhat.com/en/blog/red-hat-ai-35-scaling-and-governing-ai-agents-production)

## 交付件说明

- [RedHat-AI3.5-生产治理.html](./RedHat-AI3.5-生产治理.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [RedHat-AI3.5-生产治理.pptx](./RedHat-AI3.5-生产治理.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

唯一来源为官方发布Blog；未提供独立性能基准或成本节省数据。showback、视觉Agent追踪、AutoRAG及网关工具调用防护为技术预览，不能与GA能力混写。NVMe KV卸载未单独明确GA标记。

## 引用信息源说明

- [Red Hat AI 3.5: Scaling and governing AI agents in production](https://www.redhat.com/en/blog/red-hat-ai-35-scaling-and-governing-ai-agents-production)：版本发布日期、共享AI平台治理机制、GA与技术预览状态、证据边界

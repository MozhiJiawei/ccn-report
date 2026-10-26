# Meta-多尺度网络

## 一句话总结

Meta于2026年10月12日公布面向AI集群的多尺度以太网基础设施，其中102.4 Tbps IceCube提供128×800G总交换容量，FPF以每GPU八条100G链路接入独立平面并采用两层Clos，已交付Tahan以四台交换机互联16颗MTIA加速器，BAG及已部署SRv6骨干支撑跨站点资源连接。

## 任务信息

- 序号：263
- 任务编号：TASK-20261022153321-9c6bb77d
- 热点编号：HS-20261022-article1792654402380992
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：08-云与AI基础设施/智算中心与云平台
- 归类依据：指定分类原值null，依据正式全文自动分类。已读08/09/10/11细则：主体是AI训练集群从机架到集群再到跨站点的网络基础设施及统一运维，08智算中心与云平台明确承接AI网络平台；09硬件只覆盖交换平台子贡献，10通信运营网络不是主体，11开放规范是局部，故唯一主归属08。无指定分类差异。Meta定制平台采用Broadcom/NVIDIA伙伴ASIC，102.4T为总交换容量非端口速率；FPF未披露同条件量化时延、成本或训练收益；Tahan当前交付、72加速器预览、ESUN数据面未来规划分开；Prometheus和Muse仅背景。
- 任务正文：Meta在OCP披露下一代AI基础设施，自研多太比特交换机与统一Fabric支撑Muse智能体技术线索
- 任务来源：[原始任务来源](https://www.sdxcentral.com/news/meta-details-next-gen-ai-infra-custom-multi-terabit-switches-unified-fabrics/)

## 交付件说明

- [Meta-多尺度网络.html](./Meta-多尺度网络.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [Meta-多尺度网络.pptx](./Meta-多尺度网络.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Meta OCP Summit 2026官方工程博客](https://engineering.fb.com/2026/10/12/open-source/ocp-summit-2026-powering-ai-with-open-innovations-in-scale-up-scale-out-and-scale-across-networks/)：核心证据：三尺度网络、IceCube与IcePack、伙伴ASIC、FPF八平面与两层Clos、Tahan已交付、72加速器预览、未来ESUN、BAG与已部署SRv6、OSPA及MetaRoCE状态；设备与骨干原图来源。
- [Inside Prometheus官方工程博客](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)：用于说明跨设施AI训练和全栈可靠性的运行背景，未将系统goodput或可靠性改进归因于单交换机或FPF。
- [Introducing Muse官方产品发布](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)：仅作为个人AI Agent及专用VM的应用需求背景，不用于证明网络带来Agent效果提升。

# OpenShift Virtualization 与 Everpure Cloud

## 一句话总结

Red Hat 与 Everpure 于2026年9月23日介绍的 Azure Red Hat OpenShift 组合方案，通过 OpenShift Virtualization 在统一平台运行传统 VM 与容器，并以 Everpure Cloud、Portworx 提供存储和保护；官方宣称云存储成本最多可降低40%，但原文未提供独立基准方法。

## 任务信息

- 序号：173
- 任务编号：DSH-20260924-042
- 热点编号：HS-20260924-dsh-tech-insight
- 周期：2026-W39
- 指定分类：由 AI 自动分类
- 实际归档分类：08-云与AI基础设施/OS、虚拟化与隔离
- 归类依据：核心机制是 OpenShift Virtualization 将 VM 与容器纳入同一云平台管理，存储与保护是支撑组件。
- 任务正文：📌Red Hat OpenShift Virtualization 统一 VM 与容器跨混合云管理
原文标题：Unify VMs and containers with Everpure Cloud on Azure Red Hat OpenShift
元信息：战略 · 2026/09/23 · 编号 #42 · As organizations accelerate their cloud transforma
要点：
- 随着组织加速云转型，IT 团队常陷于双重困境——在孤岛中管理关键遗留虚拟机的同时并行推进应用现代化（要点原文截断）As organizations accelerate their cloud transformations, IT teams often find themselves trapped between 2 worldsmanaging mission-critical legacy virtual machines (VMs) in isolated silos while simultan
技术效果：效果 · 部署形态：部署形态：据 Hitachi Vantara 新闻稿，Red Hat OpenShift Virtualization 与 VSP One 整合方案采用 Global Active Device (GAD) 技术实现跨多站点 active-active 数据访问，并支持 Red Hat OpenShift master node 在公有云或隔离站点作为可选第三方仲裁；据 Hitachi Vantara 新闻稿引用的 ITPro 调研，73% 企业曾被审计、超三分之一将合规/管理过多许可列为首要痛点；据 Broadcom 文章引用的 CNCF 调研，77% Kubernetes 从业者反映集群管理与部署存在持续问题
背景补充：据 Hitachi Vantara 新闻稿，母公司日立（TSE: 6501）FY2024 营收 9,783.3 亿日元，方案已落地波兰 Alior Bank；据 Broadcom 文章，Principled Technologies 受 Broadcom 委托的基准测试显示 VMware Cloud Foundation 较 OpenShift 在裸金属上 pod 密度高 5.6×、pod 就绪快 4.9×
源链接：https://www.redhat.com/en/blog/unify-vms-and-containers-everpure-cloud-azure-red-hat-openshift
- 任务来源：[原任务来源](https://www.redhat.com/en/blog/unify-vms-and-containers-everpure-cloud-azure-red-hat-openshift)

## 交付件说明

- [OpenShift-Virtualization.html](./OpenShift-Virtualization.html)：可离线打开的 Source Understanding SingleFile HTML。
- [OpenShift-Virtualization.pptx](./OpenShift-Virtualization.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [Red Hat 官方博客](https://www.redhat.com/en/blog/unify-vms-and-containers-everpure-cloud-azure-red-hat-openshift)：用于核对组合方案与成本主张；40% 为厂商宣称的上限。
- [Everpure 官方博客](https://blog.everpuredata.com/products/everpure-cloud-and-azure-red-hat-open-shift/)：用于核对产品分工及方案背景。
- [Everpure 产品文档](https://support.everpuredata.com/r/everpure-cloud-dedicated-azure/psc-dedicated-with-aro-and-px-csi)：用于核对存储接入与架构边界。

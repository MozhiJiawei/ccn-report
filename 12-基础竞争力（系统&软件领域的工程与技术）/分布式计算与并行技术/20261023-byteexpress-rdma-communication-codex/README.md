# ByteExpress-RDMA通信层

## 一句话总结

2026年10月12日修订的v2论文介绍字节跳动ByteExpress在硬件RDMA上协同注册内存、QP复用、发送窗口与RPC恢复，使25Gbps参数服务器生产推理取参P99较已部署内核TCP下降43.7%、总CPU使用率相对下降10.69%，训练参数Push P99最高下降74.0%。

## 任务信息

- 序号：269
- 任务编号：TASK-20261022153424-ad88502a
- 热点编号：HS-20261022-article1792654465297532
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：12-基础竞争力（系统&软件领域的工程与技术）/分布式计算与并行技术
- 归类依据：category为null，依据全文自动判断。论文§4–7主要改变分布式参数服务器的注册内存、逻辑连接与QP复用、接收名额、在途字节控制及RPC恢复，§8同一通信层跨推理与训练，符合12二级分布式计算与并行技术的跨场景通用通信机制；03推理和05训练各只能覆盖应用之一，08云平台资源治理、09新硬件架构、10通信业务网络均非主要贡献。初判与全文最终分类一致，无调用方指定值差异。
- 任务正文：字节跳动ByteExpress以软件RDMA层降低推理训练通信时延与CPU占用技术线索
- 任务来源：[原始任务来源](https://arxiv.org/abs/2610.12815)

## 交付件说明

- [ByteExpress-RDMA通信层.html](./ByteExpress-RDMA通信层.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [ByteExpress-RDMA通信层.pptx](./ByteExpress-RDMA通信层.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [Deploying RDMA for Distributed Inference and Training at Scale（arXiv v2）](https://arxiv.org/abs/2610.12815v2)：唯一一手来源，支撑ByteExpress跨层通信机制、原图、25Gbps参数服务器生产实验、三基线结果、CPU降幅及故障恢复与指标边界。

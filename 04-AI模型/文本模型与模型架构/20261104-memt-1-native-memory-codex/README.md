# MemT-1.0

## 一句话总结

MemT-1.0 是在文本模型注意力旁加入可读写固定尺寸记忆状态的原生记忆模型，在作者 Nano 单并发实验的128K历史下，使每轨迹持久存储约为完整上下文KV的1/66、端到端推理加速1.86倍，但长历史细节回忆仍落后于强文本记忆系统。

## 任务信息

- 序号：327
- 任务编号：TASK-20261104090444-46c6ea68
- 热点编号：HS-20261104-article1793754285082853
- 周期：2026-W45
- 指定分类：由 AI 自动分类
- 实际归档分类：04-AI模型/文本模型与模型架构
- 归类依据：category原值为null，自动分类。全文主贡献为文本模型内的Native Memory Block、动态Local Memory与固定Hyper Memory及MoS扩容，改变模型计算结构；Agent编程为应用验证、两阶段训练为配套，故比02的外部记忆系统或05的训练方法更适配04。无调用方指定分类差异。
- 任务正文：记忆张量开源MemT 1.0，把记忆写入模型内部省下上下文快报
- 任务来源：[原始任务来源](http://mp.weixin.qq.com/s?__biz=MzAxOTcxNTIwNQ==&mid=2457996781&idx=1&sn=4f8409b50b089e6911941bd10dc24d36&chksm=8dfa5298aba20fe7706fd0ac2e4782c9021e663f138502fbd81518e378d8b58ba9d6712c319a&scene=0&xtrack=1#rd)

## 交付件说明

- [MemT-1.0.html](./MemT-1.0.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [MemT-1.0.pptx](./MemT-1.0.pptx)：一页式可编辑技术洞察 PPTX。

## 引用信息源说明

- [MemT-1.0: Towards Memory-Native Evolution](https://arxiv.org/abs/2610.26825v2)：原生记忆架构与状态更新、11基准Table2、128K效率/存储§6.5–6.6、经验编程Table5及限制；PDF为v2，65页。。
- [MemTensor/MemT-1.0 官方仓库](https://github.com/MemTensor/MemT-1.0/tree/7937b497e268e001b50c07ef8787a26e4901243a)：模型规格、架构原图、SGLang记忆客户端与快照流程；软件PolyForm NC、论文CC BY-NC-SA，权重不自动受上述许可覆盖。。

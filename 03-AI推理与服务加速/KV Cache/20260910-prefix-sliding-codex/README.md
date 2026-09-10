# PrefixSliding-前缀保留与滑窗

## 一句话总结

2026年8月26日arXiv v1论文提出Prefix Sliding，为Qwen3等推理模型保留指令前缀与最近窗口、驱逐中间历史KV状态并跳过对应注意力区块，在Qwen3-1.7B的4096窗口固定长度吞吐测试中于32K达到5479对1477 tok/s，为持续长思考提供缓存有界的执行方式。

## 任务信息

- 序号：80
- 任务编号：ISSUE36-20260910-004
- 热点编号：HS-20260910-prefix-sliding
- 周期：2026-W37
- 指定分类：由 AI 自动分类
- 实际归档分类：03-AI推理与服务加速/KV Cache
- 归类依据：直接变更对象为生成过程中历史KV的保留、驱逐及注意力可见范围，未减少累计生成的思维链token，归KV Cache而非输入输出数据。
- 任务正文：吴恩达团队提出Prefix Sliding方法，丢弃中间推理token实现3倍推理加速技术线索

线索来源：https://github.com/MozhiJiawei/Mozhi-s-AgentWorkspace/issues/36
Issue 所附来源：https://mp.weixin.qq.com/s?__biz=Mzk0MTYzMzMxMA==&mid=2247510745&idx=1&sn=413a4ff1480b263dfe33a6cc30f9d80f
论文主来源：https://arxiv.org/abs/2608.26070
来源核对备注：方法名、作者与加速主张匹配；微信报道触发验证，尚未核实报道内论文链接。3 倍加速限于论文评测条件。
- 任务来源：[原始任务来源](https://arxiv.org/abs/2608.26070)

## 交付件说明

- [PrefixSliding-前缀保留与滑窗.html](./PrefixSliding-前缀保留与滑窗.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [PrefixSliding-前缀保留与滑窗.pptx](./PrefixSliding-前缀保留与滑窗.pptx)：基于已验收 HTML 总结的一页式可编辑技术洞察 PPTX。

证据边界：Figure 1的3倍标注对应MATH500质量—平均思考时间曲线；Figure 6/Table 1的固定长度吞吐协议不同。4096窗口的三项任务准确率相对Full略降0.2–0.6个百分点；保留前缀与近窗不代表所有任务质量不变。Docling因共享主机内存不足未执行，采用GROBID与同版原始PDF/HTML图表，未宣称完整混合解析合同通过。

## 引用信息源说明

- [Prefix Sliding for efficient test-time scaling](https://arxiv.org/abs/2608.26070v1)：支持前缀与滑窗机制、位置编码、质量—时间与固定长度吞吐实验、窗口消融、训练扩展及适用限制。

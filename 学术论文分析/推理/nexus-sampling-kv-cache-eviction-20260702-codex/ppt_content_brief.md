# PPT Content Brief

## Deck Metadata
主题：面向长上下文 LLM 推理的 KV 缓存优化：Nexus Sampling 驱逐方法技术线索
目标读者：AI Infra / 推理系统研发团队
页数口径：1 页；单页输出，只生成 Summary Page；不包含 cover、contents 或内容页。
核心结论：Nexus 的差异在于把驱逐从“每步硬排名”改成“桥接评分 + 概率保留”，更适合固定预算、未来查询未知、误删会累积的流式推理。
内容来源：Nexus Sampling arXiv: 2606.23961；MorphKV arXiv: 2503.00979；PyramidKV arXiv: 2406.02069；来源选择记录见 `sources/source-selection.md`

## Summary Page
页码：Page 1
页面标题：Shrivastava课题组发布Nexus论文
标题说明：20% KV density 下，Nexus 在 SWE-bench 抽样 agent 任务中抗 true eviction，但证据仍需复现
分析总结：
- 机制：桥接重要性补足直接注意力，reservoir 替代每步 top-K 硬删
- 效果：SWE-bench 抽样 50 题中 Nexus true eviction 更稳，但 hardest setting 低于 MorphKV 1 题
正文内容：
【场景】这页面向 AI Infra / 推理系统研发团队，判断 Nexus Sampling 是否值得进入长上下文推理优化候选。当前讨论的不是 sparse attention 里“每步少读一些 token”，而是固定显存预算下的 KV-cache eviction：当长上下文、长生成或 agentic coding trace 让 cache 超过预算时，系统必须永久删除一部分历史 key/value。这个删除动作在 prefill-only 场景可能只发生一次，但在 prefill+decode 或多轮 agent 场景会连续发生；被删 token 后续不能恢复，因此一次局部误判会改变未来所有 attention 可见的信息集合。Shrivastava 课题组联合 Grinnell College、Rice University、Workato、Lambda 等作者提出的 Nexus Sampling，正是把这个问题从“局部打分排序”重新表达成“跨时间保留概率”的缓存生存问题。

【机制】Nexus Sampling 的机制由两段组成。第一段是 Nexus score：它不只看最近窗口对某个 token 的直接 attention，还引入 bridge importance，试图识别那些当前直接分数不高、但连接上下文簇或未来检索路径的桥接 token。第二段是 weighted reservoir selection：已有 H2O、SnapKV、PyramidKV、MorphKV 等驱逐方法大多可以理解为“某种 importance score + deterministic top-K”，而 Nexus 把选择原语换成按权重无放回抽样。这样做的关键含义是，top-K 阈值附近的 token 不会因为某一步低于 cutoff 就被判死；只要权重为正，它仍有非零 inclusion probability。对工程评审来说，创新点不只是“分数更复杂”，而是“选择规则也换了”：Nexus score 负责把桥接证据抬起来，reservoir 负责把边界证据从硬删除改成概率保活。

【效果】单页主效果改用 SWE-bench sampled / agentic coding，而不是 RULER。论文 Table 3 的口径是 20% KV density / 80% eviction，DeepSWE-Preview 基于 Qwen3-32B 在 R2E-Gym 中作为多轮 coding agent 运行，指标是 50 个 SWE-bench 抽样任务上的 Resolved/Pass@1。Prefill-only + Full context every turn 下，Dense 为 12/50，SnapKV 8/50，PyramidKV 7/50，AdaSnapKV 6/50，AdaPyramidKV 6/50，Nexus 9/50；切到 Prefill-only + True eviction 后，PyramidKV 和 AdaPyramidKV 从 7/50、6/50 坍缩到 1/50、1/50，而 Nexus 仍为 8/50，和 SnapKV、AdaSnapKV 同为最好。Prefill+Decode + Full context every turn 下，H2O 1/50，MorphKV 6/50，Nexus 7/50；最难的 Prefill+Decode + True eviction 下，H2O 4/50，MorphKV 9/50，Nexus 8/50。正确读法是：Nexus 在 true eviction 下更稳，尤其能暴露 PyramidKV 类方法从“可恢复压缩”到“永久删除”后的风险；但这不是完整 SWE-Bench，只是 50 个 sampled tasks，Dense 也只有 12/50，且 hardest setting 里 Nexus 比 MorphKV 少 1 个任务，所以它支持“值得复现”，不支持“已经证明生产收益”。

【对照】PyramidKV 和 MorphKV 是理解 Nexus 的两个好参照。PyramidKV 解决的是层间预算怎么分：低层保留更多 token，高层保留更少 token，用 pyramidal information funneling 压缩 prefill-only cache。MorphKV 解决的是长响应 decode 中 old token 怎么选：保留 recent window，再用最近 token 的 attention profile 选择相关远处 token。Nexus 的位置不同：它不只是给预算或定义 recent/distant cache，而是质疑各类分数之后的 deterministic top-K selection。换句话说，PyramidKV 更像“预算形状优化”，MorphKV 更像“相关旧 token 选择”，Nexus 更像“驱逐选择原语替换”。因此复现优先级应放在 SWE-bench sampled / agentic coding true eviction、RULER、LongBench MFQA 这类能放大连续误删风险的任务，而不是只看单次 prefill 压缩平均分。

【边界】这页支持“值得复现并纳入候选”，不支持“直接进入生产”。需要本地验证的边界包括：SWE-Bench 结果来自 50 个 sampled tasks，不是完整 SWE-Bench；Dense reference 只有 12/50，说明任务、模型或环境本身通过率低；hardest Prefill+Decode + True eviction 下 MorphKV 9/50 高于 Nexus 8/50，不能包装成全面领先；serving 是否允许 reservoir 带来的随机性；固定 seed、cache 状态记录和回放调试如何治理；20% density 的优势是否能迁移到本地目标密度。对团队的建议是先把 Nexus 做成可开关的 eviction policy，在相同 budget 下对照 PyramidKV / MorphKV / H2O / dense reference，先复现论文的 50-task 口径，再扩到更大 SWE-bench 子集和本地 agent 轨迹。
参考图片：
- ![Nexus 方法总览](assets/nexus-method.webp)
  图展示 Nexus scoring 与 weighted reservoir selection 的两段式流程，支撑“机制”判断。
- ![Nexus agentic coding 结果表](assets/nexus-table-3.webp)
  表展示 50 个 SWE-bench sampled tasks 上的 Resolved/Pass@1，支撑“true eviction 稳定性”和“hardest setting 落后 MorphKV”的双重判断；若原图过密，应重建为四象限矩阵。
- ![Nexus RULER 结果表](assets/nexus-ruler-table.webp)
  RULER 表只作为辅助证据，说明长上下文检索场景存在优势；单页主效果不要再围绕 RULER 展开。
备注：
- 作者背书：Anshumali Shrivastava 是莱斯大学计算机科学教授；论文作者单位包括 Grinnell College、Rice University、Workato、Lambda。讲述时不要把 “SWE-bench sampled” 说成完整 SWE-Bench；建议口播用语是“这是一组更贴近 agent 的小样本压力测试，能暴露 true eviction 风险，但还不足以支撑生产结论”。

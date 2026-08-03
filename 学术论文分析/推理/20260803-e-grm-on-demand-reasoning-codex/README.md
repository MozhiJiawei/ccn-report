# E-GRM：基于模型内部不确定性的按需推理

本目录归档 E-GRM ACL 2026 Findings 正式论文的 Source Understanding 报告，面向不了解生成式奖励模型的技术读者，解释其如何用并行解码共识度触发短/长推理路径，并用判别式评分器提高答案选择质量。

## 一句话描述

E-GRM 是腾讯混元、腾讯元宝与高校团队在 ACL 2026 Findings 发表的生成式奖励建模框架，它以 5 路并行解码、0.8 共识阈值按需触发 CoT，并在论文 MATH 设置下将准确率由 Forced-CoT 的 75.1% 提升至 78.4%、将平均延迟由 3.8 秒降至 2.2 秒，但论文宣称的“降低 62%”与表格可复算约 42.1% 不一致，仍待作者澄清口径。

## 正式交付件

- `source_understanding_review.html`：dependency-free SingleFile HTML，可离线打开，不依赖旁路图片、CSS、JavaScript 或字体文件。

## 唯一主证据

- 论文：**Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty**
- 正式版本：https://aclanthology.org/2026.findings-acl.1167.pdf
- 版本边界：Findings of ACL 2026，页码 23302–23319；报告结论以论文披露的模型、数据、阈值、硬件和实验设置为限。

## 核心证据边界

- 论文报告 MATH 上 58% 样本被路由到短路径；这不是任意任务或生产流量的固定比例。
- 表 4 给出 Forced-CoT `3.8s`、E-GRM `2.2s`，常规相对降幅约为 `42.1%`；论文正文写作 `62%`，两者存在无法从文内消解的口径矛盾。
- 表 6 给出 Base CoT-GRM `3.6s`、Full E-GRM `2.2s`，常规相对降幅约为 `38.9%`，同样不能直接推出 `62%`。
- 准确率提升不仅来自动态路由，也与混合损失判别式评分器及扩展 GRPO 训练有关，不能把全部增益归因于“少推理”。
- 并行解码仍引入论文所述低于单次生成延迟 5% 的额外开销；共识阈值和评分器泛化需要在新领域重新验证。

## 人工与质量状态

- Source Understanding：用户已确认归档。
- 论文解析：9/9 图表已索引，缺失与悬空引用为 0。
- SingleFile 导出：成功。
- 独立视觉 QA：PASS；无破图、裁切、遮挡、空 alt 或横向溢出。

归档日期：2026-08-03  
Creator：Codex


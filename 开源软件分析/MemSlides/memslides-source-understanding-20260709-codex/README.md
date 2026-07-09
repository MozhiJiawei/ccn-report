# MemSlides Source Understanding 归档

本目录归档 Issue #18「推理周报」主题「清华等高校联合开源 MemSlides」的 Source Understanding 审阅结果。

## 交付件

| 类型 | 文件 |
| --- | --- |
| Source Understanding 单文件 HTML | `source_understanding_review.html` |

## 来源范围

本轮聚焦两个来源：

- MemSlides 论文
  - URL: https://arxiv.org/abs/2606.17162
  - 角色：解释论文中的分层记忆、局部修订和校验目标。
- MemSlides 官方 GitHub 实现
  - URL: https://github.com/huohua325/Memslides
  - 本轮 checkout commit: `a308b8454633932aeef9bb8ad5a57751e5a5ef61`
  - 角色：把论文里较抽象的 PPT Agent 基座具象化为实际工程链路。

不纳入本轮证据链的内容：

- 项目官网
- 二手媒体报道
- SlideTailor、DeepPresenter 等同类方案

## 核心理解边界

MemSlides 可以理解为：先有一个能读材料、生成草稿、编辑 slide、检查结果并导出 PPTX/PDF 的 PPT Agent 基座，再在上面加记忆与校验，让多轮局部修改更稳定、更贴合用户偏好。

本轮没有实际跑端到端 `generate/revise` 实验；报告对实现基座的判断来自论文解析与官方仓库源码分析。具体生成质量仍需在真实环境中运行样例或 smoke suite 验证。

## QA 状态

- 论文 source package 解析通过。
- 官方 GitHub 实现分析完成。
- Source Understanding HTML 导出通过。
- 独立视觉 QA：PASS。
- 归档 HTML 已通过 `ccn-report/scripts/export_singlefile_archive.py` 导出为 SingleFile 单文件 HTML。

## 原始工作目录

本轮临时与可追溯产物位于：

```text
.tmp/ppt-deep-search/issue-18/memslides-v5/
```

前置论文解析和实现分析材料位于：

```text
.tmp/ppt-deep-search/issue-18/memslides-v2/
```

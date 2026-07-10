# Wayfinder Router Source Understanding 归档

本目录归档 Issue #18「推理周报」主题「Wayfinder Router 开源项目发布」的 Source Understanding 审阅结果。

## 交付件

| 类型 | 文件 |
| --- | --- |
| Source Understanding 单文件 HTML | `source_understanding_review.html` |

## 来源范围

本轮按用户确认只看两个官方来源：

- Wayfinder Router GitHub repository
  - URL: https://github.com/itsthelore/WayfinderRouter
  - 本轮 checkout commit: `f5266720d10bae00d3d7748b2bd637259b16f670`
- wayfinder-router PyPI package page
  - URL: https://pypi.org/project/wayfinder-router/
  - 页面版本信号：`2026.7.0`

不纳入本轮证据链的内容：

- Hacker News 发布讨论
- RouteLLM、Not Diamond 等同类方案
- 非官方二手文章或聚合信息

## 核心理解边界

Wayfinder Router 的核心不是语义理解模型，而是一个离线、确定性、无额外模型调用的 prompt-complexity gate。它通过 prompt 的长度、标题、列表、代码块、表格、链接和可选词汇信号计算复杂度分数，再把请求路由到本地/便宜模型或云端/强模型。

报告中特别补充了实现层和 benchmark 边界：

- decision path 与 delivery path 分离：前者是纯函数评分，后者才处理网关转发、key、缓存、限流、预算、虚拟 key 和可靠性。
- 默认 structural router 不是高精度语义 router；官方 RouterBench 结果显示 structural default 的 held-out / real-label skill 约为负值。
- lexical opt-in 在 math / reasoning / STEM-heavy 数据上有条件正向结果，但不等于通用语义难度判断能力。
- 更稳妥的产品定位是低成本第一层 `gating filter`，生产采用前应先测自有流量。

## QA 状态

- GitHub 仓库已 checkout 并完成实现与 benchmark 边界分析。
- PyPI source package 抓取和校验通过。
- Source Understanding HTML 导出通过。
- 独立视觉 QA：PASS。
- 归档 HTML 已通过 `ccn-report/scripts/export_singlefile_archive.py` 导出为 SingleFile 单文件 HTML。

## 原始工作目录

本轮临时与可追溯产物位于：

```text
.tmp/ppt-deep-search/issue-18/wayfinder-router/
```

其中包括 source package、GitHub checkout、实现分析、benchmark 边界分析、导出截图和视觉 QA。

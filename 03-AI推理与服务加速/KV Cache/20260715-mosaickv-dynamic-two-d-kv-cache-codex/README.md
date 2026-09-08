# MosaicKV 动态二维 KV Cache 压缩归档

本目录归档上海交通大学 IPADS 团队论文 `MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression` 的两份正式交付件。

## 归档信息

- 归档日期：2026-07-15
- 分类：学术论文分析 / 推理
- 原始论文：https://arxiv.org/abs/2607.00760
- 归档路径：`学术论文分析/推理/20260715-mosaickv-dynamic-two-d-kv-cache-codex/`

## 正式交付件

- `source_understanding_review.html`：面向技术读者的长文 Source Understanding 报告，解释 KV Cache 显存墙、动态二维压缩、PackedAttention、CPU/GPU 异构双缓冲、实验结果与证据边界。
- `mosaickv-management-onepager.html`：面向管理层的单页 16:9 HTML PPT，高密度呈现问题、技术价值、方案实现概要、论文证据、PoC 建议与 Go / No-Go 条件。

两份 HTML 均已通过 `ccn-report/scripts/export_singlefile_archive.py` 导出为 dependency-free SingleFile，可离线打开，不依赖旁路图片、CSS、JavaScript 或字体文件。

## 关键证据口径

论文在 H800 80GB、多模型实验中报告：最高 `7.3×` throughput、最高 `4.8×` 更低 decode latency、最高 `16×` attention speedup、`3×` memory reduction，以及 LongBench / RULER 平均 `1.76%` accuracy loss。这些数字属于论文实验结果和 `up to` 口径，不代表生产 SLA，也不保证在同一工作负载中同时达到。

## 归档边界

本目录只保存正式 SingleFile HTML 和必要说明，不归档论文 PDF、解析 XML、图片包、PNG 预览、Humanize 运行记录、视觉 QA 文件、导出 manifest 或其他临时日志。上述过程材料保留在工作区 `.tmp/` 中。

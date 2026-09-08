# Intel Xeon 6 + NVIDIA HGX B200 异构推理架构研究归档

本目录归档《Intel 推出 CPU+GPU 异构推理架构：Xeon 6 配合 NVIDIA HGX B200 提升并发用户数》研究过程和正式交付件。

## 交付件

| 类型 | 文件 |
| --- | --- |
| 4 页 HTML 成稿 | `html/source_understanding_4page.html` |
| 15 页详细理解稿 | `html/source_understanding_detailed_15page.html` |
| 可编辑 PowerPoint | `pptx/intel-xeon6-hgx-b200-brief-editable.pptx` |
| 4 页 HTML 预览 | `previews/html-4page/` |
| 可编辑 PPTX 预览 | `previews/pptx-editable/` |
| HTML 视觉 QA | `qa/html-4page-visual-qa.md`, `qa/html-detailed-15page-visual-qa.md` |
| PPTX 校验记录 | `qa/pptx-editable-validation.txt` |
| 信源与事实边界 | `sources/` |

## 研究范围

本轮只保留两个原始信源，不做同类方案横向调研：

- Intel 官方博客：`Intel Xeon 6 Processors and Intel AMX Deliver More Concurrent Users with NVIDIA HGX B200 Systems`
- Supermicro 白皮书：`Supermicro X14 HGX B200 GPU Servers With Intel Xeon 6 Processors`

补充核验用于解释硬件量级和边界：

- Intel Xeon 6776P 官方规格与 Intel Xeon 6 AMX product brief
- NVIDIA GB200 NVL72 / DGX B200 / DGX GB200 官方规格
- Intel AI TCE vLLM `cpu_binding` / `cpu_binding_demo` 分支中的 benchmark 脚本口径

## 核心结论

Intel 这条技术线索的价值不是“CPU 替代 B200/GB200 GPU”，而是在 HGX B200 系统内复用已经供电、已经部署的 host CPU 余量，把 Xeon 6 + AMX 作为 CPU 8B endpoint 承接轻量推理、校验、路由和短任务，从而让 GPU 405B endpoint 专注长文本生成和复杂推理。

公开材料给出的并发效果是：

- GPU-only baseline：127 concurrent users
- CPU 8B endpoint 增量：+56 concurrent users
- CPU-GPU co-serving total：183 concurrent users
- 相对提升：up to 1.44x

## 证据红线

- CPU 8B endpoint 的最终 TTFT / TPOT 实测值未在公开材料中披露。`10000ms TTFT / 100ms TPOT` 是 Intel demo 脚本中的 SLA 默认阈值，不是实测延迟。
- 双路 Xeon 6776P 的 AMX BF16/FP16 `302-472 TFLOPS` 和 INT8 `603-944 TOPS` 是理论峰值区间，不是 vLLM 8B endpoint 的持续吞吐。
- GB200 Superchip 的 BF16 dense / sparse Tensor Core 量级显著高于双路 Xeon AMX；本报告只把 Xeon AMX 定位为小模型服务层，不把它表述为 B200/GB200 Tensor Core compute 的替代品。
- 功耗口径不能硬比：`700W` 是双路 Xeon CPU package-level TDP；`14.3kW` 是 DGX B200 system-level power；`120kW` 是 GB200/NVL72 rack-level power。

## 处理过程

1. 使用 `web-article-capture` 抓取 Intel 官方博客正文和正文图片，输出 `sources/web/intel-xeon6-amx-hgx-b200-blog/`。
2. 使用 `grobid_pdf_skill` 解析 Supermicro 白皮书，输出结构化 XML、PDF 和图表资产。
3. 生成 15 页 Source Understanding HTML，并根据审核反馈补充 TTFT/TPOT、AMX/AVX-512/GB200 算力、功耗/能效边界。
4. 基于 15 页详细稿裁剪成 4 页高密度版：结论、硬件参数、case 场景、效果。
5. 使用 Codex 原生 Presentations skill 将 4 页 HTML 转成可编辑 PPTX，重建为原生 PowerPoint 对象，而不是整页截图。

## QA 状态

- 15 页详细理解稿：独立视觉 QA `PASS`。
- 4 页 HTML 成稿：独立视觉 QA `PASS`，四项主视觉检查均通过。
- 可编辑 PPTX：`render_slides.py` 成功渲染 4 页 PNG；`slides_test.py` 返回 `Test passed. No overflow detected.`；视觉复查未发现非预期 overlap、clip 或 wrap。


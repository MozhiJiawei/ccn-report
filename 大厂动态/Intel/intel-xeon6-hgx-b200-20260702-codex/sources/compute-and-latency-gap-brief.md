# Compute and Latency Gap Brief

Purpose: supplemental facts for revising the Source Understanding deck. Keep evidence boundaries explicit.

## User-flagged gaps

- CPU 8B endpoint can run, but the prior deck did not answer: what is its TTFT / TPOT service quality?
- AMX was described qualitatively as matrix acceleration, but the deck did not quantify matrix compute, vector compute, or compare the magnitude with NVIDIA GB200.

## CPU 8B TTFT / TPOT evidence status

Current public materials do not disclose measured TTFT / TPOT for the CPU 8B endpoint.

Evidence:

- Supermicro white paper says the benchmark flow generates `benchmark_results.md` and `benchmark_results.json`, which are used to compare concurrency, TTFT, and TPOT criteria.
- The same white paper reports only the concurrency outcome in the visible text: GPU-only B200 workload supported 127 concurrent users; adding the CPU 8B endpoint added 56 CPU users; total became 183, or up to 1.44x versus GPU-only.
- The cloned Intel AI TCE `cpu_binding` branch does not include committed `benchmark_results.md/json` values.
- The cloned Intel AI TCE `cpu_binding_demo` branch includes benchmark result extraction logic and default SLA thresholds, but not published measured results:
  - `SLA_TTFT_MS="${SLA_TTFT_MS:-10000}"`
  - `SLA_TPOT_MS="${SLA_TPOT_MS:-100}"`
  - the script extracts p99/mean TTFT and TPOT from result JSON files and then converts `benchmark_results.json` to markdown.

Conclusion to show in revised Source Understanding:

- Do not invent TTFT / TPOT. Say the evidence supports "max concurrent users under benchmark SLA search", not "CPU 8B latency quality is proven to be X ms".
- The default demo thresholds, 10,000 ms TTFT and 100 ms TPOT, are benchmark gates / defaults, not measured CPU 8B results.
- The stronger technical question for the audience is: the 56 added CPU users are meaningful only if their TTFT / TPOT stay inside the service-level threshold. The public article/white paper do not expose those final numbers.

Evidence archive notes:

- Intel AI TCE `cpu_binding_demo` benchmark script was inspected from the public `intel-ai-tce/vllm` GitHub branch during research; the cloned repository cache is not archived here.
- Parsed Supermicro white paper XML is archived at `sources/papers/supermicro-x14-hgx-b200-xeon6-whitepaper/final/supermicro-whitepaper.xml`.

## Xeon 6776P compute facts, re-verified

Official Intel product/spec sources:

- Intel Xeon 6776P processor specs: 64 cores, 128 threads, 3.9 GHz max turbo, 3.6 GHz all-core turbo, 2.3 GHz base, 350 W TDP.
  - URL: https://www.intel.com/content/www/us/en/products/sku/243691/intel-xeon-6776p-processor-336m-cache-2-30-ghz/specifications.html
- Intel Xeon 6 product brief: AMX provides up to 2,048 INT8 operations/cycle/core and 1,024 BF16/FP16 operations/cycle/core.
  - URL: https://www.intel.com/content/www/us/en/products/docs/xeon-6-product-brief.html
- Intel Xeon 6 product brief, official PDF: same AMX statement and also says AMX provides up to 16x more MAC operations than AVX-512 for BF16/FP16-based models.
  - URL: https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2024-05/intel-xeon-6-product-brief.pdf
- Intel AVX-512 explainer: AVX-512 provides up to two 512-bit FMA units; Intel Xeon 6 product brief says AMX provides up to 16x more MAC operations than AVX-512 for BF16/FP16.
  - URL: https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/what-is-intel-avx-512.html

Derived dual-socket peak estimates for the tested 2 x Xeon 6776P system:

- Cores: 2 sockets x 64 cores = 128 P-cores.
- Conservative AMX BF16/FP16 matrix peak at base clock: 1,024 ops/cycle/core x 128 cores x 2.3 GHz = about 302 TFLOPS.
- Upper-bound AMX BF16/FP16 matrix peak at Intel-listed all-core turbo: 1,024 x 128 x 3.6 GHz = about 472 TFLOPS.
- Conservative AMX INT8 matrix peak at base clock: 2,048 ops/cycle/core x 128 cores x 2.3 GHz = about 603 TOPS.
- Upper-bound AMX INT8 matrix peak at Intel-listed all-core turbo: 2,048 x 128 x 3.6 GHz = about 944 TOPS.
- AVX-512 BF16/FP16 vector compute should be framed only as an AMX/16 derived estimate under Intel's official "AMX up to 16x more MAC than AVX-512" statement: about 18.8 TFLOPS at base clock to about 29.5 TFLOPS at all-core turbo. Treat this as a derived estimate, not a published product-line item.

Recommended deck wording:

- "Intel 官方给出 AMX 每核每周期 1,024 BF16/FP16 ops；按双路 6776P、128 核计算，理论峰值约 302 TFLOPS（base）到 472 TFLOPS（all-core turbo 上界）。"
- "这个数只说明 AMX 矩阵硬件量级，不等于 vLLM 8B endpoint 的持续吞吐、TTFT 或 TPOT。"

Do not present these as sustained vLLM throughput. They are architectural/theoretical peak estimates used to explain scale. The all-core turbo calculation is an upper-bound estimate because actual AMX-heavy sustained frequency depends on power, thermals, BIOS, workload mix, and platform policy.

## NVIDIA GB200 facts for comparison

Official NVIDIA source:

- NVIDIA GB200 NVL72 specs page.
  - URL: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA DGX GB200 / rack-scale system user guide, power section: rack power consumption is approximately 120 kW.
  - URL: https://docs.nvidia.com/dgx/dgxgb200-user-guide/hardware.html
- NVIDIA DGX B200 product page: 8 x B200 system power usage is about 14.3 kW max.
  - URL: https://www.nvidia.com/en-us/data-center/dgx-b200/

GB200 Grace Blackwell Superchip official specs:

- Configuration: 1 Grace CPU + 2 Blackwell GPUs.
- NVFP4 Tensor Core: 40 PFLOPS sparse / 20 PFLOPS dense.
- FP8/FP6 Tensor Core: 20 PFLOPS sparse; dense is half per NVIDIA footnote.
- INT8 Tensor Core: 20 POPS sparse; dense is half per NVIDIA footnote.
- FP16/BF16 Tensor Core: 10 PFLOPS sparse; dense is half per NVIDIA footnote, so 5 PFLOPS dense.
- TF32 Tensor Core: 5 PFLOPS sparse; dense is half per NVIDIA footnote.
- FP32: 160 TFLOPS.
- FP64 / FP64 Tensor Core: 80 TFLOPS.
- GPU memory and bandwidth: 372 GB HBM3E, 16 TB/s.
- NVLink bandwidth: 3.6 TB/s.
- CPU: 72 Arm Neoverse V2 cores; CPU memory up to 480 GB LPDDR5X, up to 512 GB/s.

GB200 NVL72 official specs:

- Configuration: 36 Grace CPUs + 72 Blackwell GPUs.
- NVFP4 Tensor Core: 1,440 PFLOPS sparse / 720 PFLOPS dense.
- FP16/BF16 Tensor Core: 360 PFLOPS sparse / 180 PFLOPS dense.
- FP32: 5,760 TFLOPS.
- GPU memory and bandwidth: 13.4 TB HBM3E, 576 TB/s.
- NVLink bandwidth: 130 TB/s.
- CPU cores: 2,592 Arm Neoverse V2 cores; CPU memory 17 TB LPDDR5X, 14 TB/s.

Comparison guidance:

- Fairer dense BF16 comparison:
  - 2 x Xeon 6776P AMX BF16 theoretical peak: about 0.302 PFLOPS at base clock to about 0.472 PFLOPS at all-core turbo upper-bound.
  - 1 x GB200 Grace Blackwell Superchip BF16 dense Tensor Core peak: about 5 PFLOPS.
  - GB200 superchip is roughly 10.6x to 16.6x the dual-Xeon AMX dense BF16 theoretical peak, depending on whether the Xeon side uses all-core turbo upper-bound or base clock.
  - Using GB200 sparse BF16 spec, the ratio is roughly 21.2x to 33.1x.
- This confirms the positioning: Xeon AMX is not a replacement for GB200/B200-class GPU tensor compute. Its role is to monetize otherwise idle host CPU capacity for smaller 8B / validation / routing / short-context work.
- The deck should avoid making the CPU look like a GPU peer on large-model generation. It is a second inference tier with much smaller peak compute but enough local capacity for CPU-suitable tasks.

## Power and efficiency framing

Official power anchors:

- Intel Xeon 6776P TDP: 350 W per socket. The tested dual-socket CPU side is therefore 700 W CPU TDP.
- NVIDIA DGX B200 system power usage: about 14.3 kW max for an 8 x B200 system, including system-level components.
- NVIDIA DGX GB200 / GB200 NVL72 rack power: approximately 120 kW per rack. HPE's NVL72 QuickSpecs list 132 kW nominal rack TDP and about 192 kW peak electrical design power, so vendor/OEM rack planning can be higher than NVIDIA's approximate rack consumption number.

Derived power-normalized theoretical compute, for orientation only:

- Dual Xeon 6776P AMX BF16/FP16 theoretical peak per CPU TDP:
  - Base clock: 302 TFLOPS / 0.7 kW = about 431 TFLOPS/kW.
  - All-core turbo upper bound: 472 TFLOPS / 0.7 kW = about 674 TFLOPS/kW.
- GB200 NVL72 rack BF16/FP16 dense theoretical peak per rack power:
  - 180 PFLOPS dense / 120 kW = about 1,500 TFLOPS/kW at rack level.
  - 360 PFLOPS sparse / 120 kW = about 3,000 TFLOPS/kW at rack level.

Presentation guidance:

- Do not compare 700 W CPU TDP directly against 120 kW rack power as if they are the same boundary. CPU TDP is a package-level thermal design number; NVL72 power is a rack-level system number with GPUs, Grace CPUs, NVLink/NVSwitch, power delivery, and cooling design.
- For this Intel + HGX B200 story, the practical value claim is not "Xeon AMX has better absolute performance per watt than GB200." The defensible claim is "the host CPU TDP is already provisioned in the GPU server, and AMX can turn part of that existing power envelope into useful small-model serving capacity instead of leaving it idle."
- If the deck needs one sentence: "功耗口径上，双路 6776P 是 700W CPU TDP，而 B200/GB200 是十几千瓦到百千瓦级系统；异构推理的收益来自复用已在机内的 CPU 电力和核心余量，不是用 CPU 去替代 GPU 的能效曲线。"

# Intel® Xeon® 6 Processors and Intel® AMX Deliver More Concurrent Users with NVIDIA HGX B200 Systems

Source URL: https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Intel-Xeon-6-Processors-and-Intel-AMX-Deliver-More-Concurrent/post/1752394
Source slug: intel-xeon6-amx-hgx-b200-blog
Publisher: Intel Community / Tech Innovation / Artificial Intelligence (AI) blog
Author: Louie Tsai, AI Software Solutions Engineer, Intel
Posted date: 06-25-2026
Captured date: 2026-07-02
Capture mode: rendered capture via Codex in-app Browser

![Article hero image](images/image-01.webp)

Original image URL: https://community.intel.com/t5/image/serverpage/image-id/73188i8BD13E6C8563983B/image-size/large?v=v2&px=999&whitelist-exif-data=Orientation%2CResolution%2COriginalDefaultFinalSize%2CCopyright

Caption / nearby text: Intel® Xeon® 6 Processors and Intel® AMX Deliver More Concurrent Users with NVIDIA HGX B200 Systems. Displayed between the article title and the author/date metadata.

## Article Text

**Author:** *Louie Tsai, AI Software Solutions Engineer, Intel*

Modern large language model (LLM) serving systems often allocate most inference workloads to GPUs while leaving CPU resources underutilized, thereby limiting scalability and user concurrency. This blog introduces a heterogeneous architecture that co-runs vLLMs on both CPUs and GPUs to improve overall system efficiency through multi-agent or vLLM semantic routing across two inference endpoints: a CPU pathway and a GPU pathway The architecture consists of three coordinated agents:

- A CPU-based **Researcher agent** responsible for preparing and organizing contextual information.
- A GPU-based **Writer agent** dedicated to high-quality response generation.
- A CPU-based **Reviewer agent** that edits, validates, and gives rapid feedback on Writer-agent responses.

This architecture enables efficient workload distribution across heterogeneous compute resources. Its closed-loop design ensures that both CPU and GPU resources on the same AI-accelerated system are continuously engaged, reducing idle time and improving throughput. Multi-agent is one use case, and vLLM semantic routing as another use case dynamically directs requests between the two endpoints based on task complexity and inference requirements, ensuring optimal utilization of both CPU and GPU resources. This closed-loop heterogeneous design keeps all compute resources continuously engaged, reducing idle time while improving throughput, scalability, and overall serving efficiency.

This implementation extends vLLMs with a heterogeneous architecture that splits inference across two coordinated endpoints:

- A **CPU pathway** running a Llama-3.1-8B model for lightweight reasoning tasks, such as research extraction, summarization, critique, and response validation.
- A **GPU pathway** running a Llama-3.1-405B model for compute-intensive generation, including long-form structured outputs, deep reasoning, and multi-step synthesis.

### Performance

Performance results demonstrate the advantages of Intel Xeon 6 processors (P-cores) with Intel® Advanced Matrix Extensions (Intel® AMX) in a heterogeneous setup that uses both CPU and GPU compute on the same AI-accelerated system. The system runs CPU and GPU models in parallel, with the Intel Xeon 6 processor executing the Llama-3.1-8B model with 128 input/128 output tokens for lightweight reasoning, orchestration, and intermediate validation. In comparison, the NVIDIA B200 GPU runs a Llama-3.1-405B model with 2,048 input/2,048 output tokens for large-scale generation and complex synthesis. This parallel execution enables efficient workload distribution across the pipeline and improves utilization of both compute domains. With Intel AMX acceleration on Intel Xeon 6 processors, the system achieves up to 1.44x higher user concurrency by running the workload on both the CPU and the GPU simultaneously, demonstrating improved throughput and serving efficiency. The evaluation is conducted on a Supermicro SYS-822GS-NBRT HGX platform equipped with 2 x Intel Xeon 6776P processors (with Intel AMX enabled) and 8 x NVIDIA HGX B200 GPUs, highlighting the effectiveness of CPU–GPU co-serving for scalable vLLM inference.

In a multi-agent use case, the Researcher agent initiates execution first, the Writer agent begins as soon as partial context or notes become available, and the Reviewer agent starts once a partial draft is produced. This overlapping, staged execution enables pipelined processing across agents, reducing overall end-to-end latency compared to strictly sequential execution.

Without pipelining, the execution is strictly sequential, so end-to-end latency accumulates across stages:

**Total latency = Research time + Write time + Review time**

With the multi-agent pipelined design, CPU and GPU stages run concurrently, with overlapping execution:

**Total latency = Maximum of Research time, Write time, and Review time**


![Picture1.png](images/image-02.webp)

Original image URL: https://community.intel.com/t5/image/serverpage/image-id/73186i0E9C5ECF76B7FFFE/image-size/large?v=v2&px=999&whitelist-exif-data=Orientation%2CResolution%2COriginalDefaultFinalSize%2CCopyright

Caption / nearby text: Picture1.png. Appears after the latency formulas comparing sequential and pipelined multi-agent execution.

This enables a pipelined execution model in which CPU agents continuously prepare, retrieve, and validate context, while GPU agents focus on generation. This approach allows overlapping execution across stages rather than sequential processing. Consequently, end-to-end latency shifts from an additive pipeline to a parallelized bound, improving hardware utilization, reducing GPU idle time, stabilizing tail latency, and increasing overall concurrency in production-scale vLLM deployments.

![Picture2.png](images/image-03.webp)

Original image URL: https://community.intel.com/t5/image/serverpage/image-id/73187i94A7E8B265D380CB/image-size/large?v=v2&px=999&whitelist-exif-data=Orientation%2CResolution%2COriginalDefaultFinalSize%2CCopyright

Caption / nearby text: Picture2.png. Appears before the Learn More section, following the paragraph about pipelined execution and concurrency improvements.

### Learn More

Contact your Intel representative to discuss the value of Intel Xeon 6 processors with PCT for advanced AI workloads. And learn more about Intel Xeon 6 processors SKUs with PCT on Intel’s website:

Intel Xeon 6776P processor

Intel AMX Enhances vLLM Inference - Technical Brief

**Endnotes**

(1) Results may vary based on system configuration, workload characteristics, hardware environment, service-level objectives (SLOs), and other operational factors. Performance improvements are dependent on proper setup and optimization. **Configuration:** 1-node, Supermicro X14DBG-LC+, 2 x Intel Xeon 6776P processor, 64 cores, 350 W TDP, Intel® Hyper-Threading Technology (Intel® HT Technology) on, Intel® Turbo Boost Technology on, 2,048 GB total memory (32 x 64 GB DDR5 6,400 MT/s [5,200 MT/s]), BIOS 1.5, microcode 0x1000405, 3 x unknown network interface controller (NIC), 2 x Intel® Ethernet Controller X710 for 10GBASE-T, 1 x 7 TB Samsung MZTL67T6HBLC-00AW7, 1 x 3.5 TB Samsung MZTL23T8HCLS-00A07, Ubuntu 22.04.5 LTS, 6.8.0-90-generic. NVIDIA HGX B200 8-GPU with 5th Generation NVLink® 1.8TB/s, 2.3TB of HBM3e GPU memory per system. Tested by Intel as of March 21, 2026.

**Notices and Disclaimers**

Performance varies by use, configuration, and other factors. Learn more on the Performance Index site. Performance results are based on testing as of the dates shown in configurations and may not reflect all publicly available ​updates. See backup for configuration details. No product or component can be absolutely secure. Your costs and results may vary. Intel technologies may require enabled hardware, software, or service activation. © Intel Corporation. Intel, the Intel logo, and other Intel marks are trademarks of Intel Corporation or its subsidiaries. Other names and brands may be claimed as the property of others.

## Capture Notes

- Body boundary: extracted from the rendered Intel Community blog article body (`#bodyDisplay .lia-message-body-content`), with the separate article cover image included because it is in the article reading flow between title and metadata.
- Tail boundary: retained Learn More, Endnotes, and Intel Notices and Disclaimers because they are part of the article body; stopped before footer/site chrome and excluded community navigation, reactions, comments, and profile/sidebar elements.
- Media kept: article cover image, Picture1.png, and Picture2.png. Media rejected: Intel header logo, Intel footer logo, and author avatar as site chrome/profile UI rather than article正文 figures.
- Image handling: downloaded original rendered image URLs observed in the page DOM; no screenshots were used as source images.

# Dynamo Inference Framework | NVIDIA Developer

Source: https://developer.nvidia.com/dynamo
Captured: 2026-06-25

## Source Notes

- Publisher: NVIDIA Developer
- Date: Not shown on the captured page
- Selected content: Rendered main page content for NVIDIA Dynamo, including product positioning, "How NVIDIA Dynamo Works", getting-started resources, starter kits, and related resource sections.
- Capture notes: The page is a product/developer landing page with marketing and resource-summary content rather than a deep technical reference. For later technical detail, especially component architecture and deployment behavior, use the linked NVIDIA Dynamo documentation introduction (`https://docs.nvidia.com/dynamo/latest/`) as a follow-up source. This capture only processes the requested URL.
- Image notes: The source page includes many video thumbnails in the "See NVIDIA Dynamo in Action" carousel. They are summarized as resource links rather than saved as body figures. Original inline page images saved here are the Dynamo inference diagram, Dynamo Office Hours image, and Blackwell/Dynamo performance illustration.

## Content

## NVIDIA Dynamo

NVIDIA Dynamo is an open source, low-latency, modular inference framework for serving generative AI models in distributed environments. It is positioned for scaling inference workloads across large GPU fleets with intelligent resource scheduling and request routing, optimized memory management, and seamless data transfer.

The page says Dynamo supports open source inference engines including SGLang, TensorRT LLM, and vLLM. It frames Dynamo as a way to simplify distributed serving by disaggregating phases of inference across GPUs, intelligently routing requests to appropriate GPUs to avoid redundant computation, and extending GPU memory through data caching to cost-effective storage tiers.

NVIDIA also positions Dynamo with GB300 NVL72 for large-scale mixture-of-experts inference. The page states that independent benchmarks show GB300 NVL72 combined with Dynamo improves MoE model throughput by up to 50x compared to NVIDIA Hopper-based systems. It attributes this to 72 GPUs connected through NVIDIA NVLink for low-latency expert communication, plus Dynamo's disaggregated inference that splits prefill and decode phases across nodes for independent optimization.

The page describes Dynamo as building on the successes of NVIDIA Triton Inference Server, which standardized AI model deployment and execution across workloads.

Primary calls to action:

- Get Started: https://github.com/ai-dynamo/dynamo
- Documentation: https://docs.nvidia.com/dynamo/latest/

## See NVIDIA Dynamo in Action

This section is a video/resource carousel. Relevant entries for downstream comparison with llm-d and inference gateway themes include:

- "State of NVIDIA Dynamo", covering the current state of the open-source project and key features.
- "Under the Hood: Dynamo End-to-End Design", covering Dynamo end-to-end architecture.
- "Inference OSS Ecosystem featuring vLLM", covering large-scale LLM serving with vLLM and disaggregated serving.
- "Inference OSS Ecosystem featuring TensorRT LLM", introducing TensorRT LLM.
- "Inference OSS Ecosystem featuring llm-d", introducing llm-d as a distributed open-source framework for LLM inference. This is the clearest same-page comparable point for llm-d.
- "Inference OSS Ecosystem featuring SGLang", discussing SGLang and Dynamo for production DeepSeek serving.
- "Solving KV Caching Bottlenecks with Tensormesh", discussing LMCache with Dynamo and engines like vLLM.
- "Solving KV Caching Bottlenecks with Dynamo's KV Block Manager (KVBM)", discussing KV-cache-driven LLM inference with LMCache and Dynamo's KVBM.
- "The Future of AI Inference", surveying large-scale inference and disaggregated designs.

The page links the full playlist via NVIDIA On-Demand and YouTube:

- NVIDIA On-Demand playlist: https://www.nvidia.com/en-us/on-demand/playlist/playList-e42aee58-4db9-4ce4-8a6f-c41d8e272d72/
- YouTube playlist: https://www.youtube.com/playlist?list=PL5B692fm6--tgryKu94h2Zb7jTFM3Go4X

## How NVIDIA Dynamo Works

The page frames the problem as follows: models are becoming larger and are increasingly part of AI workflows that interact with multiple models. Deploying them at scale requires distribution across multiple nodes and careful GPU coordination. Optimization methods such as disaggregated serving split response work across different GPUs, which adds coordination and data-transfer challenges.

NVIDIA says Dynamo addresses distributed and disaggregated inference serving through the following components:

- SLO Planner: A planning and scheduling engine that monitors capacity and prefill activity in multi-node deployments, adjusting GPU resources to meet Service Level Objectives.
- KV-aware Router: A KV-cache-aware routing engine that directs incoming traffic across large GPU fleets in multi-node deployments to minimize redundant KV cache recomputation.
- Low-Latency Communication Library (NIXL): A point-to-point inference data transfer library for accelerating KV cache transfer between GPUs and across heterogeneous memory and storage types.
- KV Block Manager: A cost-aware KV caching engine that transfers KV cache across memory hierarchies, freeing GPU memory while maintaining user experience.
- Grove: A modular Dynamo component for deploying hierarchical gang-scheduled and topology-aware AI workloads on Kubernetes.
- AI Perf: A benchmarking tool for measuring performance of generative AI models served by SGLang, TensorRT LLM, and vLLM.

![A flowchart of how NVIDIA Dynamo works](images/image-01.webp)

Image source: https://developer.download.nvidia.com/images/dynamo/dynamo-devzone-inference-diagram.png

Caption / nearby text: A flowchart of how NVIDIA Dynamo works.

## NVIDIA Dynamo Key Moments

The page promotes live NVIDIA Dynamo Office Hours sessions where developers can ask questions, share feedback, and learn from the Dynamo team. It says each episode covers topics related to Dynamo and inference, helping developers build, optimize, and deploy AI models.

![NVIDIA Dynamo Office Hours](images/image-02.webp)

Image source: https://developer.download.nvidia.com/images/nvidia-dynamo-key-moments.jpg

Caption / nearby text: NVIDIA Dynamo Office Hours / NVIDIA Dynamo Key Moments.

## Get Started With NVIDIA Dynamo

The page lists several starting points:

- Quick-Start Guide: Learn the basics for getting started with Dynamo, including deploying a model in a disaggregated server setup and launching the smart router. Link: https://docs.nvidia.com/dynamo/v-0-8-1/getting-started/quickstart
- Dynamo 1.0 Blog: Details early adopter integration into real-world inference workflows, system-level performance improvements, and latest framework features and optimizations. Link: https://developer.nvidia.com/blog/nvidia-dynamo-1-production-ready/?nvid=nv-int-tblg-327957
- Deploy LLM Inference With NVIDIA Dynamo and vLLM: Tutorial for deployment with vLLM. Link: https://github.com/ai-dynamo/dynamo/tree/main/examples/backends/vllm
- Multi-Node Deployment With NVIDIA Dynamo and Grove on Kubernetes: Describes multi-node deployment using Dynamo with Grove API, including efficient scaling and declarative startup ordering of interdependent AI inference components across nodes. Link: https://docs.nvidia.com/dynamo/v-0-9-0/kubernetes-deployment/multinode/multinode-deployments
- Introductory Blog: Describes how Dynamo simplifies AI inference in production, deployment tools, and ecosystem integrations. Link: https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/

## Licensing and Availability

The page says Dynamo is available as open source software on GitHub with end-to-end examples:

- NVIDIA Dynamo GitHub repository: https://github.com/ai-dynamo/dynamo

It also states that Dynamo is the successor to NVIDIA Triton Inference Server and links the earlier Triton repository:

- NVIDIA Triton Inference Server GitHub repository: https://github.com/triton-inference-server/server

For enterprise use, the page says NVIDIA AI Enterprise will include Dynamo for production inference in a future release and offers a 90-day license path:

- NVIDIA AI Enterprise: https://www.nvidia.com/en-us/data-center/products/ai-enterprise/
- Request a 90-day license: https://enterpriseproductregistration.nvidia.com/?LicType=EVAL&ProductFamily=NVAIEnterprise
- Contact NVIDIA about Dynamo: https://www.nvidia.com/en-us/data-center/products/ai-enterprise/contact-sales/

## Starter Kits

The page groups related technical content into starter kits for inference optimization.

### Multi-GPU Inference

The page says models have grown too large for a single GPU, so deployment requires distribution across multiple GPUs and nodes. The kit collects optimization techniques for multi-GPU inference:

- MultiShot communication protocol: https://developer.nvidia.com/blog/3x-faster-allreduce-with-nvswitch-and-tensorrt-llm-multishot/
- Pipeline Parallelism for High-Concurrency Efficiency: https://developer.nvidia.com/blog/boosting-llama-3-1-405b-throughput-by-another-1-5x-on-nvidia-h200-tensor-core-gpus-and-nvlink-switch/
- Large NVIDIA NVLink domains: https://developer.nvidia.com/blog/low-latency-inference-chapter-2-blackwell-is-coming-nvidia-gh200-nvl32-with-nvlink-switch-gives-signs-of-big-leap-in-time-to-first-token-performance/

### Prefill Optimizations

The page describes prefill as the stage where a request to a large language model generates a KV cache to compute contextual understanding. It characterizes the process as computationally intensive and requiring specialized optimization:

- Key-value cache early reuse: https://developer.nvidia.com/blog/5x-faster-time-to-first-token-with-nvidia-tensorrt-llm-kv-cache-early-reuse/
- Chunked prefill: https://developer.nvidia.com/blog/streamlining-ai-inference-performance-and-deployment-with-nvidia-tensorrt-llm-chunked-prefill/
- Supercharging multiturn interactions: https://developer.nvidia.com/blog/nvidia-gh200-superchip-accelerates-inference-by-2x-in-multiturn-interactions-with-llama-models/

### Decode Optimizations

The page describes decode as the autoregressive generation phase after the LLM generates the KV cache and first token:

- Multiblock attention for long sequences: https://developer.nvidia.com/blog/nvidia-tensorrt-llm-multiblock-attention-boosts-throughput-by-more-than-3x-for-long-sequence-lengths-on-nvidia-hgx-h200/
- Speculative decoding for accelerated throughput: https://developer.nvidia.com/blog/tensorrt-llm-speculative-decoding-boosts-inference-throughput-by-up-to-3-6x/
- Speculative decoding with Medusa: https://developer.nvidia.com/blog/low-latency-inference-chapter-1-up-to-1-9x-higher-llama-3-1-performance-with-medusa-on-nvidia-hgx-h200-with-nvlink-switch/

### Topology-Optimized Serving on Kubernetes

The page says AI workloads have evolved into complex multi-component systems spanning multiple nodes. Grove bridges AI inference frameworks and Kubernetes scheduling, enabling efficient scaling and declarative startup ordering of interdependent components through unified custom resources.

Related links:

- Optimizing the Deployment of Interdependent AI Inference Components: https://developer.nvidia.com/dynamo
- Developer Workflow of Grove API: https://github.com/ai-dynamo/grove/blob/main/docs/quickstart.md
- NVIDIA Grove GitHub Repository: https://github.com/ai-dynamo/grove

## NVIDIA Blackwell Ultra Performance and Dynamo

The page includes a resource titled "NVIDIA Blackwell Ultra Delivers up to 50x Better Performance and 35x Lower Cost for Agentic AI." It says Blackwell Ultra is built for agentic AI and lower cost, with cloud providers deploying NVIDIA GB300 NVL72 systems for low-latency and long-context use cases such as agentic coding and coding assistants.

The page attributes the result to co-design across NVIDIA Blackwell, NVLink, NVLink Switch, NVFP4, NVIDIA Dynamo, and TensorRT LLM, with development through community frameworks including SGLang and vLLM.

![Data center illustration showing multi-modal AI tokens for image, audio, visual and more as part of the NVIDIA Think SMART framework](images/image-03.webp)

Image source: https://developer.download.nvidia.com/images/dgx-press-gb300-1920x1080.jpg

Caption / nearby text: Data center illustration showing multi-modal AI tokens for image, audio, visual and more as part of the NVIDIA "Think SMART" framework.

Related link:

- Explore Key Results: https://blogs.nvidia.com/blog/data-blackwell-ultra-performance-lower-cost-agentic-ai/?nvid=nv-int-bnr-552734

## More Resources

The page links additional NVIDIA developer resources:

- Explore Developer Discord: https://discord.com/invite/nvidia-dynamo
- Get Training and Certification: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-03+V1
- Watch Dynamo Office Hours On-Demand: https://www.youtube.com/playlist?list=PL5B692fm6--tgryKu94h2Zb7jTFM3Go4X
- Sign Up for Inference-Related Developer News: https://developer.nvidia.com/email-signup
- Read NVIDIA Dynamo FAQ: https://forums.developer.nvidia.com/t/nvidia-dynamo-faq/327484
- Join the NVIDIA Developer Program: https://developer.nvidia.com/developer-program

## Ethical AI

The page includes NVIDIA's standard trustworthy AI statement. It says trustworthy AI is a shared responsibility and points developers to model-card subcards for explainability, bias, safety and security, and privacy considerations. It also asks readers to report security vulnerabilities or NVIDIA AI concerns through NVIDIA's support channel.

Security / AI concern reporting link: https://www.nvidia.com/en-us/support/submit-security-vulnerability/

## Downstream Notes for GKE Inference Gateway / llm-d Comparison

- Dynamo's routing claim is KV-cache-aware routing across GPU fleets to reduce redundant KV recomputation. This is directly relevant to latency-sensitive request routing discussions.
- Dynamo explicitly separates prefill and decode phases across nodes, which is the page's primary disaggregated serving claim.
- KV movement is split across NIXL for low-latency transfer and KVBM for cost-aware movement across memory/storage tiers.
- Grove is the Kubernetes-oriented component to compare with GKE/Kubernetes deployment concerns: topology-aware workloads, gang scheduling, multi-node deployment, scaling, and startup ordering of interdependent inference components.
- The page itself mentions llm-d through an ecosystem video entry, but it does not give technical comparison details. Treat the NVIDIA Docs introduction and the linked llm-d ecosystem talk as follow-up sources if deeper comparison is needed.

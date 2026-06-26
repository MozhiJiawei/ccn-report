# Introducing the next generation of AI inference, powered by llm-d

Source: https://cloud.google.com/blog/products/ai-machine-learning/enhancing-vllm-for-distributed-inference-with-llm-d
Captured: 2026-06-25

## Source Notes

- Publisher: Google Cloud Blog
- Page title: Google Cloud Blog: Enhancing vLLM for distributed inference with llm-d
- Article title: Introducing the next generation of AI inference, powered by llm-d
- Date: 2025-05-21
- Authors: Mark Lohmeyer, VP and GM, AI and Computing Infrastructure; Gabe Monroy, VP & GM, Cloud Runtimes
- Selected content: main blog article body, excluding promotional cards, social sharing links, tags, and related-article recommendations.
- Capture notes: rendered in browser before extraction. The article contains one正文 architecture image; duplicate DOM copies of the same image were deduplicated. Related-article thumbnails were intentionally excluded.

## Content

As AI deployments move from prototypes to scaled production, the article frames efficient inference as a gating factor. It says the earlier bottleneck was model size, while the newer pressure comes from agentic workflows and reasoning models that create highly variable demand, slowing inference and harming user experience.

Google Cloud positions open-source inference engines such as vLLM as central to the response. The article notes Google Cloud Next 25 announcements for vLLM support on Cloud TPUs across Google Kubernetes Engine (GKE), Google Compute Engine, Vertex AI, and Cloud Run. It also connects this to the Gateway API Inference Extension and GKE Inference Gateway, which add AI-native routing to Kubernetes for inference workloads. The article mentions customer use by Samsung and BentoML, and future use with seventh-generation Ironwood TPU infrastructure.

The core announcement is llm-d: an open-source project for Kubernetes-native distributed and disaggregated inference that makes vLLM scalable. Google Cloud is described as a founding contributor alongside Red Hat, IBM Research, NVIDIA, and CoreWeave, with AMD, Cisco, Hugging Face, Intel, Lambda, and Mistral AI also named as industry participants. The article presents llm-d as community-led infrastructure intended to run broadly across environments.

The mechanism section states that llm-d builds on the vLLM inference engine and adds distributed serving technology. It highlights three major innovations:

- vLLM-aware inference scheduler: instead of traditional round-robin load balancing, it routes requests to instances with prefix-cache hits and low load so latency SLOs can be met with fewer hardware resources.
- Disaggregated serving: longer requests can be served with higher throughput and lower latency by separating the prefill and decode stages of LLM inference onto independent instances.
- Multi-tier KV cache: intermediate prefix values can be reused across storage tiers to improve response time and reduce storage cost.

The article also says llm-d works across frameworks, with PyTorch supported at publication time and JAX planned later in 2025, and across GPU and TPU accelerators.

![llm-d stack architecture diagram](images/image-01.jpg)

Image source: https://storage.googleapis.com/gweb-cloudblog-publish/images/llm-d_stack_v1.max-2200x2200.jpg

Caption / nearby context: The article places this architecture image after the paragraph describing llm-d's three major innovations: vLLM-aware scheduling, disaggregated serving for prefill/decode, and multi-tier KV caching.

The final paragraph describes llm-d as a Kubernetes stack for cost-effective distributed serving. On Google Cloud, the article says llm-d can use Google Cloud's global network, GKE AI capabilities, and AI Hypercomputer integrations across software and hardware accelerators. It reports early Google Cloud tests showing 2x improvements in time-to-first-token for use cases such as code completion.

The article closes by directing readers to the llm-d project:

- llm-d project: https://github.com/llm-d/llm-d
- llm-d architecture link from the article: https://github.com/llm-d/llm-d?tab=readme-ov-file#-architecture

## Key Mechanisms And Boundaries

- llm-d/vLLM-aware scheduler: the scheduling claim is specifically about routing to vLLM instances with prefix-cache hits and low load, rather than simple round-robin distribution.
- Disaggregation: the article's disaggregation boundary is the LLM inference split between prefill and decode stages, served by independent instances.
- Kubernetes integration: llm-d is framed as Kubernetes-native and connected to GKE, Gateway API Inference Extension, and GKE Inference Gateway for AI-native routing.
- Hardware and framework scope: the article claims GPU and TPU accelerator support, PyTorch support at publication, and JAX later in 2025.
- Evidence boundary: the 2x time-to-first-token improvement is reported as early Google Cloud testing for use cases like code completion; the article does not include a benchmark methodology, model list, traffic mix, or reproducibility details.

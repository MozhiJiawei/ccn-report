# Source Selection

输入类型：web

主题：Google Cloud GKE Inference Gateway 宣称可减少 92% 的 AI 响应延迟

## 原始页面候选

1. Google Cloud Blog: GKE Inference Gateway prefix caching accelerates AI inference
   URL: https://cloud.google.com/blog/products/containers-kubernetes/gke-inference-gateway-prefix-caching-accelerates-ai-inference
   角色：92.8% TTFT 降低、15.7% throughput 提升、62.6% ITL 降低的直接出处，并包含 benchmark 条件和 Principled Technologies 来源标注。

2. Google Cloud Docs: About GKE Inference Gateway powered by llm-d
   URL: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway
   角色：官方机制说明，解释 prefix-cache aware routing、load-aware routing、LoRA-aware routing 和 InferencePool/Objective 等对象。

3. Google Cloud Blog: Enhancing vLLM for distributed inference with llm-d
   URL: https://cloud.google.com/blog/products/ai-machine-learning/enhancing-vllm-for-distributed-inference-with-llm-d
   角色：GKE Inference Gateway 背后的 llm-d / vLLM-aware scheduler 技术路线说明，用于连接产品宣称与开源实现。

## 同类/相邻/竞品方案候选

1. NVIDIA Dynamo — NVIDIA Developer: Dynamo Inference Framework
   URL: https://developer.nvidia.com/dynamo
   对照角色：NVIDIA 官方产品/项目介绍页，说明 Dynamo 作为开源低延迟分布式推理框架，覆盖智能资源调度、请求路由、内存管理和数据传输；适合与 llm-d 的 Kubernetes-native/Gateway API 路线做同层对比。
   备用细化来源：https://docs.nvidia.com/dynamo/getting-started/introduction

2. AIBrix — vLLM Blog: Introducing AIBrix: A Scalable, Cost-Effective Control Plane for vLLM
   URL: https://vllm.ai/blog/2025-02-21-aibrix-release
   对照角色：vLLM 官方博客介绍 AIBrix，说明其作为 vLLM 控制面覆盖 distributed KV cache、P&D aggregation、request migration、cross-instance KV reuse、QoS/Priority/Fairness；适合比较 llm-d 与 AIBrix 在控制面、KV cache 复用、路由策略和生产化边界上的差异。
   备用细化来源：https://aibrix.github.io/posts/2025-02-20-vllm-control-plane/

# Source Map

Captured on 2026-06-25 for `source_understanding_review.html`.

## Slide 1: 结论

- Source: `sources/web/google-gke-inference-gateway-prefix-caching/source.md`
- Evidence: 92.8% TTFT, 15.7% throughput, 62.6% ITL, shared-prefix workload, 8x A100 40GB, round-robin comparison.
- Visual: Google Cloud benchmark chart image.

## Slide 2: 证据口径

- Source: `sources/web/google-gke-inference-gateway-prefix-caching/source.md`
- Evidence: benchmark table values and benchmark conditions.
- Visual: Google Cloud benchmark chart image plus metric overlays.
- Boundary: Principled Technologies PDF was linked by Google but not captured in full.

## Slide 3: 机制

- Source: `sources/web/google-docs-about-gke-inference-gateway/source.md`
- Evidence: llm-d EPP, KV cache utilization, queue length, prefix cache state, LoRA adapter affinity, prefix/load/LoRA aware routing.
- Source: `sources/web/google-llm-d-vllm-distributed-inference/source.md`
- Evidence: vLLM-aware scheduler and prefix-cache hit routing.
- Visual: Google Cloud request flow diagram.

## Slide 4: 产品结构

- Source: `sources/web/google-docs-about-gke-inference-gateway/source.md`
- Evidence: InferencePool, InferenceObjective, Gateway Mode, L7 Proxy, EPP, shared infrastructure, advanced traffic management.
- Visual: Google Cloud GKE Inference Gateway resource model.

## Slide 5: llm-d 路线

- Source: `sources/web/google-llm-d-vllm-distributed-inference/source.md`
- Evidence: vLLM-aware inference scheduler, disaggregated serving, multi-tier KV cache, early 2x TTFT claim and evidence boundary.
- Visual: Google Cloud llm-d stack architecture diagram.

## Slide 6: Dynamo 对照

- Source: `sources/web/nvidia-dynamo-inference-framework/source.md`
- Evidence: Dynamo positioning, SLO Planner, KV-aware Router, NIXL, KVBM, Grove, AI Perf.
- Visual: NVIDIA Dynamo architecture and components diagram.

## Slide 7: AIBrix 对照

- Source: `sources/web/vllm-aibrix-control-plane/source.md`
- Evidence: AIBrix positioning, LLM Gateway and Routing, autoscaler, distributed inference, distributed KV cache, P&D aggregation, request migration, QoS/Priority/Fairness.
- Visual: AIBrix control-plane diagram.

## Slide 8: 适用边界

- Source: `sources/web/google-gke-inference-gateway-prefix-caching/source.md`
- Evidence: RAG/codebase Q&A, multi-turn chat examples, Snap 75-80% prefix cache hit quote.
- Source: `sources/web/google-docs-about-gke-inference-gateway/source.md`
- Evidence: supported metrics and route scoring.
- Visual: static-prefix / dynamic-suffix prompt reuse diagram.

## Slide 9: 证据审计

- Sources: all captured source packages.
- Purpose: separate strong evidence, medium evidence, and evidence requiring follow-up before content brief.
- Visual: A/B/C evidence ladder.

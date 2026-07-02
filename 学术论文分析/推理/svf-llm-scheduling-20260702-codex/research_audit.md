# Research Audit: SVF for LLM Serving Scheduling

## Scope

- Topic: Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice
- Source set: arXiv paper `2606.22327`, local PDF/text/XML parse, Docling-exported figures and tables, and the paper-declared companion GitHub repository for code availability checks.
- User constraint: no external comparison papers or solution benchmarks; companion GitHub is used only to verify open-source status.

## Source Integrity

- arXiv URL: https://arxiv.org/abs/2606.22327
- Source PDF/text/XML were parsed during report generation from arXiv `2606.22327`.
- Archived figure/table assets used by the final report are stored in this directory under `assets/`.
- GROBID/Docling validation: valid; 6 images exported and referenced.
- Companion code repository: `https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling`
- GitHub repository tree check: public repo includes `predictor/latency_prediction.py`, `predictor/evaluate_predictor_accuracy.py`, `predictor/llama3_preprocess_dataset.py`, scheduling scripts, and overhead scripts.

## Corrected Framing

- The user-provided clue says "IIT Bombay etc."; the paper metadata and local parse do not support IIT Bombay affiliation. The deck should avoid naming IIT Bombay unless a later source is added.
- The more precise claim is not simply "48 to 5": Theorem 3.2 states `CR <= 1 + 2/(1-alpha)`. Table 1 gives `CR <= 5.00` at `alpha = 1/2`, and the corollary says the bound approaches `3` as `alpha -> 0`.

## Evidence Claims

### Strong Claims

1. SVF changes the scheduling priority from 1D time to 2D memory-time volume.
   - Evidence: Section 2.2 defines `v_i = s_i * o_i + (o_i^2 + o_i) / 2`.
   - Visual: `picture_001.webp`.

2. Under burst arrivals, SVF has a worst-case competitive ratio bound of `1 + 2/(1-alpha)`.
   - Evidence: Theorem 3.2.
   - Visual: `table_001.webp`.

3. The bound approaches 3 in the high-concurrency regime.
   - Evidence: Corollary 3.2.1 and Table 1.
   - Boundary: high concurrency corresponds to small `alpha`, where `alpha = max_i p_i / M`.

4. The `CR <= 5` number is the conservative half-capacity point, not the paper's asymptotic headline.
   - Evidence: Corollary 3.2.2 and Table 1 show `alpha = 1/2`, minimum concurrency `2`, `CR <= 5.00`.

5. 1-bit SVF uses only binary short/long classification and proxy volume.
   - Evidence: Section 2.2 and Theorem 3.3.
   - Boundary: it preserves the geometry idea but does not match full SVF's exact volume ordering.

6. Experiments are implemented as a plug-and-play layer in vLLM and evaluated on Llama-3.1-8B/70B.
   - Evidence: Section 4.1.
   - Setup: 8 NVIDIA A100 80GB GPUs; 8B on one GPU; 70B on all 8 GPUs with tensor parallelism; context 65,536; max generation 4,096.

7. In burst experiments, SVF generally has the best non-oracle average latency and often best P95 latency.
   - Evidence: Table 2 and Section 4.2.
   - Boundary: throughput is not always highest for SVF; 1-bit SVF sometimes leads throughput.

8. Predictor overhead is reported as tiny.
   - Evidence: Table 3 reports full regression at max 0.06% overhead and classifier at about 0.01%.
   - Boundary: measured on Meta-Llama-3.1-8B-Instruct with N=200 concurrent requests.

9. The predictor training and evaluation code is open, but trained predictor weights were not found in the repository tree.
   - Evidence: GitHub README exposes `predictor/` workflow: preprocessing, BERT-base regression training, BERT-tiny 1-bit classification training, and `evaluate_predictor_accuracy.py`.
   - Evidence: repository tree contains predictor scripts but no `.pth`, `.pt`, `.safetensors`, or `.bin` checkpoint files.
   - Boundary: BERT-tiny as a base model is publicly available, but the paper-specific fine-tuned 1-bit classifier checkpoint appears to require local training from the provided pipeline.

### Weak Or Context-Bound Claims

1. "Empirically proven for production" should be softened.
   - Reason: experiments are on selected models, datasets, hardware, and simulated arrivals.

2. "1-bit SVF is always better than SJF" should be avoided.
   - Reason: the paper says 1-bit SVF has slightly higher average latency than SJF in LMSYS chatbot workloads, while outperforming in LongBench and throughput.

3. "No starvation" should be softened to "the paper argues tail latency/fairness improves".
   - Reason: the paper uses empirical P95 and a qualitative fairness remark, not a standalone starvation theorem.

4. "5x improvement" should not be used.
   - Reason: 48 and 5 are competitive ratio upper bounds under different assumptions; the paper claims bound tightening, not measured speedup.

5. "The prediction model is open-source and ready to use" should be avoided.
   - Reason: code is open, but trained paper-specific predictor/classifier checkpoints are not evidently published in the GitHub repo.

## Recommended Storyline

1. Problem: LLM serving scheduling is no longer a pure time problem because KV cache grows during decoding.
2. Mechanism: SVF ranks requests by memory-time volume, aligning greedy admission with the lower bound used for OPT.
3. Theory: the new certificate yields `1 + 2/(1-alpha)`, explaining 5 at `alpha=1/2` and near-3 at high concurrency.
4. Practice: vLLM implementation on Llama-3.1 shows latency gains, especially on memory-intensive LongBench.
5. Caveat: the method needs length prediction/classification and evidence remains paper-bounded.
6. Reproducibility caveat: the companion repository opens the training/evaluation pipeline, but users likely need to train their own predictor weights.

## Image Inventory

- `picture_001.webp`: Figure 1, LLM inference process and volume calculation.
- `table_001.webp`: Table 1, competitive ratio vs alpha.
- `table_002.webp`: Table 2, burst-arrival performance.
- `picture_002.webp`: Figure 2, Poisson arrival practical performance.
- `picture_003.webp`: Figure 3, theoretical claim validation.
- `table_003.webp`: Table 3, predictor overhead.

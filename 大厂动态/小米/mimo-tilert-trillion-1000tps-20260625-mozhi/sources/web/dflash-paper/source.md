# DFlash: Block Diffusion for Flash Speculative Decoding

- Source URL: https://arxiv.org/abs/2602.06036
- HTML source URL: https://arxiv.org/html/2602.06036v1
- GitHub source URL: https://github.com/z-lab/dflash
- Captured date: 2026-06-25
- Authors: Jian Chen, Yesheng Liang, Zhijian Liu
- Published: 2026-02-05

## Source Role

This package supplements the MiMo × TileRT source-understanding deck with DFlash-specific mechanism details and original diagrams.

The MiMo and HuggingFace model-card sources explain how MiMo-V2.5-Pro-FP4-DFlash uses DFlash, but they do not fully explain the underlying DFlash mechanism. This source fills that gap using the DFlash paper and project repository.

## Core Mechanism

DFlash is a speculative decoding framework that uses a lightweight block diffusion model as the drafter. It keeps the high-quality autoregressive target model as verifier, but changes the draft stage from sequential autoregressive token generation to parallel block prediction.

The paper frames the problem as a two-sided trade-off:

- Autoregressive LLMs are high quality but decode token by token.
- Diffusion/block-diffusion models can predict masked tokens in parallel, but standalone diffusion LLM quality is usually weaker.
- DFlash confines diffusion to the speculative draft stage, then lets the target autoregressive model verify the draft so output quality remains governed by the target model.

## Why It Differs From EAGLE-Style Drafting

Autoregressive drafters generate draft tokens sequentially. Their draft cost grows with the number of speculative tokens. DFlash predicts all masked positions in a block in one forward pass, so draft latency is much less sensitive to block length.

The DFlash paper says this changes the design space: the drafter can be deeper and more expressive while still keeping drafting latency low.

## Target Feature Conditioning

DFlash's key insight is that the target model's hidden states contain information useful for predicting future tokens. During inference, the target model produces hidden context features. DFlash fuses hidden states from fixed layers and injects them into every draft layer's Key/Value cache.

This KV injection differs from feeding target features only as the draft model's input: persistent KV conditioning keeps target information available throughout all draft layers, so acceptance length can scale with draft depth.

## Inference Design Figure

![DFlash Inference Design](images/image-02-inference-design.webp)

Original image URL: https://arxiv.org/html/2602.06036v1/x2.png

Caption / nearby text: Figure 2, DFlash Inference Design. Hidden context features extracted from the target model are fused and injected into each draft layer's Key-Value cache to enable conditional speculation.

## Training Attention Figure

![DFlash training attention](images/image-04-training-attention.webp)

Original image URL: https://arxiv.org/html/2602.06036v1/x4.png

Caption / nearby text: Figure 4, DFlash training attention. The target model provides context features that condition the draft model. Masked blocks contain clean anchor tokens and mask tokens for parallel prediction, while invisible tokens prevent cross-block leakage.

## Speedup Comparison Figure

![DFlash speedup comparison](images/image-01-speedup.webp)

Original image URL: https://arxiv.org/html/2602.06036v1/x1.png

Caption / nearby text: Figure 1, DFlash and EAGLE-3 speedup against autoregressive decoding on Qwen3-8B with the Transformers backend.

## Draft Cost Figure

![DFlash draft cost](images/image-03-draft-cost.webp)

Original image URL: https://arxiv.org/html/2602.06036v1/x3.png

Caption / nearby text: Figure 3, draft cost of 1-, 3-, 5-layer DFlash and 1-layer EAGLE-3.

## Training Details Relevant To Slides

- DFlash trains draft models to align block-level diffusion predictions with outputs of a frozen autoregressive target model.
- During training, clean sequences are passed through the target model to extract hidden features for all tokens; those features are injected into draft model Key/Value projections.
- Masked blocks are sampled around clean anchor tokens so training matches inference behavior: the draft model conditions on a clean token produced by the target model.
- Tokens attend bidirectionally within the same block and to corresponding injected target context features, while attention across blocks is disallowed.
- Loss is weighted toward earlier positions in the draft block because an early wrong token invalidates later accepted tokens.
- The draft model shares the target token embedding and LM head; only draft Transformer layers are trained.

## Project Page / Repository Notes

The GitHub README describes DFlash as a lightweight block diffusion model for speculative decoding and shows it supports multiple serving backends:

- vLLM: DFlash support is included in vLLM v0.20.1+ according to the README.
- SGLang: launch uses `--speculative-algorithm DFLASH` and `--speculative-num-draft-tokens`.
- Transformers and MLX examples are provided for supported models.

Repository README also lists supported DFlash draft models and states that training recipe open-sourcing is planned.

## Evidence Boundaries

- The DFlash paper reports results on Qwen3 and related models, not Xiaomi MiMo-V2.5-Pro itself.
- MiMo's DFlash integration changes the concrete settings: MiMo model card uses a 5-layer drafter, block size 8, captured backbone layers [0, 15, 31, 47, 69], and BF16 drafter.
- DFlash's lossless guarantee is the speculative decoding guarantee relative to the target verifier distribution, not a claim that every draft token is correct.
- The paper's speedup figures are not the same benchmark as MiMo/TileRT's 8-GPU 1000+ tokens/s claim.

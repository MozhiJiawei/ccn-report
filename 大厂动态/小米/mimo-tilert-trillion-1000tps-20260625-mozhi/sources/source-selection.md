# Source Selection

Task: MiMo 与 TileRT 在 8-GPU 节点上实现万亿参数模型超 1000 token/s 解码技术

Input type: web

Status: approved by user with scope narrowed to original sources only; comparable / adjacent sources removed.

## Proposed Original Sources

1. MiMo-V2.5-Pro-UltraSpeed: Pushing 1T-Parameter Model Generation Speed Beyond 1000 TPS
   - URL: https://mimo.xiaomi.com/blog/mimo-tilert-1000tps
   - Reason: Official Xiaomi MiMo blog post; primary source for the 1000+ tokens/s claim, technique stack, pricing/API announcement, and evidence figures.

2. Xiaomi MiMo Partners with TileRT | 1T Model Breaks 1000 tokens/s
   - URL: https://mimo.mi.com/docs/en-US/news/latest/1000tps
   - Reason: Official MiMo documentation/news page; concise primary-source announcement with cited references including MXFP4 and DFlash.

3. XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash model card
   - URL: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
   - Reason: Claimed open checkpoint location; needed to verify released artifact, model/config metadata, quantization/DFlash packaging, and reproducibility boundary.

4. DFlash: Block Diffusion for Flash Speculative Decoding
   - URL: https://arxiv.org/abs/2602.06036
   - Supplementary project URL: https://github.com/z-lab/dflash
   - Reason: User requested deeper DFlash explanation and technical diagrams; this is the original DFlash paper/project source for inference design, training attention, and speedup/draft-cost figures.

## Comparable / Adjacent Sources

User decision: not needed. This is not a single-point technical comparison task; capture original sources only.

## Evidence Gaps To Verify After Approval

- Exact hardware configuration behind "standard 8-GPU node" and whether GPU model is disclosed.
- Whether "1000 tokens/s" is single-request decode speed, aggregate throughput, accepted-token speed under speculation, or demo-observed streaming rate.
- Batch size, concurrency, prompt/output length, context length, and sampling settings.
- MiMo-V2.5-Pro total/active parameters and MoE expert structure.
- FP4/MXFP4 quantization scope and quality-retention evidence.
- DFlash acceptance length, draft cost, and whether output is mathematically equivalent to target-model sampling.
- TileRT runtime mechanisms and how much of the result depends on closed runtime versus released checkpoint.
- Comparability with mainstream frameworks such as vLLM, SGLang, TensorRT-LLM, and vendor benchmark conventions.
- DFlash-specific mechanism: target hidden-feature conditioning, KV injection, block diffusion training attention, and how those details map onto MiMo's 5-layer BF16 drafter and block size 8.

# Source Map

## Core Claims

| Claim | Evidence | Boundary |
| --- | --- | --- |
| Incremental BPE reaches worst-case `O(n log^2 t)` over input length `n` and maximum token length `t`. | Abstract; Section 5 complexity analysis; Table 6. | Complexity is for the BPE stage; full tokenizer pipeline may still be dominated by normalization, pre-tokenization, regex, or output construction. |
| The algorithm is exact with respect to standard BPE merge rules. | Abstract; structural sections on canonical token hierarchy, successor forest, monotonic path property. | Exactness assumes a fixed BPE vocabulary and merge-rule semantics. |
| The practical speedup can reach about 3x, but the average gain depends heavily on tokenizer and dataset. | Table 1; detailed Table 5. | CodeLlama on code shows the highest gain; many tiktoken/HF rows are near 1x. |
| Pathological repeated-character inputs expose baseline degradation, while the proposed algorithm stays stable. | Figure 3; Figure 7; robustness section. | The dramatic improvement is most relevant to adversarial or unusual long repeated inputs, not ordinary text in every pipeline. |
| Eager output makes streaming output possible after token boundaries become stable. | Section 6; Appendix G; Table 6. | Eager output adds about 10% overhead in reported end-to-end throughput. |
| End-to-end inference throughput may improve through pipelining, but the paper does not prove a universal 3x model-serving gain. | Figure 1; Future Work; profiling Appendix I. | Non-BPE stages and model-side scheduling still need local validation. |

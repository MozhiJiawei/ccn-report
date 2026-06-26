# Source Selection

## Input Type

paper

## Original Sources

1. Incremental BPE Tokenization
   - PDF: `.tmp/ppt-deep-search/incremental-bpe-tokenization-throughput/paper/incremental-bpe-tokenization.pdf`
   - XML: `.tmp/ppt-deep-search/incremental-bpe-tokenization-throughput/pdf_xml/incremental-bpe-tokenization/final/incremental-bpe-tokenization.xml`
   - Images: `.tmp/ppt-deep-search/incremental-bpe-tokenization-throughput/pdf_xml/incremental-bpe-tokenization/final/images/`
   - Intermediate archive: `.tmp/ppt-deep-search/incremental-bpe-tokenization-throughput/pdf_xml/incremental-bpe-tokenization/incremental-bpe-tokenization.intermediate_parse_results.zip`

## Peer / Adjacent Schemes For Contrast

1. Standard offline BPE implementations in Hugging Face `tokenizers`
   - Contrast role: main practical baseline for end-to-end throughput speedup claims.
2. OpenAI `tiktoken` baseline and rust-gems incremental implementations
   - Contrast role: robustness and algorithmic-complexity baseline, especially under pathological repeated-character inputs.

## Selected Evidence For Source Understanding

- Figure 1 / `picture_001.png`: modern LLM tokenization pipeline and where BPE sits.
- Figure 2 / `picture_002.png`: Successor Forest and Suffix-Successor Tree intuition.
- Figure 3 / `picture_003.png`: pathological-input throughput stability.
- Figure 5 / `picture_005.png` and Figure 6 / `picture_006.png`: profiling shows non-BPE stages can dominate.
- Figure 7 / `picture_007.png`: baseline tiktoken pathological scaling.
- Table 1 / `table_002.png`: end-to-end speedup factors.
- Table 6 / `table_010.png`: complexity and feature comparison.
- Figure 8 / `table_012.png`: comparison with other incremental BPE implementations.

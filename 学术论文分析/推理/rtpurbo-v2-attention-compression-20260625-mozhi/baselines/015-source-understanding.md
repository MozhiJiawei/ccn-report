# 015 Source Understanding Baseline

Status: approved by user on 2026-06-25.

## Approved Artifact

- HTML: D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\ppt-deep-search\ptrurbov2-attention-compression\review\source_understanding_review.html
- Rendered PNGs: D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\ppt-deep-search\ptrurbov2-attention-compression\review\source-understanding-images
- Visual QA: D:\Agent Repo\Mozhi-s-AgentWorkspace\.tmp\ppt-deep-search\ptrurbov2-attention-compression\review\visual-qa.md

## Scope

This baseline explains RTPurbo / RTPurboV2 attention compression from the parsed paper XML package, with particular attention to:

- attention compression object: head-wise retrieval/local split, low-dimensional token indexer, dynamic top-p token selection;
- compression and speed claims: prefill vs decode vs end-to-end口径分开处理；
- accuracy evidence: RULER, ultra-long multi-hop, reasoning benchmarks;
- evidence boundary: paper-backed RTPurbo claims vs external RTPurboV2 release/open-source claims to be separately verified.

## User Preference Captured

Source Understanding must make visual evidence understandable:主视觉材料应配解释，默认一页一个主视觉材料，说明关键字、条件、读图方法和结论边界。

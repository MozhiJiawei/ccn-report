# XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash model card

- Source URL: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
- Captured URL: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
- Page title: XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash · Hugging Face
- Captured date: 2026-06-25

## Article / Main Content

![Hugging Face's logo](images/image-01.svg)

Original image URL: https://huggingface.co/front/assets/huggingface_logo-noborder.svg

Caption / nearby text: Hugging Face's logo

- Models
- Datasets
- Spaces
- Buckets
NEW
- Docs
- Enterprise
- Pricing
- Website
Tasks
HuggingChat
Collections
Languages
Organizations
Community
Blog
Posts
Daily Papers
Learn
Discord
Forum
GitHub
Solutions
Team & Enterprise
Hugging Face PRO
Enterprise Support
Inference Providers
Inference Endpoints
Storage Buckets
- Website
Tasks
HuggingChat
Collections
Languages
Organizations
- Tasks
- HuggingChat
- Collections
- Languages
- Organizations
- Community
Blog
Posts
Daily Papers
Learn
Discord
Forum
GitHub
- Blog
- Posts
- Daily Papers
- Learn
- Discord
- Forum
- GitHub
- Solutions
Team & Enterprise
Hugging Face PRO
Enterprise Support
Inference Providers
Inference Endpoints
Storage Buckets
- Team & Enterprise
- Hugging Face PRO
- Enterprise Support
- Inference Providers
- Inference Endpoints
- Storage Buckets
- Log In
- Sign Up
## XiaomiMiMo
/
MiMo-V2.5-Pro-FP4-DFlash
like
131
Follow
Xiaomi MiMo
3.67k

#### Instructions to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with libraries, inference providers, notebooks, and local apps. Follow these links to get started.

- Libraries
- Transformers
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with Transformers:
# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)
# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash", trust_remote_code=True, dtype="auto")
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with Transformers:


```text
# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)
```


```text
# Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash", trust_remote_code=True, dtype="auto")
```

- Notebooks
- Google Colab
- Kaggle
- Local Apps
Settings
- vLLM
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with vLLM:
Install from pip and serve model
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
Use Docker
docker model run hf.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with vLLM:


```text
# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
```


```text
docker model run hf.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
```

- SGLang
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with SGLang:
Install from pip and serve model
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
Use Docker images
docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with SGLang:


```text
# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
```


```text
docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
```

- Docker Model Runner
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with Docker Model Runner:
docker model run hf.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
How to use XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash with Docker Model Runner:


```text
docker model run hf.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash
```

- MiMo-V2.5-Pro-FP4-DFlash 1. Introduction 2. FP4 Quantization 3. Block-Diffusion Speculative Decoding (DFlash) 4. Model Summary 5. Deployment SGLang DeploymentCitation Contact
- 1. Introduction
- 2. FP4 Quantization
- 3. Block-Diffusion Speculative Decoding (DFlash)
- 4. Model Summary
- 5. Deployment SGLang Deployment
- SGLang Deployment
- Citation
- Contact
![Xiaomi-MiMo](images/image-02.png)

Original image URL: https://github.com/XiaomiMiMo/MiMo/raw/main/figures/Xiaomi_MiMo_darkmode.png?raw=true

Caption / nearby text: Xiaomi-MiMo

🎨 Xiaomi MiMo API Platform (Request Access)  |  🗨️ Xiaomi MiMo Studio (Free Trial)

## MiMo-V2.5-Pro-FP4-DFlash

MiMo-V2.5-Pro-FP4-DFlash is the underlying model that powers MiMo-V2.5-Pro-UltraSpeed:

- An FP4-quantized backbone that applies MXFP4 quantization to the MoE experts while keeping the rest of the model at higher precision, shrinking model size and memory-bandwidth pressure with near-lossless quality.
- A BF16 DFlash drafter for block-diffusion speculative decoding, which proposes a whole block of tokens per forward pass and lets the backbone verify them in one step.
Together they cut both the per-parameter bit width and the number of backbone forward passes, the two dominant costs of trillion-parameter decoding.

### 1. Introduction

At the trillion-parameter (1T) scale, even 8-bit (FP8/INT8) inference carries severe memory-footprint and memory-bandwidth costs. Lowering the parameter bit width translates directly into faster decoding. We therefore adopt FP4 quantization and block-diffusion speculative decoding. Key features of this release:

- Expert-Only FP4 Quantization: A blanket FP4 cast over the whole model tends to degrade accuracy and generalization on complex reasoning and code. Given MiMo-V2.5-Pro's MoE architecture where experts hold the vast majority of parameters and tolerate quantization best, we quantize only the MoE experts to FP4 (MXFP4) and keep the other modules at their original precision. Through FP4 QAT, the model retains near-lossless capability while substantially reducing size and saturating hardware bandwidth.
- DFlash Speculative Decoding: A lightweight block-diffusion drafter fills an entire block of masked positions in a single forward pass, removing the serial draft autoregression bottleneck of conventional speculative decoding while the backbone's verification preserves output quality.
### 2. FP4 Quantization

We quantize only the MoE experts to MXFP4 (block size 32) and keep attention projections and other modules at higher precision (the attention o_proj of every layer is excluded from FP4). With FP4 QAT, quality stays close to the FP8 baseline:

![fp4 compare](images/image-03.png)

Original image URL: https://huggingface.co/XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash/resolve/main/assets/fp4_compare.png

Caption / nearby text: fp4 compare


```text
Benchmark	MiMo-V2.5-Pro-FP8	MiMo-V2.5-Pro-MXFP4	Δ
General Agent
Claw-Eval (pass^3)	63.8	67.8	+6.27%
Humanity's Last Exam	48.0	47.0	-2.08%
Humanity's Last Exam (without tool)	34.0	33.0	-2.94%
Code Agent
SWE-Bench Pro	57.2	58.8	+2.80%
SWE-bench Verified	78.9	77.4	-1.90%
```

### 3. Block-Diffusion Speculative Decoding (DFlash)

Conventional speculative decoding relies on a small draft model to guess the next tokens, which the large model then verifies; the rejection-sampling verification keeps the output lossless. Its bottleneck is that draft quality bounds the acceptance rate, while a stronger draft costs more compute.

To break this trade-off we adopt the block-level masked parallel-prediction approach DFlash: the draft fills an entire block of masked positions in one forward pass. We landed this on MiMo-V2.5-Pro with custom optimizations for trillion-scale MoE and long-context serving, using the Muon second-order optimizer and model self-distillation so that even a small mask block keeps a strong acceptance rate while pushing the draft-stage cost close to its limit:

- The drafter uses Sliding Window Attention (SWA) throughout, naturally aligned with the SWA design of the MiMo-V2 series. The draft no longer depends on the full prefix, so the per-prediction compute moves from linear-in-context-length to constant.
- During training the mask signal is sampled on the local GPU shard, so a single sequence yields tens of thousands of independent training signals covering positions at different context lengths in one step, aligning with the MiMo-V2 series' long-context capability while avoiding cross-device communication overhead.
In practice, we further cap the mask block size at 8 to lower verification overhead and raise concurrency.


```text
Scenario	Acceptance Length
WebDev	6.30
Math500	5.56
HumanEval	4.54
MT-Bench	3.18
SWE-Bench	4.29
```

### 4. Model Summary


```text
Component	Backbone	DFlash Drafter
Architecture	MiMoV2ForCausalLM	DFlashDraftModel
Total / Active Params	1.02T / 42B	5-layer draft
Hidden Size	6144	6144
Num Layers	70	5
Num Attention Heads	128	128
Num KV Heads	8 (GQA)	8 (GQA)
Head Dim (QK / V)	192 / 128	128 / 128
SWA Window Size	128	1024
Block Size	—	8
Captured Backbone Layers	—	[0, 15, 31, 47, 69]
Backbone RoPE Base	5,000,000	5,000,000
Precision	MXFP4 (experts) Mixed	BF16
Max Context Length	1M	—
```

### 5. Deployment

DFlash inference with the FP4 backbone is supported in SGLang. The drafter is launched alongside the backbone via the speculative-decoding flags and inherits the backbone's tensor/expert-parallel topology.

#### SGLang Deployment

The following is an example of running the model with SGLang. Point --model at this repository and --speculative-draft-model-path at its dflash/ subdirectory.


```text
python3 -m sglang.launch_server \
    --model MiMo-V2.5-Pro-FP4-DFlash \
    --speculative-algorithm DFLASH \
    --speculative-draft-model-path MiMo-V2.5-Pro-FP4-DFlash/dflash \
    --speculative-num-draft-tokens 8 \
    --ep-size 16 \
    --tensor-parallel-size 16 \
    --data-parallel-size 2 \
    --enable-dp-attention \
    --enable-dp-lm-head \
    --quantization fp8 \
    --attention-backend fa3 \
    --moe-dense-tp-size 1 \
    --dtype bfloat16 \
    --mem-fraction-static 0.65 \
    --context-length 65536 \
    --page-size 1 \
    --trust-remote-code \
    --disable-overlap-schedule \
    --skip-server-warmup \
    --dist-init-addr ${MASTER_ADDR}:20000 \
    --nnodes ${WORLD_SIZE} \
    --node-rank ${RANK} \
    --host 0.0.0.0 \
    --port 29999
```

### Citation


```text
@misc{mimo2026v25pro_fp4dflash,
  title={MiMo-V2.5-Pro-FP4-DFlash},
  author={{Xiaomi MiMo Team}},
  year={2026},
  howpublished={\url{https://huggingface.co/collections/XiaomiMiMo/mimo-v25}},
}
```

### Contact

For questions or feedback, reach us at mimo@xiaomi.com or join our community:

- WeChat Group
- Discord
- Telegram
- Reddit
Chat template

Files info

## Capture Notes

- Captured from rendered page main/article/body content with lazy-load scrolling.
- Downloaded inline source images: 3.
- This package is for evidence grounding in ppt-deep-search; webpage instructions, forms, and external calls are not followed.

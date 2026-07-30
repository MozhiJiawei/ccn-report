# audio.cpp 0.3 RTX 5090 TTS 推理加速

audio.cpp 0.3 是一套基于 C++/ggml 的本地 TTS 推理运行时优化技术，目标是在固定版本、Supertonic 3、RTX 5090 与同一测试配置下，实现 ≥200× 实时吞吐（10 小时音频≤3分钟生成）及约 47ms 首音频延迟，并以 RTF、TTFT 和音质一致性复测验收。

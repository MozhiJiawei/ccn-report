# CANN Bench Source Understanding

截至 2026 年 7 月论文版本，CANN Bench 是一套面向华为昇腾 910B2、用于评估 AI 生成 CANN 算子内核的可复现基准：以 53 个算子和 1060 个公开测试用例覆盖 L1–L4 难度及 FP16、BF16、FP32、INT8 路径，并按编译 20%、正确性 30%、性能 50% 计分，以 HAP 硬件极限和隐藏用例协议约束性能可比性与刷分风险。

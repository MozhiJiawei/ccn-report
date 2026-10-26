# ACPs-可信互联

## 一句话总结

截至2026年10月21日固定提交，北邮牵头的ACPs以v02.02规范和Python SDK 2.2.0将可信注册、能力发现及直连/群组交互接成异构智能体协作链，为跨平台接入提供参考实现，但尚无本次来源支持的量化性能或全面标准符合认证结论。

## 任务信息

- 序号：257
- 任务编号：TASK-20261021221712-cceaff24
- 热点编号：HS-20261021-article1792592233555758
- 周期：2026-W43
- 指定分类：由 AI 自动分类
- 实际归档分类：02-智能体平台、协议与执行系统/协议与互操作
- 归类依据：输入category=null，已加载02与11细则；正文主贡献为ATR注册、ADP发现及AIP交互的Agent互操作机制与参考实现，故归02/协议与互操作；GB/Z185标准发布与TC28会议为证据背景，11仅次关联，无指定值差异。
- 任务正文：北邮ACPs协议族推进智能体互联，国标GB/Z 185-2026形成参考实现技术线索
- 任务来源：[原始任务来源](http://mp.weixin.qq.com/s?__biz=MzA3NDc1NDI3MQ==&mid=2652541560&idx=1&sn=919d728aed3c52810dfd4712c1bdab72&chksm=8594b3719ea16013c8de81145282b56302afcde6dd08a38f7c05da005c01554b85c1945741c6&scene=0&xtrack=1#rd)

## 交付件说明

- [ACPs-可信互联.html](./ACPs-可信互联.html)：dependency-free SingleFile Source Understanding HTML，可离线打开。
- [ACPs-可信互联.pptx](./ACPs-可信互联.pptx)：可编辑的一页式技术洞察 PPTX。

## 引用信息源说明

- [ACPs官方固定版本中文README](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/readme_cn.md)：支撑项目定位、SDK2.2.0与实现入口、版本和许可。
- [ATR v02.02](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-specs/04-ACPs-spec-ATR/ACPs-spec-ATR.md)：支撑EAB账户绑定、可信注册、实体身份派生与证书流程。
- [ADP v02.02](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-specs/06-ACPs-spec-ADP/ACPs-spec-ADP.md)：支撑能力发现模式、候选选择及发现接口。
- [AIP v02.02](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-specs/07-ACPs-spec-AIP/ACPs-spec-AIP.md)：支撑会话、直连/群组及条件身份绑定。
- [ACPs基础设施说明](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-infra/README.md)：支撑部署组件、Compose和host模式及运行依赖。
- [ACPs SDK元数据](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-sdk/pyproject.toml)：支撑Python范围、版本和依赖。
- [ACPs官方总览](https://github.com/AIP-PUB/ACPs-community/blob/d7a0a5cd3c4b1cf99d064dd3e88e41df1d308886/acps-specs/01-ACPs-spec-overview/ACPs-spec-overview.md)：支撑实体关系原图、协议族概念与原图上下文。
- [GB/Z185.1-2026《总体架构》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=CFF03D872963466AC7F03ED0E28B6702)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.2-2026《身份码》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=11B33B7532093ED660305B2BF4940A12)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.3-2026《身份管理》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=BFCCE65447B30927953D90059AB89E23)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.4-2026《智能体描述》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=348CD9F4C2C07D1BE6902D94A7CA5DC5)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.5-2026《智能体发现》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=D668764F4B1AAFCC4E731E9D7C2597F2)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.6-2026《智能体交互》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=52231E3A8CED414AD7604D7B70C63198)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [GB/Z185.7-2026《智能体工具调用》官方详情](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=BD79A8E88A70EBAEAC179367A0F8778E)：核准准确编号、标题、2026-05-22发布及现行状态；未展示实施日期。
- [TC28标准应用推进专题会议](https://nits.org.cn/tc28/hydt/202607/0958b17c91d1405d99839f13d3300f8c.shtml)：支撑7月会议、AIP V2.1发布与跨域协作展示的历史背景。

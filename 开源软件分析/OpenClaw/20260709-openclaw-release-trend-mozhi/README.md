# OpenClaw Release Trend Report

- 报告对象：OpenClaw 2026 年 1-7 月 release 趋势分析
- 归档版本：v2
- 归档日期：2026-07-13
- 归档人：mozhi
- 报告形态：SingleFile HTML 多文件报告

## 入口

- [汇总报告](summary/index.html)
- [易用性趋势](usability/index.html)
- [Agent 能力趋势](agent-capability/index.html)
- [插件与生态趋势](plugin-ecosystem/index.html)
- [DFX 趋势](dfx/index.html)

## 说明

本版替换旧归档版本。四篇子报告均以技术机制解释图呈现趋势，并保留全量 ReleaseNote 中文翻译证据折叠区。
本目录仅保留最终 SingleFile HTML 与本 README；过程文件、截图、视觉 QA、manifest 和源数据保留在工作区 `.tmp/`。

## 分类后的原始 Release

- 总条目数：625
- 易用性：179
- Agent 能力：205
- 插件与生态：86
- DFX：155

以下为分类后的原始 ReleaseNote 条目，保留英文原始变更说明，并附一级/二级分类。

### 二级分类统计

| 一级分类 | 二级分类 | 条目数 |
| --- | --- | ---: |
| 易用性 | Control UI/WebChat/桌面与移动端体验 | 65 |
| 易用性 | 渠道与消息平台 | 114 |
| Agent能力 | Agent 运行时与任务编排 | 66 |
| Agent能力 | 模型与 Provider | 97 |
| Agent能力 | 记忆/上下文与转录 | 42 |
| 插件与生态 | 多媒体与生成工具 | 16 |
| 插件与生态 | 插件化与生态 | 48 |
| 插件与生态 | 语音/Talk/Realtime 与会议 | 22 |
| DFX | CLI/配置/运维与部署 | 30 |
| DFX | Gateway/Node/远程连接 | 17 |
| DFX | 安全/权限与信任边界 | 70 |
| DFX | 性能/可靠性与可观测性 | 38 |

### 易用性

| ID | 时间 | Release | 二级分类 | 原始变更说明 |
| --- | --- | --- | --- | --- |
| 2026-01-050 | 2026-01-21 | clawdbot 2026.1.21 | Control UI/WebChat/桌面与移动端体验 | Added custom assistant identity, avatars, and per-session identity display in Control UI. |
| 2026-01-053 | 2026-01-21 | clawdbot 2026.1.21 | 渠道与消息平台 | Added Signal typing indicators/read receipts and MSTeams file uploads, adaptive cards, and attachment handling. |
| 2026-01-056 | 2026-01-21 | clawdbot 2026.1.21 | 渠道与消息平台 | Added explicit heartbeat session keys, active hours, per-channel idle durations, and per-channel auto-reply debounce overrides. |
| 2026-01-058 | 2026-01-21 | clawdbot 2026.1.21 | 渠道与消息平台 | Added Discord wildcard channel configuration. |
| 2026-01-046 | 2026-01-22 | clawdbot 2026.1.22 | 渠道与消息平台 | Added Slack chat-type reply-threading overrides. |
| 2026-01-048 | 2026-01-22 | clawdbot 2026.1.22 | Control UI/WebChat/桌面与移动端体验 | Improved onboarding with TUI/Web/Later hatch choice, token explainer, macOS dashboard seed, and showcase link. |
| 2026-01-035 | 2026-01-23 | Clawdbot 2026.1.23 | 渠道与消息平台 | Added per-channel heartbeat visibility controls. |
| 2026-01-037 | 2026-01-23 | Clawdbot 2026.1.23 | 渠道与消息平台 | Added the Tlon/Urbit channel plugin for DMs, group mentions, and thread replies. |
| 2026-01-043 | 2026-01-23 | Clawdbot 2026.1.23 | 渠道与消息平台 | Added per-channel Markdown table conversion for messaging surfaces. |
| 2026-01-025 | 2026-01-24 | Clawdbot 2026.1.24 | 渠道与消息平台 | Added LINE Messaging API plugin support with rich replies and quick replies. |
| 2026-01-028 | 2026-01-24 | Clawdbot 2026.1.24 | 渠道与消息平台 | Added Telegram DM topics as separate sessions and an outbound link-preview toggle. |
| 2026-01-030 | 2026-01-24 | Clawdbot 2026.1.24 | Control UI/WebChat/桌面与移动端体验 | Refreshed the Control UI dashboard design system. |
| 2026-01-020 | 2026-01-28 | Introducing OpenClaw | 渠道与消息平台 | Added Twitch and Google Chat plugins. |
| 2026-01-022 | 2026-01-28 | Introducing OpenClaw | Control UI/WebChat/桌面与移动端体验 | Added image sending in Web Chat. |
| 2026-01-012 | 2026-01-29 | openclaw 2026.1.29 | 渠道与消息平台 | Expanded Telegram capabilities with captions, media/buttons payloads, silent sends, message edits, quote replies, stickers, vision handling, and topic-aware notifications. |
| 2026-01-013 | 2026-01-29 | openclaw 2026.1.29 | 渠道与消息平台 | Expanded channel/platform support across Discord privileged intents, Matrix SDK migration, Slack streamed-reply cleanup, and Tlon thread reply IDs. |
| 2026-01-014 | 2026-01-29 | openclaw 2026.1.29 | 渠道与消息平台 | Added per-account DM session scoping and multi-account isolation for routing. |
| 2026-01-016 | 2026-01-29 | openclaw 2026.1.29 | Control UI/WebChat/桌面与移动端体验 | Added OpenClaw macOS/app branding migrations and reduced debug-only PATH hijacking risk. |
| 2026-01-018 | 2026-01-29 | openclaw 2026.1.29 | Control UI/WebChat/桌面与移动端体验 | Improved WebChat image paste previews and image-only sends. |
| 2026-01-005 | 2026-01-30 | openclaw 2026.1.30 | Control UI/WebChat/桌面与移动端体验 | Refreshed Web UI session handling after chat commands and improved session display names. |
| 2026-02-059 | 2026-02-01 | openclaw 2026.2.1 | 渠道与消息平台 | Telegram uses the shared pairing store. |
| 2026-02-063 | 2026-02-01 | openclaw 2026.2.1 | 渠道与消息平台 | Discord inherits thread parent bindings for routing. |
| 2026-02-066 | 2026-02-01 | openclaw 2026.2.1 | Control UI/WebChat/桌面与移动端体验 | Web UI refines chat layout and extends session active duration. |
| 2026-02-053 | 2026-02-03 | openclaw 2026.2.2 | 渠道与消息平台 | Feishu/Lark plugin support and docs open a new channel integration path. |
| 2026-02-054 | 2026-02-03 | openclaw 2026.2.2 | Control UI/WebChat/桌面与移动端体验 | Web UI adds an Agents dashboard for managing agent files, tools, skills, models, channels, and cron jobs. |
| 2026-02-049 | 2026-02-04 | openclaw 2026.2.3 | 渠道与消息平台 | Messages add per-channel and per-account responsePrefix overrides across channels. |
| 2026-02-043 | 2026-02-06 | openclaw 2026.2.6 | Control UI/WebChat/桌面与移动端体验 | Web UI adds a token usage dashboard. |
| 2026-02-035 | 2026-02-08 | openclaw 2026.2.9 | Control UI/WebChat/桌面与移动端体验 | Gateway adds agent management RPC methods for the Web UI, including create, update, and delete. |
| 2026-02-036 | 2026-02-08 | openclaw 2026.2.9 | Control UI/WebChat/桌面与移动端体验 | Web UI chat history shows a Compaction divider. |
| 2026-02-038 | 2026-02-08 | openclaw 2026.2.9 | 渠道与消息平台 | Routing reloads bindings per message so binding changes apply without restart. |
| 2026-02-039 | 2026-02-08 | openclaw 2026.2.9 | 渠道与消息平台 | Discord adds forum and media thread-create starter message support. |
| 2026-02-030 | 2026-02-12 | openclaw 2026.2.12 | 渠道与消息平台 | Telegram renders blockquotes as native tags instead of stripping them. |
| 2026-02-024 | 2026-02-13 | openclaw 2026.2.13 | 渠道与消息平台 | Discord adds configurable presence status, activity, type, and URL. |
| 2026-02-019 | 2026-02-14 | openclaw 2026.2.14 | 渠道与消息平台 | Telegram adds poll sending through openclaw message poll, including duration, silent delivery, and anonymity controls. |
| 2026-02-020 | 2026-02-14 | openclaw 2026.2.14 | 渠道与消息平台 | Discord exec approval prompts can target channels or both DM and channel via configuration. |
| 2026-02-013 | 2026-02-15 | openclaw 2026.2.15 | 渠道与消息平台 | Discord gains rich interactive agent prompts with Components v2, including buttons, selects, modals, and attachment-backed file blocks. |
| 2026-02-014 | 2026-02-15 | openclaw 2026.2.15 | 渠道与消息平台 | Discord Components v2 also improves embeds passthrough and exec approval UX. |
| 2026-02-017 | 2026-02-15 | openclaw 2026.2.15 | 渠道与消息平台 | Slack, Discord, and Telegram support per-channel and per-account ack reaction overrides for platform-specific emoji formats. |
| 2026-02-012 | 2026-02-26 | openclaw 2026.2.26 | 渠道与消息平台 | Messaging and channel workflows improve with Feishu message metadata and doc-tool account routing, Telegram group inline-button handling, LINE directive authorization, and inherited DM allowlist validation across account-capable channels. |
| 2026-03-167 | 2026-03-01 | openclaw 2026.3.1 | 渠道与消息平台 | Added Telegram per-DM direct/topic configuration with topic-aware routing, authorization, debounce, callbacks, commands, and reactions. |
| 2026-03-168 | 2026-03-01 | openclaw 2026.3.1 | Control UI/WebChat/桌面与移动端体验 | Added live Android capability refresh wiring and node canvas capability refresh support. |
| 2026-03-170 | 2026-03-01 | openclaw 2026.3.1 | 渠道与消息平台 | Added Feishu chat info/member query tool actions and optional owner permission grants on Feishu doc creation. |
| 2026-03-171 | 2026-03-01 | openclaw 2026.3.1 | Control UI/WebChat/桌面与移动端体验 | Added German locale support in the Web UI. |
| 2026-03-179 | 2026-03-01 | openclaw 2026.3.1 | 渠道与消息平台 | Added Discord thread idle/max-age lifecycle controls and commands. |
| 2026-03-182 | 2026-03-01 | openclaw 2026.3.1 | 渠道与消息平台 | Added Feishu Docx table creation, table writing, file/image uploads, and reaction-event handling. |
| 2026-03-150 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Added shared sendPayload support across direct-text-media, Discord, Slack, WhatsApp, Zalo, and Zalouser. |
| 2026-03-153 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Defaulted Telegram streaming to partial for new setups and added DM draft streaming with separate reasoning and answer lanes. |
| 2026-03-154 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Added Telegram voice-note mention preflight gating controls. |
| 2026-03-158 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Rebuilt Zalo Personal plugin runtime around native in-process zca-js integration. |
| 2026-03-159 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Exposed channelRuntime for external channel plugins. |
| 2026-03-163 | 2026-03-02 | openclaw 2026.3.2 | 渠道与消息平台 | Changed new-install onboarding defaults to messaging tools profile, ACP dispatch default-on, explicit plugin HTTP route registration, and JS-native Zalo Personal runtime. |
| 2026-03-129 | 2026-03-07 | openclaw 2026.3.7 | 渠道与消息平台 | Added durable Discord channel and Telegram topic ACP binding storage with routing resolution and CLI/docs support. |
| 2026-03-130 | 2026-03-07 | openclaw 2026.3.7 | 渠道与消息平台 | Added Telegram ACP topic binding support, topic-thread follow-ups, approval buttons, and pinned in-topic bind confirmations. |
| 2026-03-131 | 2026-03-07 | openclaw 2026.3.7 | 渠道与消息平台 | Added per-topic Telegram agent routing for forum groups and DM topics. |
| 2026-03-132 | 2026-03-07 | openclaw 2026.3.7 | Control UI/WebChat/桌面与移动端体验 | Added Spanish locale support in the Control UI. |
| 2026-03-141 | 2026-03-07 | openclaw 2026.3.7 | 渠道与消息平台 | Added Slack DM typing reactions and Discord bot mention gating. |
| 2026-03-144 | 2026-03-07 | openclaw 2026.3.7 | Control UI/WebChat/桌面与移动端体验 | Prepared iOS App Store Connect release metadata, bundle IDs, Watch icons, screenshots, and Keychain-backed ASC auth. |
| 2026-03-111 | 2026-03-08 | openclaw 2026.3.8 | Control UI/WebChat/桌面与移动端体验 | Made the TUI infer the active agent from the current workspace. |
| 2026-03-116 | 2026-03-08 | openclaw 2026.3.8 | Control UI/WebChat/桌面与移动端体验 | Removed Android Play distribution-sensitive capabilities including self-update, background location, screen recording, and background microphone capture. |
| 2026-03-118 | 2026-03-08 | openclaw 2026.3.8 | Control UI/WebChat/桌面与移动端体验 | Added light-terminal theme detection for the TUI with OPENCLAW_THEME override. |
| 2026-03-100 | 2026-03-11 | openclaw 2026.3.11 | Control UI/WebChat/桌面与移动端体验 | Added iOS home canvas welcome screen, live agent overview refresh, docked toolbar, and main-session chat routing. |
| 2026-03-101 | 2026-03-11 | openclaw 2026.3.11 | Control UI/WebChat/桌面与移动端体验 | Added macOS chat model picker and persisted thinking-level selections. |
| 2026-03-107 | 2026-03-11 | openclaw 2026.3.11 | 渠道与消息平台 | Added Discord auto-created thread archive-duration configuration. |
| 2026-03-092 | 2026-03-12 | openclaw 2026.3.12 | Control UI/WebChat/桌面与移动端体验 | Refreshed the Control UI dashboard with modular overview, chat, config, agent, and session views plus command palette, mobile tabs, slash commands, search, export, and pinned messages. |
| 2026-03-098 | 2026-03-12 | openclaw 2026.3.12 | 渠道与消息平台 | Added Slack Block Kit reply delivery through shared agent reply handling. |
| 2026-03-086 | 2026-03-13 | openclaw 2026.3.13 | Control UI/WebChat/桌面与移动端体验 | Redesigned Android chat settings with grouped device/media sections and denser Connect, Voice, composer, and session-header layouts. |
| 2026-03-087 | 2026-03-13 | openclaw 2026.3.13 | Control UI/WebChat/桌面与移动端体验 | Added iOS first-run welcome pager before gateway setup and clearer /pair qr onboarding instructions. |
| 2026-03-073 | 2026-03-22 | openclaw 2026.3.22 | Control UI/WebChat/桌面与移动端体验 | Added Control UI chat expand-to-canvas and in-app session navigation from Sessions and Cron views. |
| 2026-03-074 | 2026-03-22 | openclaw 2026.3.22 | Control UI/WebChat/桌面与移动端体验 | Added Control UI appearance roundness controls and usage view improvements. |
| 2026-03-075 | 2026-03-22 | openclaw 2026.3.22 | Control UI/WebChat/桌面与移动端体验 | Added Android system-aware dark theme across onboarding, chat, and voice flows. |
| 2026-03-077 | 2026-03-22 | openclaw 2026.3.22 | Control UI/WebChat/桌面与移动端体验 | Added Android node callLog.search and sms.search capabilities. |
| 2026-03-078 | 2026-03-22 | openclaw 2026.3.22 | 渠道与消息平台 | Added Telegram DM forum auto-topic labeling and topic-edit actions. |
| 2026-03-079 | 2026-03-22 | openclaw 2026.3.22 | 渠道与消息平台 | Added Feishu current-conversation ACP/subagent binding, reasoning streaming cards, and identity-aware reply cards. |
| 2026-03-080 | 2026-03-22 | openclaw 2026.3.22 | 渠道与消息平台 | Added Matrix room policies for bot-to-bot conversations and private/internal homeserver opt-in. |
| 2026-03-054 | 2026-03-23 | 2026.3.23 | Control UI/WebChat/桌面与移动端体验 | Expanded Qwen endpoint support, refreshed Control UI clarity and accessibility, and strengthened CSP/auth handling across plugin, browser, gateway, and model workflows. |
| 2026-03-052 | 2026-03-24 | openclaw 2026.3.24 | 渠道与消息平台 | Broadened Gateway and OpenAI compatibility, refreshed Control UI and skills management, and expanded messaging capabilities across Teams, Slack, Discord, Telegram, WhatsApp, Feishu, and ACP. |
| 2026-03-040 | 2026-03-28 | openclaw 2026.3.28 | 渠道与消息平台 | Added current-conversation ACP binds for Discord, BlueBubbles, and iMessage. |
| 2026-03-045 | 2026-03-28 | openclaw 2026.3.28 | 渠道与消息平台 | Added explicit Slack upload-file action support. |
| 2026-03-046 | 2026-03-28 | openclaw 2026.3.28 | 渠道与消息平台 | Added canonical upload-file support for Microsoft Teams, Google Chat, and BlueBubbles file sends. |
| 2026-03-047 | 2026-03-28 | openclaw 2026.3.28 | 渠道与消息平台 | Added native Matrix voice bubbles for auto-TTS replies. |
| 2026-03-015 | 2026-03-30 | openclaw 2026.3.31 | Control UI/WebChat/桌面与移动端体验 | Added Android notification-forwarding controls with package filters, quiet hours, rate limits, and safer picker behavior. |
| 2026-03-018 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added QQ Bot as a bundled channel plugin with multi-account setup, SecretRef-aware credentials, slash commands, reminders, and media send/receive. |
| 2026-03-019 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added LINE image, video, and audio outbound sends on the LINE-specific delivery path. |
| 2026-03-020 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added Matrix HTTP(S) proxy configuration with account-level overrides. |
| 2026-03-021 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added Matrix draft streaming so partial replies update the same message in place. |
| 2026-03-022 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added Matrix per-DM threadReplies overrides and thread-session isolation aligned to effective room or DM policy. |
| 2026-03-025 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added a Microsoft Teams Graph-backed member info action. |
| 2026-03-029 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added native Slack exec-approval routing and approver authorization. |
| 2026-03-031 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added WhatsApp reaction support for agent replies. |
| 2026-03-035 | 2026-03-30 | openclaw 2026.3.31 | 渠道与消息平台 | Added optional Matrix room-history context for group triggers. |
| 2026-03-005 | 2026-03-31 | openclaw 2026.4.1 | 渠道与消息平台 | Added Feishu Drive comment-event workflows with thread context resolution, in-thread replies, and feishu_drive comment actions. |
| 2026-03-011 | 2026-03-31 | openclaw 2026.4.1 | 渠道与消息平台 | Added configurable Telegram delivery error policies and cooldowns. |
| 2026-04-124 | 2026-04-01 | openclaw 2026.4.2 | Control UI/WebChat/桌面与移动端体验 | Android added assistant-role entrypoints and Google Assistant App Actions metadata to launch OpenClaw and hand prompts into chat composer. |
| 2026-04-128 | 2026-04-01 | openclaw 2026.4.2 | 渠道与消息平台 | Channel session routing moved provider-specific conversation grammar into plugin-owned session-key surfaces. |
| 2026-04-129 | 2026-04-01 | openclaw 2026.4.2 | 渠道与消息平台 | Feishu added Drive comment-event workflows with comment-thread context resolution, in-thread replies, and document comment actions. |
| 2026-04-130 | 2026-04-01 | openclaw 2026.4.2 | 渠道与消息平台 | Matrix emits spec-compliant `m.mentions` metadata across sends, captions, edits, polls, and action-driven edits. |
| 2026-04-114 | 2026-04-05 | openclaw 2026.4.5 | Control UI/WebChat/桌面与移动端体验 | Control UI localization expanded to Simplified Chinese, Traditional Chinese, Brazilian Portuguese, German, Spanish, Japanese, Korean, French, Turkish, Indonesian, Polish, and Ukrainian. |
| 2026-04-116 | 2026-04-05 | openclaw 2026.4.5 | 渠道与消息平台 | iOS and Matrix gained native exec approval flows through APNs/in-app modals and Matrix-native account-scoped prompts. |
| 2026-04-117 | 2026-04-05 | openclaw 2026.4.5 | 渠道与消息平台 | Channels gained configurable `contextVisibility` filtering for supplemental quote/thread/history context. |
| 2026-04-110 | 2026-04-07 | openclaw 2026.4.7 | 渠道与消息平台 | Discord event creation can accept cover image URLs or local files and pass validated image payloads through admin/runtime paths. |
| 2026-04-099 | 2026-04-08 | openclaw 2026.4.9 | Control UI/WebChat/桌面与移动端体验 | Control UI added a structured diary view with timeline navigation, backfill/reset controls, traceable dreaming summaries, a grounded Scene lane, and safe clear-grounded actions. |
| 2026-04-102 | 2026-04-08 | openclaw 2026.4.9 | Control UI/WebChat/桌面与移动端体验 | iOS release versioning moved to explicit CalVer pinning with a documented `pnpm ios:version:pin -- --from-gateway` workflow. |
| 2026-04-088 | 2026-04-11 | openclaw 2026.4.11 | Control UI/WebChat/桌面与移动端体验 | Control UI webchat renders assistant media, reply, and voice directives as structured chat bubbles, with an `[embed ...]` rich output tag gated for external URLs. |
| 2026-04-090 | 2026-04-11 | openclaw 2026.4.11 | 渠道与消息平台 | Feishu document comment sessions gained richer context parsing, comment reactions, and typing feedback. |
| 2026-04-091 | 2026-04-11 | openclaw 2026.4.11 | 渠道与消息平台 | Microsoft Teams gained reaction support, reaction listing, Graph pagination, delegated OAuth setup, and message actions for pin/unpin/read/react. |
| 2026-04-083 | 2026-04-12 | openclaw 2026.4.12 | 渠道与消息平台 | Matrix partial streaming added MSC4357 live markers for draft preview sends/edits. |
| 2026-04-077 | 2026-04-13 | openclaw 2026.4.14 | 渠道与消息平台 | Telegram forum topics now surface human topic names in agent context, prompt metadata, and plugin hook metadata. |
| 2026-04-071 | 2026-04-15 | openclaw 2026.4.15 | Control UI/WebChat/桌面与移动端体验 | Control UI Overview added a Model Auth status card for OAuth token health and provider rate-limit pressure. |
| 2026-04-066 | 2026-04-20 | openclaw 2026.4.20 | 渠道与消息平台 | BlueBubbles group chats gained per-group systemPrompt injection into inbound context. |
| 2026-04-068 | 2026-04-20 | openclaw 2026.4.20 | 渠道与消息平台 | Mattermost can stream thinking, tool activity, and partial reply text into a single draft preview post. |
| 2026-04-050 | 2026-04-22 | openclaw 2026.4.22 | Control UI/WebChat/桌面与移动端体验 | TUI added local embedded mode for terminal chats without a Gateway while preserving plugin approval gates. |
| 2026-04-054 | 2026-04-22 | openclaw 2026.4.22 | 渠道与消息平台 | WhatsApp gained native reply quoting and per-group/per-direct system prompt injection. |
| 2026-04-055 | 2026-04-22 | openclaw 2026.4.22 | Control UI/WebChat/桌面与移动端体验 | Sessions listing added mailbox-style filters for label, agent, search, title, and last-message previews. |
| 2026-04-056 | 2026-04-22 | openclaw 2026.4.22 | Control UI/WebChat/桌面与移动端体验 | Control UI added browser-local operator identity with shared avatar rendering and tighter quick settings/chat layouts. |
| 2026-04-038 | 2026-04-24 | openclaw 2026.4.24 | Control UI/WebChat/桌面与移动端体验 | Control UI refined agent Tool Access with compact live-tool chips, collapsible groups, direct per-tool toggles, and clearer runtime/source provenance. |
| 2026-04-039 | 2026-04-24 | openclaw 2026.4.24 | 渠道与消息平台 | Matrix added full cross-signing identity trust requirements for self-device verification plus `openclaw matrix verify self`. |
| 2026-04-029 | 2026-04-26 | OpenClaw 2026.4.25 | Control UI/WebChat/桌面与移动端体验 | Control UI added PWA install support and Web Push notifications for Gateway chat. |
| 2026-04-030 | 2026-04-26 | OpenClaw 2026.4.25 | 渠道与消息平台 | Discord voice responses can use a channel-specific LLM while keeping STT/TTS on existing media settings. |
| 2026-04-031 | 2026-04-26 | OpenClaw 2026.4.25 | Control UI/WebChat/桌面与移动端体验 | The first-run CLI/TUI experience gained a setup helper, local planner fallback, full-TUI interactive Crestodian, startup progress indicators, context mode selector, and shorter startup greeting. |
| 2026-04-023 | 2026-04-27 | OpenClaw 2026.4.26 | Control UI/WebChat/桌面与移动端体验 | Control UI added a raw config pending-changes diff panel with JSON5 parsing and sensitive-value redaction. |
| 2026-04-012 | 2026-04-28 | openclaw 2026.4.27 | 渠道与消息平台 | Tencent Yuanbao and QQBot support expanded channel coverage, including QQBot group chat, streaming, media upload, activation modes, and refactored outbound pipelines. |
| 2026-04-013 | 2026-04-28 | openclaw 2026.4.27 | Control UI/WebChat/桌面与移动端体验 | Chat send can stage non-image attachments as agent-readable media paths instead of silently dropping unsupported files. |
| 2026-04-016 | 2026-04-28 | openclaw 2026.4.27 | 渠道与消息平台 | Matrix approval messages gained versioned structured approval metadata for richer capable-client rendering. |
| 2026-04-002 | 2026-04-29 | openclaw 2026.4.29 | 渠道与消息平台 | Messaging and automation gained default active-run steering, visible-reply enforcement, spawned subagent routing metadata, and opt-in follow-up commitments delivered through heartbeat reminders. |
| 2026-04-008 | 2026-04-29 | openclaw 2026.4.29 | Control UI/WebChat/桌面与移动端体验 | Control UI and docs localization expanded with Persian, Dutch, Vietnamese, Italian, Arabic, Thai, and zh-TW related locale/glossary coverage. |
| 2026-04-009 | 2026-04-29 | openclaw 2026.4.29 | 渠道与消息平台 | Tencent Yuanbao gained official channel catalog/docs entries and a plugin alias. |
| 2026-05-076 | 2026-05-02 | openclaw 2026.5.2 | 渠道与消息平台 | Discord channel authorization gained reusable message-channel access groups and channel-audience DM authorization. |
| 2026-05-080 | 2026-05-02 | openclaw 2026.5.2 | Control UI/WebChat/桌面与移动端体验 | Control UI Usage added UTC quarter-hour token buckets for Usage Mosaic filtering. |
| 2026-05-067 | 2026-05-03 | OpenClaw 2026.5.3 | 渠道与消息平台 | Discord, WhatsApp Channel/Newsletter targets, Telegram, Feishu, Matrix, Microsoft Teams, Slack, and degraded transport reporting gained broader channel delivery and recovery behavior. |
| 2026-05-060 | 2026-05-04 | openclaw 2026.5.4 | Control UI/WebChat/桌面与移动端体验 | Control UI added dashboard breadcrumb agent names, a collapsible Cron New Job sidebar, debug logging for long animation/task entries, compact duplicate chat messages, and richer progress draft controls. |
| 2026-05-061 | 2026-05-04 | openclaw 2026.5.4 | 渠道与消息平台 | Slack and channel streaming added richer structured progress drafts, progress line trimming, compact explain-mode summaries, and raw detail overrides for debugging. |
| 2026-05-055 | 2026-05-05 | openclaw 2026.5.5 | 渠道与消息平台 | Session routing, chat and reasoning visibility, plugin/update handling, and provider compatibility improved across Discord, Slack, Telegram, WhatsApp, and Gateway workflows. |
| 2026-05-052 | 2026-05-08 | openclaw 2026.5.9-beta.1 | 渠道与消息平台 | Agent, CLI, voice, plugin, and channel workflows added new chat command defaults, richer model catalog and provider support, stronger logging/redaction, and improved Discord and Telegram voice handling. |
| 2026-05-051 | 2026-05-09 | openclaw 2026.5.10-beta.2 | 渠道与消息平台 | Telegram, Discord voice, Gateway, models, CLI, and agents gained live PR evidence automation, richer voice diagnostics, safer installs, better onboarding, and broader provider compatibility. |
| 2026-05-048 | 2026-05-13 | openclaw 2026.5.14-beta.1 | 渠道与消息平台 | Codex, Gateway, channels, and Control UI received broad platform upgrades with cleaner dependencies, richer status reactions, stronger release validation, and better voice and Telegram support. |
| 2026-05-043 | 2026-05-19 | openclaw 2026.5.19 | 渠道与消息平台 | New skills and plugin tooling landed alongside faster Gateway restarts, improved Browser and CLI workflows, refreshed Mac app Settings, expanded mobile and chat features, and stronger Telegram, Discord, memory, and agent behavior. |
| 2026-05-038 | 2026-05-22 | openclaw 2026.5.22-beta.1 | Control UI/WebChat/桌面与移动端体验 | Onboarding, chat, session UI, plugin workflows, SDK support, diagnostics, Gateway warmups, and desktop/mobile setup flows were broadened into a more complete platform experience. |
| 2026-05-023 | 2026-05-27 | openclaw 2026.5.27 | 渠道与消息平台 | Channel delivery improved across Telegram durable outbound sends, iMessage native exec approval prompts, Slack final replies, Matrix mention previews, QQBot fallback approvals, Discord requester checks, and Google Chat DM behavior. |
| 2026-05-027 | 2026-05-27 | openclaw 2026.5.26 | 渠道与消息平台 | Telegram, iMessage, WhatsApp, Discord, Signal, and mobile approval flows gained stronger production behavior, including forum topic context, attachment roots, remote media staging, voice playback, model picking, and reaction approvals. |
| 2026-05-032 | 2026-05-27 | openclaw 2026.5.26 | Control UI/WebChat/桌面与移动端体验 | TUI/status can queue prompts while an agent is busy and shows explicit fast-mode and systemd Gateway hygiene state. |
| 2026-05-014 | 2026-05-28 | openclaw 2026.5.28-beta.4 | Control UI/WebChat/桌面与移动端体验 | The iOS dev app added Pro Command, Chat, Agents, Settings, hosted push relay defaults, and realtime Talk playback wired to gateway sessions and diagnostics. |
| 2026-05-001 | 2026-05-31 | openclaw 2026.5.31-beta.4 | 渠道与消息平台 | Channels and mobile delivery became steadier across Telegram, WhatsApp, iMessage, Slack, Discord, Microsoft Teams, Google Chat, Google Meet, and iOS realtime Talk. |
| 2026-05-003 | 2026-05-31 | openclaw 2026.5.31-beta.4 | Control UI/WebChat/桌面与移动端体验 | Skill Workshop gained a fuller Control UI flow for proposal lists, today actions, revision handoff, searchable file previews, review states, localization, reusable session routing, guarded apply/reject/quarantine actions, support files, rollback metadata, and in-place proposal revisions. |
| 2026-05-008 | 2026-05-31 | openclaw 2026.5.31-beta.4 | Control UI/WebChat/桌面与移动端体验 | Chat and Control UI startup paths preserve sends during history loading, stream deltas incrementally, reduce markdown work while streaming, and expose calmer composer controls. |
| 2026-06-077 | 2026-06-02 | openclaw 2026.6.1 | 渠道与消息平台 | Channels and mobile delivery become steadier across Telegram, WhatsApp, iMessage, Slack, Discord, Microsoft Teams, Google Chat, Google Meet, and iOS realtime Talk. |
| 2026-06-080 | 2026-06-02 | openclaw 2026.6.1 | Control UI/WebChat/桌面与移动端体验 | iOS adds hosted push relay defaults, realtime Talk playback, guarded WebSocket ping, and native iPad display layouts. |
| 2026-06-082 | 2026-06-02 | openclaw 2026.6.1 | Control UI/WebChat/桌面与移动端体验 | Control UI adds a Dreaming-tab agent selector and propagates the selected agent through Dreaming status, diary, and diary actions. |
| 2026-06-072 | 2026-06-03 | openclaw 2026.6.2-beta.1 | 渠道与消息平台 | Telegram progress drafts can show commentary and reasoning, shared progress draft compositors are used across channel plugins, and Telegram polling stop/reset boundaries are cheaper and more reliable. |
| 2026-06-073 | 2026-06-03 | openclaw 2026.6.2-beta.1 | Control UI/WebChat/桌面与移动端体验 | Workboard adds keyboard movement controls and tighter card operations, while Android companion-first shell UX improves. |
| 2026-06-075 | 2026-06-03 | openclaw 2026.6.2-beta.1 | Control UI/WebChat/桌面与移动端体验 | Chat, Control UI, Skill Workshop, Workboard, Android companion shell, and WebChat flows preserve streaming text, reconcile completed sends, expose ACK timing, improve dialog accessibility, lazy-load usage views, and keep current chat toggles working. |
| 2026-06-057 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 渠道与消息平台 | QQBot strips model reasoning/thinking scaffolding before native delivery. |
| 2026-06-061 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 渠道与消息平台 | Matrix adds voice-note preflight before mention gating and preserves thread reads/replies through Matrix relations pagination. |
| 2026-06-066 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 渠道与消息平台 | Google Chat approvals use platform-native approval card actions and click handling. |
| 2026-06-067 | 2026-06-08 | openclaw 2026.6.5-beta.6 | Control UI/WebChat/桌面与移动端体验 | Android provider/model screens surface expiring, unavailable, unresolved, and attention states; Android adds theme mode selection; iOS settings and Talk tabs keep diagnostics, gateway rows, attachment labels, fallback copy, and unavailable Talk controls reachable. |
| 2026-06-047 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 渠道与消息平台 | Telegram delivery is safer and more coherent, with account-scoped topics, streamed text through tool calls, /compact on generic ingress, concrete callback APIs, shared draft chunking, SDK-level durable dispatch dedupe, and unauthorized DM text kept out of cache and prompt context. |
| 2026-06-048 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 渠道与消息平台 | iMessage recovery and delivery cover always-on inbound restart, durable echo markers, block streaming, idle approval discovery, hardened outbound transport, and actionable startup diagnostics. |
| 2026-06-049 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | Control UI/WebChat/桌面与移动端体验 | Control UI startup and first-reply latency improve through cached model metadata, no startup catalog wait, lazy slash-command loading, first-event tracing, and slow-reply diagnostics. |
| 2026-06-050 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 渠道与消息平台 | Claude CLI commentary progress events can bridge inter-tool commentary into channel progress without exposing protocol scaffolding. |
| 2026-06-053 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 渠道与消息平台 | QQBot adds a group mention toggle, iPad/iPhone control surfaces improve, and the TUI footer exposes the active connection host. |
| 2026-06-038 | 2026-06-17 | openclaw 2026.6.8 | 渠道与消息平台 | Telegram and WhatsApp delivery support richer structured messages, including tables, lists, expandable blockquotes, preserved line breaks, CLI-backed replies, and WhatsApp ACP bindings. |
| 2026-06-041 | 2026-06-17 | openclaw 2026.6.8 | Control UI/WebChat/桌面与移动端体验 | UI and mobile sessions are calmer: workspace files start collapsed, WebChat backscroll survives streaming, the desktop session picker remains interactive, reset arguments survive dispatch, and iOS reconnects stale foreground Gateways. |
| 2026-06-042 | 2026-06-17 | openclaw 2026.6.8 | 渠道与消息平台 | /usage and reply payload hooks gain a native full footer renderer, default templates, fixed-decimal formatting, credential-aware limits, partial-count handling, and warnings for broken templates. |
| 2026-06-028 | 2026-06-20 | openclaw 2026.6.10-beta.1 | Control UI/WebChat/桌面与移动端体验 | Android settings are grouped by intent, iOS notification state is cleaner, Watch app targets are updated for Xcode 27, and macOS file inputs use the native panel. |
| 2026-06-031 | 2026-06-20 | openclaw 2026.6.10-beta.1 | Control UI/WebChat/桌面与移动端体验 | Chat users gain practical workflows to rename sessions, compact sessions explicitly, view session duration, preserve command progress detail, and preview message sends/polls with dry-run output. |
| 2026-06-034 | 2026-06-20 | openclaw 2026.6.9 | Control UI/WebChat/桌面与移动端体验 | Control UI adds a session workspace rail and extension health, iOS adds Watch controls, and Android shows chat context. |
| 2026-06-036 | 2026-06-20 | openclaw 2026.6.9 | 渠道与消息平台 | Telegram delivery gains richer HTML/markdown rendering, sticker paths, safer HTML table normalization, and more faithful progress and command output. |
| 2026-06-022 | 2026-06-23 | openclaw 2026.6.11-beta.1 | 渠道与消息平台 | Channel control expands with Slack relay mode, native Mattermost /oc_queue, and per-DM model overrides. |
| 2026-06-025 | 2026-06-23 | openclaw 2026.6.11-beta.1 | Control UI/WebChat/桌面与移动端体验 | Android settings detail panels improve mobile configuration visibility and control. |
| 2026-06-001 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Channel delivery reliability improved across Telegram, WhatsApp, Matrix, Google Chat, iMessage, Feishu, Mattermost, WebChat, Control UI, and TUI, with better reply targeting, progress rendering, reconnect behavior, and conversation continuity. |
| 2026-06-002 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Shared gateways can assign different models to individual direct-message contacts across supported chat channels while preserving existing group and wildcard model choices. |
| 2026-06-003 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | QQBot admins can control slash-command availability in groups, and private-only commands now route users toward private chat. |
| 2026-06-004 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Mattermost gains native /oc_queue controls for active-run queuing and persistent thread participation without requiring repeated bot mentions. |
| 2026-06-005 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Slack router relay mode supports managed and multi-gateway Slack deployments by centralizing incoming traffic while preserving gateway ownership of mentions, threads, and replies. |
| 2026-06-006 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Exec approval results from external channel plugins now return to the originating channel or DM instead of falling back to WebChat. |
| 2026-06-012 | 2026-06-30 | openclaw 2026.6.11 | 渠道与消息平台 | Raft channel/plugin support the local CLI wake path for External Agents with named profiles and prerequisite checks. |
| 2026-07-003 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 渠道与消息平台 | Telegram Codex workflows now support `/login` pairing, steering active Codex runs, multi-lane progress summaries, and more durable final replies. |
| 2026-07-005 | 2026-07-05 | openclaw 2026.7.1-beta.2 | Control UI/WebChat/桌面与移动端体验 | Native apps get a broad refresh: iOS adopts the iOS 26 visual system with clearer Chat, Talk, onboarding, and reconnect flows; Apple and Android surfaces gain expanded localization. |
| 2026-07-006 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 渠道与消息平台 | Messaging expands with native iMessage poll creation, reading, and voting, plus clearer built-in per-turn usage footers. |
| 2026-07-009 | 2026-07-05 | openclaw 2026.7.1-beta.2 | Control UI/WebChat/桌面与移动端体验 | Control UI navigation improves with a session-first sidebar, compact context meter, warm light theme, reasoning-effort slider, streamlined composer, and slash-command picker. |

### Agent能力

| ID | 时间 | Release | 二级分类 | 原始变更说明 |
| --- | --- | --- | --- | --- |
| 2026-01-054 | 2026-01-21 | clawdbot 2026.1.21 | 模型与 Provider | Refreshed /models, /model listing, model paging, and the interactive update wizard. |
| 2026-01-044 | 2026-01-22 | clawdbot 2026.1.22 | 记忆/上下文与转录 | Added adaptive compaction safeguards with chunking, progressive fallback, UI status, and retries. |
| 2026-01-045 | 2026-01-22 | clawdbot 2026.1.22 | 模型与 Provider | Added Antigravity usage tracking to provider status output. |
| 2026-01-039 | 2026-01-23 | Clawdbot 2026.1.23 | 模型与 Provider | Added Bedrock auto-discovery defaults and config overrides. |
| 2026-01-024 | 2026-01-24 | Clawdbot 2026.1.24 | 模型与 Provider | Added Ollama discovery and upgraded Venice provider guidance. |
| 2026-01-029 | 2026-01-24 | Clawdbot 2026.1.24 | Agent 运行时与任务编排 | Added Brave web-search freshness filtering for time-scoped results. |
| 2026-01-021 | 2026-01-28 | Introducing OpenClaw | 模型与 Provider | Added KIMI K2.5 and Xiaomi MiMo-V2-Flash model support. |
| 2026-01-002 | 2026-01-30 | openclaw 2026.1.30 | 模型与 Provider | Added per-agent model status filtering in the CLI. |
| 2026-01-003 | 2026-01-30 | openclaw 2026.1.30 | 模型与 Provider | Added Kimi K2.5 to the synthetic model catalog and moved Kimi Coding to the built-in provider flow. |
| 2026-01-004 | 2026-01-30 | openclaw 2026.1.30 | 模型与 Provider | Added MiniMax OAuth plugin support and onboarding. |
| 2026-02-060 | 2026-02-01 | openclaw 2026.2.1 | 模型与 Provider | Agents add OpenRouter app attribution headers. |
| 2026-02-062 | 2026-02-01 | openclaw 2026.2.1 | Agent 运行时与任务编排 | Agent session creation options now accept systemPrompt, skills, and contextFiles. |
| 2026-02-064 | 2026-02-01 | openclaw 2026.2.1 | Agent 运行时与任务编排 | Gateway injects timestamps into agent and chat.send messages. |
| 2026-02-055 | 2026-02-03 | openclaw 2026.2.2 | 记忆/上下文与转录 | Memory adds an opt-in QMD backend for workspace memory. |
| 2026-02-057 | 2026-02-03 | openclaw 2026.2.2 | Agent 运行时与任务编排 | Config allows default and per-agent subagent thinking levels. |
| 2026-02-047 | 2026-02-04 | openclaw 2026.2.3 | 模型与 Provider | Onboarding adds Cloudflare AI Gateway provider setup and docs. |
| 2026-02-048 | 2026-02-04 | openclaw 2026.2.3 | 模型与 Provider | Onboarding adds Moonshot .cn auth choice while preserving the China base URL. |
| 2026-02-050 | 2026-02-04 | openclaw 2026.2.3 | Agent 运行时与任务编排 | Cron adds announce delivery mode for isolated jobs across CLI and Control UI, ISO 8601 schedule.at inputs, one-shot cleanup after success, and consistent announce summaries. |
| 2026-02-041 | 2026-02-06 | openclaw 2026.2.6 | 模型与 Provider | Models add support for Anthropic Opus 4.6 and OpenAI Codex gpt-5.3-codex with forward-compat fallbacks. |
| 2026-02-042 | 2026-02-06 | openclaw 2026.2.6 | 模型与 Provider | Providers add xAI Grok support. |
| 2026-02-044 | 2026-02-06 | openclaw 2026.2.6 | 记忆/上下文与转录 | Memory adds native Voyage AI support. |
| 2026-02-045 | 2026-02-06 | openclaw 2026.2.6 | 记忆/上下文与转录 | Sessions cap sessions_history payloads to reduce context overflow. |
| 2026-02-034 | 2026-02-08 | openclaw 2026.2.9 | 模型与 Provider | Web search can use Grok/xAI as a provider. |
| 2026-02-026 | 2026-02-13 | openclaw 2026.2.13 | 模型与 Provider | Agents add synthetic catalog support for hf:zai-org/GLM-5. |
| 2026-02-027 | 2026-02-13 | openclaw 2026.2.13 | 模型与 Provider | Onboarding adds first-class Hugging Face Inference provider support, including provider wiring, API-key auth flow, default-model selection, and explicit-token handling. |
| 2026-02-016 | 2026-02-15 | openclaw 2026.2.15 | Agent 运行时与任务编排 | Subagents can now spawn nested subagents with configurable depth, child limits, depth-aware tool policy, and announce-chain routing. |
| 2026-02-018 | 2026-02-15 | openclaw 2026.2.15 | Agent 运行时与任务编排 | Cron webhooks gain a finished-run delivery toggle and dedicated webhook auth token support. |
| 2026-02-002 | 2026-02-26 | openclaw 2026.2.26 | Agent 运行时与任务编排 | ACP agents become first-class runtimes for thread sessions, including spawn/send dispatch integration, acpx backend bridging, lifecycle controls, startup reconciliation, runtime cleanup, and coalesced thread replies. |
| 2026-02-003 | 2026-02-26 | openclaw 2026.2.26 | Agent 运行时与任务编排 | New agents routing CLI commands add account-scoped route management through openclaw agents bindings, bind, and unbind, with binding upgrades and plugin-resolved account IDs. |
| 2026-02-004 | 2026-02-26 | openclaw 2026.2.26 | Agent 运行时与任务编排 | openai-codex now defaults to WebSocket-first transport with SSE fallback while retaining explicit per-model and per-runtime transport overrides. |
| 2026-02-010 | 2026-02-26 | openclaw 2026.2.26 | 模型与 Provider | Model/provider handling improves with MiniMax auth-header defaults, Google Gemini forward-compat fallbacks, profile suffix parsing that preserves @ in model IDs, OpenAI Codex config schema parity, and Azure OpenAI Responses store=true behavior. |
| 2026-03-164 | 2026-03-01 | openclaw 2026.3.1 | 模型与 Provider | Made adaptive thinking the default for Anthropic Claude 4.6 models, including Bedrock Claude 4.6 references. |
| 2026-03-173 | 2026-03-01 | openclaw 2026.3.1 | 记忆/上下文与转录 | Added LanceDB memory support for custom OpenAI baseUrl and embedding dimensions. |
| 2026-03-174 | 2026-03-01 | openclaw 2026.3.1 | Agent 运行时与任务编排 | Updated ACPX streaming support with configurable command/version probing and lower-noise stream delivery. |
| 2026-03-175 | 2026-03-01 | openclaw 2026.3.1 | Agent 运行时与任务编排 | Added OPENCLAW_SHELL markers across shell-like runtimes. |
| 2026-03-176 | 2026-03-01 | openclaw 2026.3.1 | 记忆/上下文与转录 | Added lightweight bootstrap context for cron agent turns and heartbeat runs. |
| 2026-03-177 | 2026-03-01 | openclaw 2026.3.1 | 模型与 Provider | Added optional OpenAI Responses WebSocket warm-up. |
| 2026-03-178 | 2026-03-01 | openclaw 2026.3.1 | Agent 运行时与任务编排 | Replaced ad-hoc subagent completion handoff with typed internal completion events. |
| 2026-03-180 | 2026-03-01 | openclaw 2026.3.1 | 模型与 Provider | Made OpenAI Responses streaming WebSocket-first by default with SSE fallback. |
| 2026-03-151 | 2026-03-02 | openclaw 2026.3.2 | 模型与 Provider | Added first-class MiniMax-M2.5-highspeed support across catalogs, onboarding, and MiniMax OAuth defaults. |
| 2026-03-152 | 2026-03-02 | openclaw 2026.3.2 | Agent 运行时与任务编排 | Added inline file attachment support for sessions_spawn in subagent runtime. |
| 2026-03-157 | 2026-03-02 | openclaw 2026.3.2 | 记忆/上下文与转录 | Added Ollama memory embedding support through memorySearch.provider and memorySearch.fallback. |
| 2026-03-128 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added a ContextEngine plugin slot with lifecycle hooks, slot-based registry, legacy wrapper, scoped subagent runtime, and sessions.get gateway method. |
| 2026-03-133 | 2026-03-07 | openclaw 2026.3.7 | Agent 运行时与任务编排 | Added web-search provider selection during onboarding/configure, including SecretRef ref-mode support. |
| 2026-03-134 | 2026-03-07 | openclaw 2026.3.7 | Agent 运行时与任务编排 | Switched Perplexity web search to the Search API with structured results and language, region, and time filters. |
| 2026-03-137 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added plugin before_prompt_build prependSystemContext and appendSystemContext fields. |
| 2026-03-138 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added compaction lifecycle hook events and plugin callbacks. |
| 2026-03-139 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added configurable post-compaction AGENTS section reinjection. |
| 2026-03-142 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added configurable head+tail truncation for oversized tool results. |
| 2026-03-143 | 2026-03-07 | openclaw 2026.3.7 | 记忆/上下文与转录 | Added compaction safeguard tuning knobs to the validated config surface. |
| 2026-03-145 | 2026-03-07 | openclaw 2026.3.7 | 模型与 Provider | Added first-class google/gemini-3.1-flash-lite-preview support. |
| 2026-03-112 | 2026-03-08 | openclaw 2026.3.8 | 记忆/上下文与转录 | Added Brave LLM Context mode for web_search with extracted grounding snippets and source metadata. |
| 2026-03-114 | 2026-03-08 | openclaw 2026.3.8 | Agent 运行时与任务编排 | Added ACP ingress provenance metadata and optional visible receipts. |
| 2026-03-115 | 2026-03-08 | openclaw 2026.3.8 | Agent 运行时与任务编排 | Normalized web-search provider ordering across runtime selection, onboarding, and configuration pickers. |
| 2026-03-119 | 2026-03-08 | openclaw 2026.3.8 | 模型与 Provider | Updated openai-codex/gpt-5.4 forward-compat model limits. |
| 2026-03-120 | 2026-03-08 | openclaw 2026.3.8 | 模型与 Provider | Restored Perplexity OpenRouter/Sonar compatibility for legacy key and baseUrl setups while preserving the native Search API path. |
| 2026-03-122 | 2026-03-08 | openclaw 2026.3.8 | 记忆/上下文与转录 | Persisted successful ACP child-run transcripts with spawned-session lineage. |
| 2026-03-124 | 2026-03-08 | openclaw 2026.3.8 | 记忆/上下文与转录 | Added context-engine plugin bootstrapping at embedded-run, compaction, and subagent boundaries. |
| 2026-03-099 | 2026-03-11 | openclaw 2026.3.11 | 模型与 Provider | Added temporary Hunter Alpha and Healer Alpha OpenRouter catalog entries. |
| 2026-03-102 | 2026-03-11 | openclaw 2026.3.11 | 模型与 Provider | Added first-class Ollama onboarding with Local and Cloud + Local modes, browser cloud sign-in, and curated model suggestions. |
| 2026-03-103 | 2026-03-11 | openclaw 2026.3.11 | 模型与 Provider | Added OpenCode Go provider setup alongside OpenCode Zen with shared onboarding and key storage. |
| 2026-03-104 | 2026-03-11 | openclaw 2026.3.11 | 记忆/上下文与转录 | Added multimodal image/audio memory indexing for memorySearch.extraPaths with Gemini gemini-embedding-2-preview. |
| 2026-03-105 | 2026-03-11 | openclaw 2026.3.11 | 记忆/上下文与转录 | Added Gemini embedding memory-search support with configurable output dimensions and automatic reindexing. |
| 2026-03-108 | 2026-03-11 | openclaw 2026.3.11 | Agent 运行时与任务编排 | Added ACP sessions_spawn resumeSessionId support for resuming existing ACPX/Codex conversations. |
| 2026-03-093 | 2026-03-12 | openclaw 2026.3.12 | 模型与 Provider | Added configurable session-level fast toggles across /fast, TUI, Control UI, and ACP for OpenAI/Codex. |
| 2026-03-094 | 2026-03-12 | openclaw 2026.3.12 | 模型与 Provider | Added Anthropic Claude fast-mode mapping to direct API service_tier requests. |
| 2026-03-095 | 2026-03-12 | openclaw 2026.3.12 | 模型与 Provider | Moved Ollama, vLLM, and SGLang onto provider-plugin architecture with provider-owned onboarding, discovery, model picker setup, and post-selection hooks. |
| 2026-03-097 | 2026-03-12 | openclaw 2026.3.12 | Agent 运行时与任务编排 | Added sessions_yield so orchestrators can end the current turn and carry hidden follow-up payloads into the next session turn. |
| 2026-03-088 | 2026-03-13 | openclaw 2026.3.13 | Agent 运行时与任务编排 | Added official Chrome DevTools MCP attach mode for signed-in live Chrome sessions. |
| 2026-03-090 | 2026-03-13 | openclaw 2026.3.13 | Agent 运行时与任务编排 | Added batched browser actions, selector targeting, delayed clicks, and normalized browser act dispatch. |
| 2026-03-061 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Updated default OpenAI setup models to openai/gpt-5.4 and openai-codex/gpt-5.4, with centralized OpenAI defaults. |
| 2026-03-062 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Added per-agent thinking, reasoning, and fast defaults with automatic reversion of disallowed model overrides. |
| 2026-03-063 | 2026-03-22 | openclaw 2026.3.22 | 记忆/上下文与转录 | Added /btw side questions for quick tool-less answers without changing future session context. |
| 2026-03-066 | 2026-03-22 | openclaw 2026.3.22 | Agent 运行时与任务编排 | Added browser profile userDataDir support for attaching Chrome DevTools MCP to Brave, Edge, and other Chromium browsers. |
| 2026-03-067 | 2026-03-22 | openclaw 2026.3.22 | Agent 运行时与任务编排 | Exposed bundle MCP servers as runnable embedded Pi tools and rooted relative bundle MCP launches at the bundle root. |
| 2026-03-069 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Added Anthropic Vertex provider support for Claude via Google Vertex AI. |
| 2026-03-070 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Added a bundled Chutes provider with plugin-owned OAuth/API-key auth and dynamic model discovery. |
| 2026-03-071 | 2026-03-22 | openclaw 2026.3.22 | Agent 运行时与任务编排 | Added Exa, Tavily, and Firecrawl as bundled web-search/tool providers. |
| 2026-03-072 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Added OpenAI provider catalog support for gpt-5.4-mini and gpt-5.4-nano. |
| 2026-03-081 | 2026-03-22 | openclaw 2026.3.22 | 模型与 Provider | Expanded MiniMax, GitHub Copilot, xAI, Z.AI, Mistral, and Xiaomi model/provider metadata and fast-mode support. |
| 2026-03-084 | 2026-03-22 | openclaw 2026.3.22 | 记忆/上下文与转录 | Preserved registered skills with a compact catalog fallback before dropping prompt entries under budget pressure. |
| 2026-03-036 | 2026-03-28 | openclaw 2026.3.28 | 模型与 Provider | Moved the bundled xAI provider to the Responses API, added first-class x_search, and auto-enabled configured xAI search/tool flows. |
| 2026-03-037 | 2026-03-28 | openclaw 2026.3.28 | 模型与 Provider | Added optional Grok x_search setup during onboarding and web-search configuration. |
| 2026-03-042 | 2026-03-28 | openclaw 2026.3.28 | 模型与 Provider | Moved bundled Claude CLI, Codex CLI, and Gemini CLI inference defaults onto plugin surfaces and added bundled Gemini CLI backend support. |
| 2026-03-043 | 2026-03-28 | openclaw 2026.3.28 | 模型与 Provider | Auto-loaded bundled provider and CLI-backend plugins from explicit config references. |
| 2026-03-049 | 2026-03-28 | openclaw 2026.3.28 | 记忆/上下文与转录 | Moved memory pre-compaction flush planning behind the active memory plugin contract. |
| 2026-03-051 | 2026-03-28 | openclaw 2026.3.28 | 模型与 Provider | Added MiniMax M2.7 catalog/default updates while trimming older legacy MiniMax catalog entries. |
| 2026-03-016 | 2026-03-30 | openclaw 2026.3.31 | Agent 运行时与任务编排 | Promoted background tasks into a shared SQLite-backed control plane across ACP, subagents, cron, and background CLI execution, with lifecycle status, audit, maintenance, cleanup, and recovery visibility. |
| 2026-03-017 | 2026-03-30 | openclaw 2026.3.31 | Agent 运行时与任务编排 | Added the first task-flow control surface with openclaw flows list\|show\|cancel. |
| 2026-03-024 | 2026-03-30 | openclaw 2026.3.31 | 记忆/上下文与转录 | Added per-agent memorySearch.qmd.extraCollections for opt-in cross-agent session search. |
| 2026-03-027 | 2026-03-30 | openclaw 2026.3.31 | 模型与 Provider | Forwarded OpenAI Responses text.verbosity across HTTP and WebSocket transports and surfaced it in /status. |
| 2026-03-028 | 2026-03-30 | openclaw 2026.3.31 | Agent 运行时与任务编排 | Added native Codex web search support for embedded Pi runs. |
| 2026-03-001 | 2026-03-31 | openclaw 2026.4.1 | Agent 运行时与任务编排 | Added /tasks as a chat-native background task board with current-session task details and agent-local fallback counts. |
| 2026-03-002 | 2026-03-31 | openclaw 2026.4.1 | Agent 运行时与任务编排 | Added bundled SearXNG web_search provider support with configurable host settings. |
| 2026-03-003 | 2026-03-31 | openclaw 2026.4.1 | 模型与 Provider | Added Amazon Bedrock Guardrails support to the bundled provider. |
| 2026-03-006 | 2026-03-31 | openclaw 2026.4.1 | 记忆/上下文与转录 | Made gateway webchat chat-history truncation configurable globally and per request. |
| 2026-03-007 | 2026-03-31 | openclaw 2026.4.1 | 模型与 Provider | Added agents.defaults.params for global default provider parameters. |
| 2026-03-008 | 2026-03-31 | openclaw 2026.4.1 | 模型与 Provider | Added rate-limit-aware auth-profile retry caps before cross-provider model fallback, with a configurable rotation cooldown. |
| 2026-03-012 | 2026-03-31 | openclaw 2026.4.1 | 模型与 Provider | Added glm-5.1 and glm-5v-turbo to the bundled Z.AI provider catalog. |
| 2026-03-013 | 2026-03-31 | openclaw 2026.4.1 | 记忆/上下文与转录 | Made agents.defaults.compaction.model apply consistently across manual /compact and other compaction entrypoints. |
| 2026-04-122 | 2026-04-01 | openclaw 2026.4.2 | Agent 运行时与任务编排 | Task Flow returned as a core substrate with managed-vs-mirrored sync modes, durable state/revision tracking, inspection, recovery, managed child task spawning, and sticky cancel intent. |
| 2026-04-123 | 2026-04-01 | openclaw 2026.4.2 | Agent 运行时与任务编排 | Plugins gained a bound `api.runtime.taskFlow` seam for creating and driving managed TaskFlows from host-resolved OpenClaw context. |
| 2026-04-126 | 2026-04-01 | openclaw 2026.4.2 | 模型与 Provider | Providers gained replay hook surfaces for transcript policy, replay cleanup, and reasoning-mode dispatch. |
| 2026-04-113 | 2026-04-05 | openclaw 2026.4.5 | 模型与 Provider | Bundled providers expanded with Qwen, Fireworks AI, StepFun, MiniMax TTS, Ollama Web Search, MiniMax Search, Amazon Bedrock Mantle, xAI video, Alibaba Model Studio Wan, and Runway video. |
| 2026-04-118 | 2026-04-05 | openclaw 2026.4.5 | 模型与 Provider | Provider requests gained shared transport overrides for OpenAI-, Anthropic-, Google-, and compatible paths, including headers, auth, proxy, and TLS controls. |
| 2026-04-119 | 2026-04-05 | openclaw 2026.4.5 | Agent 运行时与任务编排 | Claude CLI runs now expose OpenClaw tools through a loopback MCP bridge with stdin and stream-json partial-message streaming. |
| 2026-04-121 | 2026-04-05 | openclaw 2026.4.5 | 记忆/上下文与转录 | Memory/dreaming added aging controls, REM preview tooling, Dream Diary surfaces, `dreams.md`, and replay-safe durable promotion. |
| 2026-04-103 | 2026-04-07 | openclaw 2026.4.7 | 模型与 Provider | `openclaw infer` became a first-class provider-backed hub for model, media, web, and embedding workflows. |
| 2026-04-104 | 2026-04-07 | openclaw 2026.4.7 | 记忆/上下文与转录 | The bundled memory-wiki stack returned with plugin, CLI, sync/query/apply tooling, memory-host integration, structured claim/evidence fields, digest retrieval, claim-health linting, contradiction clustering, staleness dashboards, and freshness-weighted search. |
| 2026-04-105 | 2026-04-07 | openclaw 2026.4.7 | Agent 运行时与任务编排 | A bundled webhook ingress plugin can create and drive bound TaskFlows through per-route shared-secret endpoints. |
| 2026-04-106 | 2026-04-07 | openclaw 2026.4.7 | 记忆/上下文与转录 | Compaction gained a pluggable provider registry so plugins can replace built-in summarization. |
| 2026-04-107 | 2026-04-07 | openclaw 2026.4.7 | Agent 运行时与任务编排 | Agent defaults gained `systemPromptOverride` and heartbeat prompt-section controls for controlled prompt/runtime experiments. |
| 2026-04-108 | 2026-04-07 | openclaw 2026.4.7 | 模型与 Provider | Google added Gemma 4 support, Arcee AI shipped as a bundled provider plugin, Anthropic restored Claude CLI as the preferred local path, and Ollama detects vision capability from `/api/show`. |
| 2026-04-109 | 2026-04-07 | openclaw 2026.4.7 | 记忆/上下文与转录 | Dreaming can ingest redacted session transcripts into the dreaming corpus with per-day notes, cursor checkpointing, and promotion/doctor support. |
| 2026-04-098 | 2026-04-08 | openclaw 2026.4.9 | 记忆/上下文与转录 | Memory/dreaming added REM backfill from historical notes, diary commit/reset flows, durable-fact extraction, and live short-term promotion integration. |
| 2026-04-101 | 2026-04-08 | openclaw 2026.4.9 | 模型与 Provider | Provider manifests gained `providerAuthAliases` so provider variants can share env vars, auth profiles, config-backed auth, and API-key onboarding choices. |
| 2026-04-096 | 2026-04-10 | openclaw 2026.4.10 | Agent 运行时与任务编排 | Agents gained an opt-in strict-agentic embedded Pi execution contract for GPT-5-family runs. |
| 2026-04-097 | 2026-04-10 | openclaw 2026.4.10 | Agent 运行时与任务编排 | OpenAI/Codex runs gained provider-owned tool schema compatibility and embedded-run replay/liveness state for long-running runs. |
| 2026-04-087 | 2026-04-11 | openclaw 2026.4.11 | 记忆/上下文与转录 | Dreaming/memory-wiki added ChatGPT import ingestion plus Imported Insights and Memory Palace diary subtabs. |
| 2026-04-093 | 2026-04-11 | openclaw 2026.4.11 | 模型与 Provider | Ollama caches context-window and capability metadata during model discovery. |
| 2026-04-078 | 2026-04-12 | openclaw 2026.4.12 | 记忆/上下文与转录 | Active Memory shipped as an optional memory sub-agent that can recall relevant preferences, context, and past details before the main reply, with configurable context modes and `/verbose` inspection. |
| 2026-04-081 | 2026-04-12 | openclaw 2026.4.12 | Agent 运行时与任务编排 | Gateway added `commands.list` so remote clients can discover runtime-native, text, skill, and plugin commands with argument metadata. |
| 2026-04-082 | 2026-04-12 | openclaw 2026.4.12 | 模型与 Provider | Model requests gained per-provider trusted private-network opt-in for self-hosted OpenAI-compatible endpoints. |
| 2026-04-084 | 2026-04-12 | openclaw 2026.4.12 | Agent 运行时与任务编排 | Codex shipped as a bundled provider with plugin-owned app-server harness, native auth, threads, model discovery, and compaction while keeping OpenAI routes separate. |
| 2026-04-085 | 2026-04-12 | openclaw 2026.4.12 | 模型与 Provider | LM Studio shipped as a bundled provider with onboarding, runtime model discovery, stream preload, and memory-search embeddings. |
| 2026-04-076 | 2026-04-13 | openclaw 2026.4.14 | 模型与 Provider | OpenAI Codex added forward-compatible support for `gpt-5.4-pro`, including pricing/limits and list/status visibility ahead of upstream catalog updates. |
| 2026-04-069 | 2026-04-15 | openclaw 2026.4.15 | 模型与 Provider | Anthropic defaults, Opus aliases, Claude CLI defaults, and bundled image understanding moved to Claude Opus 4.7. |
| 2026-04-072 | 2026-04-15 | openclaw 2026.4.15 | 记忆/上下文与转录 | Memory/LanceDB added cloud storage support for durable memory indexes. |
| 2026-04-073 | 2026-04-15 | openclaw 2026.4.15 | 记忆/上下文与转录 | GitHub Copilot embeddings became available for memory search. |
| 2026-04-074 | 2026-04-15 | openclaw 2026.4.15 | Agent 运行时与任务编排 | Local-model setups gained an experimental lean mode that drops heavyweight default tools to reduce prompt size. |
| 2026-04-075 | 2026-04-15 | openclaw 2026.4.15 | Agent 运行时与任务编排 | Bundled plugin runtime dependencies were localized to owning extensions, trimming published builds and reducing extension-owned baggage in core. |
| 2026-04-062 | 2026-04-20 | openclaw 2026.4.20 | Agent 运行时与任务编排 | Default agent prompts and the OpenAI GPT-5 overlay gained stronger completion bias, live-state checks, weak-result recovery, and verification guidance. |
| 2026-04-063 | 2026-04-20 | openclaw 2026.4.20 | 模型与 Provider | Model usage reporting gained tiered pricing support from cached catalogs/configured models, including bundled Moonshot Kimi K2.6/K2.5 estimates. |
| 2026-04-065 | 2026-04-20 | openclaw 2026.4.20 | 模型与 Provider | Moonshot setup, web search, and media-understanding defaults moved to Kimi K2.6 while retaining K2.5 compatibility. |
| 2026-04-067 | 2026-04-20 | openclaw 2026.4.20 | Agent 运行时与任务编排 | Plugin executors gained a detached task lifecycle/cancellation contract. |
| 2026-04-048 | 2026-04-22 | openclaw 2026.4.22 | 模型与 Provider | xAI gained image generation, text-to-speech, speech-to-text, reference-image edits, live voices, and realtime transcription for Voice Call streaming. |
| 2026-04-052 | 2026-04-22 | openclaw 2026.4.22 | 模型与 Provider | OpenAI Responses models can use OpenAI native web search automatically when web search is enabled and no managed search provider is pinned. |
| 2026-04-053 | 2026-04-22 | openclaw 2026.4.22 | 模型与 Provider | Chat added `/models add` for registering a model without restarting the gateway. |
| 2026-04-057 | 2026-04-22 | openclaw 2026.4.22 | 模型与 Provider | Tencent Cloud shipped as a bundled provider plugin with TokenHub onboarding, docs, model catalog entries, and pricing metadata. |
| 2026-04-058 | 2026-04-22 | openclaw 2026.4.22 | 模型与 Provider | GPT-5 prompt overlays moved into shared provider runtime for OpenAI, OpenRouter, OpenCode, Codex, and compatible GPT providers. |
| 2026-04-059 | 2026-04-22 | openclaw 2026.4.22 | Agent 运行时与任务编排 | `/status` now reports the active runner, such as embedded Pi, CLI provider, or ACP harness backend. |
| 2026-04-045 | 2026-04-23 | openclaw 2026.4.23 | Agent 运行时与任务编排 | Native `sessions_spawn` added optional forked context so child sessions can inherit requester transcript context when needed while keeping isolation as the default. |
| 2026-04-047 | 2026-04-23 | openclaw 2026.4.23 | 记忆/上下文与转录 | Local embedding memory search gained configurable context size for constrained hosts. |
| 2026-04-036 | 2026-04-24 | openclaw 2026.4.24 | Agent 运行时与任务编排 | Browser automation added coordinate clicks, longer default action budgets, per-profile headless overrides, and steadier tab reuse/recovery. |
| 2026-04-037 | 2026-04-24 | openclaw 2026.4.24 | 模型与 Provider | DeepSeek V4 Flash and V4 Pro entered the bundled catalog, with V4 Flash as the onboarding default. |
| 2026-04-040 | 2026-04-24 | openclaw 2026.4.24 | 模型与 Provider | Model listing and catalogs moved to faster static/manifest-sourced rows with conflict reporting and runtime-free provider listing. |
| 2026-04-041 | 2026-04-24 | openclaw 2026.4.24 | 记忆/上下文与转录 | Codex app-server sessions gained context-engine bootstrap, assembly, post-turn maintenance, engine-owned compaction, plugin hook bridges, approval relay, and fallback policy seams. |
| 2026-04-026 | 2026-04-26 | OpenClaw 2026.4.25 | Agent 运行时与任务编排 | Browser automation gained safer tab URLs, iframe-aware role snapshots, CDP readiness tuning, headless one-shot launch, and deeper browser doctor probes. |
| 2026-04-019 | 2026-04-27 | OpenClaw 2026.4.26 | 模型与 Provider | Cerebras shipped as a bundled provider plugin with onboarding, static model catalog, docs, and manifest-owned endpoint metadata. |
| 2026-04-020 | 2026-04-27 | OpenClaw 2026.4.26 | 记忆/上下文与转录 | Memory search added asymmetric embedding endpoint configuration and model-specific retrieval query prefixes for local/OpenAI-compatible providers. |
| 2026-04-011 | 2026-04-28 | openclaw 2026.4.27 | 模型与 Provider | DeepInfra joined the bundled provider set with model discovery, image/media generation and editing, TTS, embeddings, and provider-owned onboarding policy. |
| 2026-04-015 | 2026-04-28 | openclaw 2026.4.27 | 模型与 Provider | Plugin and model catalogs moved further toward manifest-first metadata for faster gateway boot and easier provider/model auditing. |
| 2026-04-003 | 2026-04-29 | openclaw 2026.4.29 | 记忆/上下文与转录 | Memory expanded into a people-aware wiki with provenance views, per-conversation Active Memory filters, partial recall on timeout, and bounded REM preview diagnostics. |
| 2026-04-004 | 2026-04-29 | openclaw 2026.4.29 | 模型与 Provider | Provider and model coverage expanded with NVIDIA onboarding/catalogs, manifest-backed model/auth paths, Bedrock Opus 4.7 thinking parity, and safer Codex/OpenAI-compatible replay and streaming behavior. |
| 2026-05-072 | 2026-05-02 | openclaw 2026.5.2 | Agent 运行时与任务编排 | Platform tool descriptors and cached plugin tool descriptors allow prompt-time planning without repeated runtime loading while execution still loads the live plugin tool. |
| 2026-05-073 | 2026-05-02 | openclaw 2026.5.2 | 模型与 Provider | xAI Grok 4.3 was added to the bundled catalog and made the default xAI chat model. |
| 2026-05-075 | 2026-05-02 | openclaw 2026.5.2 | Agent 运行时与任务编排 | Thread-bound spawns became the default through `threadBindings.spawnSessions`, replacing split subagent/ACP toggles with doctor migration support. |
| 2026-05-077 | 2026-05-02 | openclaw 2026.5.2 | Agent 运行时与任务编排 | Gateway SDK added `tools.invoke` RPC with shared HTTP policy, typed approval/refusal results, and SDK helper support. |
| 2026-05-078 | 2026-05-02 | openclaw 2026.5.2 | Agent 运行时与任务编排 | Codex app-server dynamic tools became native-first, direct source replies default to the OpenClaw message tool when visible delivery is not configured, and heartbeat runs gained a structured `heartbeat_respond` tool. |
| 2026-05-068 | 2026-05-03 | OpenClaw 2026.5.3 | Agent 运行时与任务编排 | `/side` was added as a text and native slash-command alias for `/btw` side questions. |
| 2026-05-059 | 2026-05-04 | openclaw 2026.5.4 | 模型与 Provider | Models auth added `openclaw models auth list` for inspecting saved per-agent auth profiles without exposing secrets. |
| 2026-05-063 | 2026-05-04 | openclaw 2026.5.4 | 模型与 Provider | Providers added verified OpenRouter response-caching headers and broader OpenRouter app attribution categories. |
| 2026-05-054 | 2026-05-05 | openclaw 2026.5.6 | 模型与 Provider | Codex OAuth routing and valid `openai-codex` paths were restored, while plugin fetch, debug proxy, and web request handling became more robust. |
| 2026-05-047 | 2026-05-13 | OpenAI Models in OpenClaw, Done Right | Agent 运行时与任务编排 | Native Codex app-server support for OpenAI agent turns added cleaner tool search, intentional visible replies, subscription-backed auth, isolated per-agent state, and better long-running turn and approval support. |
| 2026-05-046 | 2026-05-15 | openclaw 2026.5.16-beta.2 | 模型与 Provider | xAI Grok OAuth login for SuperGrok users, cron waiting controls, and localized setup flows in English, Simplified Chinese, and Traditional Chinese were added. |
| 2026-05-041 | 2026-05-20 | openclaw 2026.5.20 | 模型与 Provider | xAI device-code login and OpenRouter routing controls were added. |
| 2026-05-034 | 2026-05-23 | openclaw 2026.5.24-beta.1 | 记忆/上下文与转录 | Meeting Notes added an external source-only plugin, SDK source-provider contract, auto-start capture config, manual transcript imports, read-only CLI access, and Discord voice as the first live source. |
| 2026-05-037 | 2026-05-23 | openclaw 2026.5.24-beta.1 | 模型与 Provider | CLI model auth can store a returned provider auth profile under a requested `--profile-id`, with named Codex OAuth profile setup documented. |
| 2026-05-021 | 2026-05-27 | openclaw 2026.5.27 | 模型与 Provider | Provider and model coverage added core OpenAI-compatible embedding providers, full credential-aware DeepInfra model catalog browsing, Pixverse video generation and API region selection, VLLM thinking params, Claude CLI OAuth overlays, and bare direct Anthropic model IDs. |
| 2026-05-022 | 2026-05-27 | openclaw 2026.5.27 | Agent 运行时与任务编排 | Codex app-server runs became more reliable across model resolution, workspace memory routing, shared app-server clients, native hook relay restarts, and runtime switch handling. |
| 2026-05-026 | 2026-05-27 | openclaw 2026.5.26 | 记忆/上下文与转录 | Transcripts became a core platform path for meeting summaries, source-provider chunks, cleaned user turns, media provenance, Codex mirrors, WebChat replies, and CLI/TUI replay. |
| 2026-05-030 | 2026-05-27 | openclaw 2026.5.26 | 模型与 Provider | Named model login profiles and credential migration support were added for Hermes, OpenCode, and Codex auth profiles. |
| 2026-05-012 | 2026-05-28 | openclaw 2026.5.28-beta.4 | 模型与 Provider | Provider, media, and document coverage expanded with Claude Opus 4.8, Fal Krea image schemas, NVIDIA featured models, MiniMax streaming music responses, encrypted PDF extraction, voice model catalogs, GitHub Copilot agent runtime support, and a Codex Supervisor plugin path. |
| 2026-05-004 | 2026-05-31 | openclaw 2026.5.31-beta.4 | Agent 运行时与任务编排 | Workboard added orchestration primitives and agent coordination tools for multi-agent planning, board-backed runs, task comments, and run tracking. |
| 2026-05-006 | 2026-05-31 | openclaw 2026.5.31-beta.4 | 模型与 Provider | Providers and model metadata expanded with MiniMax M3, account OAuth endpoints, OpenRouter SQLite model caching, Copilot Claude 1M capability metadata, Google/Vertex catalog alignment, and Foundry reasoning alignment. |
| 2026-06-078 | 2026-06-02 | openclaw 2026.6.1 | Agent 运行时与任务编排 | Workboard adds orchestration primitives and agent coordination tools for multi-agent planning and run tracking, including task-backed board runs and task comments in the edit modal. |
| 2026-06-081 | 2026-06-02 | openclaw 2026.6.1 | Agent 运行时与任务编排 | Code mode adds internal namespaces for scoped agent/global sessions, exact namespace tool dispatch, and MCP API files/docs for integrations. |
| 2026-06-085 | 2026-06-02 | openclaw 2026.6.1 | 模型与 Provider | Providers add MiniMax M3 model support, expanded provider/model metadata, and better OpenRouter/Google/Vertex/Copilot/Foundry/OpenAI response replay handling. |
| 2026-06-058 | 2026-06-08 | openclaw 2026.6.5-beta.6 | Agent 运行时与任务编排 | MCP tool results coerce resource links, resources, audio, malformed images, and future non-text/image blocks at the materialization boundary. |
| 2026-06-059 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 模型与 Provider | Parallel becomes a bundled web_search provider with PARALLEL_API_KEY discovery, guarded endpoint handling, cache-safe session ids, and onboarding picker support. |
| 2026-06-060 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 模型与 Provider | Google Vertex ADC users regain static catalog rows and runtime model resolution. |
| 2026-06-068 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 记忆/上下文与转录 | QMD search gains a rerank toggle, and memory adapter status uses the resolved default model identity. |
| 2026-06-052 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 记忆/上下文与转录 | Local llama.cpp runtime moves into its provider plugin, embeddings can batch across files, the agent model catalog cache persists, and QMD JSON search remains one-shot while filtering stale REM recall previews. |
| 2026-06-056 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 模型与 Provider | Provider support expands with OpenRouter OAuth onboarding and Claude Fable 5 adaptive thinking. |
| 2026-06-039 | 2026-06-17 | openclaw 2026.6.8 | 模型与 Provider | Model routing adds GLM-5.2 and Claude Haiku 4.5 catalog support with normalized provider IDs, managed SecretRef auth, bounded model browsing, and safer OpenAI/Anthropic tool-schema recovery. |
| 2026-06-040 | 2026-06-17 | openclaw 2026.6.8 | 模型与 Provider | Key-free search providers such as Parallel Free, DuckDuckGo, Ollama, and Codex Hosted Search remain explicit opt-ins instead of automatic fallbacks. |
| 2026-06-043 | 2026-06-17 | openclaw 2026.6.8 | Agent 运行时与任务编排 | CLI-backed sessions support /btw, and CLI usage-error exits are classified as usage failures rather than successful runs. |
| 2026-06-046 | 2026-06-17 | openclaw 2026.6.7-beta.1 | 模型与 Provider | Kimi K2.7 Code is added to the provider catalog, with reasoning replay preserved across tool turns. |
| 2026-06-032 | 2026-06-20 | openclaw 2026.6.9 | Agent 运行时与任务编排 | Codex integration adds automatic plugin approvals, GPT-5.3 Spark OAuth routing, remote-node exec as a dynamic tool, and more reliable app-server teardown and terminal outcomes. |
| 2026-06-035 | 2026-06-20 | openclaw 2026.6.9 | 模型与 Provider | Codex Hosted Search is available, key-free search providers remain explicit opt-ins, and ClawHub skill installs retain verified source provenance. |
| 2026-06-016 | 2026-06-25 | openclaw 2026.6.10 | Agent 运行时与任务编排 | Adds /fast auto so short conversational calls can start quickly while longer or fallback work returns to normal mode with the effective fast-mode state visible in status. |
| 2026-06-017 | 2026-06-25 | openclaw 2026.6.10 | 模型与 Provider | Zhipu/GLM overloads, zai/glm-5.2 reasoning effort, bundled Z.ai GLM-5 routing, and OpenCode Go model catalog entries for GLM-5.2 and Kimi K2.7 Code improve model selection and fallback behavior. |
| 2026-06-018 | 2026-06-25 | openclaw 2026.6.10 | 记忆/上下文与转录 | Adds a durable session-transcript SDK contract so plugins can read, append, publish, and lock the intended transcript without treating legacy file paths as identity. |
| 2026-06-021 | 2026-06-25 | openclaw 2026.6.10 | 模型与 Provider | StepFun provider plugin discovery is restored through ClawHub and npm. |
| 2026-06-007 | 2026-06-30 | openclaw 2026.6.11 | 模型与 Provider | Provider and model routing improves for Google, Mistral, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, OpenRouter, Vercel AI Gateway, LM Studio, Ollama Cloud, Xiaomi Token Plan, and DeepSeek-style OpenAI-compatible models. |
| 2026-06-008 | 2026-06-30 | openclaw 2026.6.11 | 模型与 Provider | Google Gemini 3.5 Flash, Ollama Cloud glm-5.2:cloud, and Vercel AI Gateway live-catalog models can be selected with their current context and tool capabilities. |
| 2026-06-009 | 2026-06-30 | openclaw 2026.6.11 | Agent 运行时与任务编排 | OpenAI Responses users, including affected Bedrock Mantle GPT-5.x reasoning setups, get a single clean final answer with aligned transcripts and replay context. |
| 2026-07-017 | 2026-07-01 | openclaw 2026.7.1-beta.1 | Agent 运行时与任务编排 | Initial beta introduced the core July capabilities: GPT-5.6 support, `openclaw attach`, Telegram Codex pairing and steering, event-driven cron runs, iOS/native app refresh, iMessage polls, usage footers, scoped conversation profiles, expanded diagnostics, and Cursor Agent autoreview support. |
| 2026-07-001 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 模型与 Provider | OpenAI GPT-5.6 support is available across model catalog, capability, and runtime selection paths. |
| 2026-07-002 | 2026-07-05 | openclaw 2026.7.1-beta.2 | Agent 运行时与任务编排 | `openclaw attach` can launch an external harness against an existing Gateway session, making interactive Codex-style sessions easier to resume and inspect. |
| 2026-07-004 | 2026-07-05 | openclaw 2026.7.1-beta.2 | Agent 运行时与任务编排 | Event-driven cron runs add an `on-exit` schedule kind that wakes an agent when a watched command exits, with session-targeted runs able to detach cleanly. |
| 2026-07-010 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 模型与 Provider | ClawRouter ships as a bundled provider plugin with credential-scoped dynamic model discovery, OpenAI-compatible and native Anthropic/Gemini transports, and managed budget reporting. |
| 2026-07-011 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 模型与 Provider | Model and provider coverage expands with Nemotron Super's 1M context window and explicit OpenRouter authentication header preservation. |
| 2026-07-013 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 模型与 Provider | Local inference and chat controls add Ollama inference node auto-discovery and keep OpenClaw control tools available when deferred tool search selects the wrong tool family. |
| 2026-07-015 | 2026-07-05 | openclaw 2026.7.1-beta.2 | Agent 运行时与任务编排 | Conversation and review controls add Cursor Agent as an autoreview engine. |

### 插件与生态

| ID | 时间 | Release | 二级分类 | 原始变更说明 |
| --- | --- | --- | --- | --- |
| 2026-01-049 | 2026-01-21 | clawdbot 2026.1.21 | 插件化与生态 | Added the Lobster optional plugin tool for typed workflows with approval gates. |
| 2026-01-047 | 2026-01-22 | clawdbot 2026.1.22 | 语音/Talk/Realtime 与会议 | Added BlueBubbles voice memo sending for MP3/CAF attachments. |
| 2026-01-033 | 2026-01-23 | Clawdbot 2026.1.23 | 语音/Talk/Realtime 与会议 | Moved Telegram TTS into core and enabled model-driven TTS tags by default for expressive audio replies. |
| 2026-01-042 | 2026-01-23 | Clawdbot 2026.1.23 | 插件化与生态 | Added an optional llm-task JSON-only plugin tool for workflows. |
| 2026-01-026 | 2026-01-24 | Clawdbot 2026.1.24 | 语音/Talk/Realtime 与会议 | Added keyless Edge TTS fallback and /tts auto modes. |
| 2026-01-019 | 2026-01-28 | Introducing OpenClaw | 插件化与生态 | Announced the OpenClaw rebrand and positioned the project as an open, self-hosted agent platform for chat apps. |
| 2026-01-007 | 2026-01-29 | openclaw 2026.1.29 | 插件化与生态 | Renamed the package and CLI to OpenClaw, added an openclaw compatibility shim, and moved extensions to the @openclaw scope. |
| 2026-01-015 | 2026-01-29 | openclaw 2026.1.29 | 多媒体与生成工具 | Added extra memory indexing paths and multi-image input support for Nano Banana Pro. |
| 2026-02-023 | 2026-02-13 | openclaw 2026.2.13 | 语音/Talk/Realtime 与会议 | Discord can send voice messages with waveform previews from local audio files, including silent delivery. |
| 2026-02-015 | 2026-02-15 | openclaw 2026.2.15 | 插件化与生态 | Plugins expose llm_input and llm_output hook payloads so extensions can observe prompt/input context and model output usage. |
| 2026-02-005 | 2026-02-26 | openclaw 2026.2.26 | 插件化与生态 | Channel plugins can own interactive onboarding through configureInteractive and configureWhenConfigured hooks. |
| 2026-03-172 | 2026-03-01 | openclaw 2026.3.1 | 多媒体与生成工具 | Added optional diffs plugin tool for read-only diff rendering with canvas and PNG outputs. |
| 2026-03-149 | 2026-03-02 | openclaw 2026.3.2 | 多媒体与生成工具 | Added a first-class pdf tool with native Anthropic and Google PDF support, extraction fallback, and configurable PDF defaults. |
| 2026-03-156 | 2026-03-02 | openclaw 2026.3.2 | 多媒体与生成工具 | Added PDF output and quality controls for generated diff artifacts. |
| 2026-03-160 | 2026-03-02 | openclaw 2026.3.2 | 插件化与生态 | Added plugin runtime APIs for STT transcription, targeted heartbeat wakeups, agent-event subscriptions, and session transcript subscriptions. |
| 2026-03-161 | 2026-03-02 | openclaw 2026.3.2 | 插件化与生态 | Added lifecycle and message hook context improvements for session keys, transcription, preprocessing, sent-message metadata, and audio transcript echo. |
| 2026-03-140 | 2026-03-07 | openclaw 2026.3.7 | 语音/Talk/Realtime 与会议 | Added OpenAI-compatible TTS baseUrl support with endpoint-aware validation. |
| 2026-03-121 | 2026-03-08 | openclaw 2026.3.8 | 语音/Talk/Realtime 与会议 | Added Talk mode silence-timeout configuration. |
| 2026-03-089 | 2026-03-13 | openclaw 2026.3.13 | 插件化与生态 | Added built-in browser profiles for the logged-in host browser and Chrome extension relay. |
| 2026-03-055 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Added ClawHub-backed openclaw skills search\|install\|update flows and gateway skill install/update support. |
| 2026-03-056 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Added Claude marketplace registry resolution, plugin@marketplace installs, marketplace listing, and plugin update support. |
| 2026-03-057 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Added owner-gated /plugins and /plugin chat commands for plugin list/show and enable/disable flows. |
| 2026-03-058 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Allowed installs and updates from GitHub main via openclaw update --tag main, installer --version main, or package-manager git specs. |
| 2026-03-059 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Added compatible Codex, Claude, and Cursor bundle discovery/install support, including bundle skill mapping and Claude bundle settings defaults for embedded Pi. |
| 2026-03-060 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Routed hook-pack install/update through openclaw plugins and surfaced plugin-managed hook details in CLI output. |
| 2026-03-068 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Moved OpenRouter, GitHub Copilot, and OpenAI Codex provider/runtime logic into bundled plugins. |
| 2026-03-076 | 2026-03-22 | openclaw 2026.3.22 | 语音/Talk/Realtime 与会议 | Moved Android Talk speech synthesis behind gateway talk.speak and final-response audio playback. |
| 2026-03-083 | 2026-03-22 | openclaw 2026.3.22 | 插件化与生态 | Added plugin SDK surfaces for app-server integrations, conversation-binding callbacks, context-engine delegation, model-aware context assembly, and plugin-author testing. |
| 2026-03-038 | 2026-03-28 | openclaw 2026.3.28 | 多媒体与生成工具 | Added MiniMax image generation for the image-01 model, including image-to-image editing and aspect-ratio controls. |
| 2026-03-050 | 2026-03-28 | openclaw 2026.3.28 | 插件化与生态 | Exposed runHeartbeatOnce in the plugin runtime system namespace. |
| 2026-03-023 | 2026-03-30 | openclaw 2026.3.31 | 插件化与生态 | Added remote HTTP/SSE MCP server support with auth headers and safer MCP credential redaction. |
| 2026-03-034 | 2026-03-30 | openclaw 2026.3.31 | 插件化与生态 | Added safer MCP bundle tool naming, streamable-http transport selection, and per-server connection timeouts. |
| 2026-03-004 | 2026-03-31 | openclaw 2026.4.1 | 语音/Talk/Realtime 与会议 | Added macOS Voice Wake as a Talk Mode trigger option. |
| 2026-03-010 | 2026-03-31 | openclaw 2026.4.1 | 插件化与生态 | Moved provider-specific session conversation grammar into plugin-owned session-key surfaces, preserving channel-specific routing and inheritance behavior. |
| 2026-04-127 | 2026-04-01 | openclaw 2026.4.2 | 插件化与生态 | Plugins gained `before_agent_reply` hooks to short-circuit the LLM with synthetic replies after inline actions. |
| 2026-04-111 | 2026-04-05 | openclaw 2026.4.5 | 多媒体与生成工具 | Agents gained built-in `video_generate` and `music_generate` tools with bundled provider support, async task tracking, and follow-up delivery of finished media. |
| 2026-04-112 | 2026-04-05 | openclaw 2026.4.5 | 多媒体与生成工具 | ComfyUI and Comfy Cloud workflows shipped as a bundled media plugin for image, video, and workflow-backed music generation. |
| 2026-04-115 | 2026-04-05 | openclaw 2026.4.5 | 插件化与生态 | Plugin onboarding gained config TUI prompts, force install replacement, and ClawHub search/detail/install flows in the Skills panel. |
| 2026-04-094 | 2026-04-10 | openclaw 2026.4.10 | 多媒体与生成工具 | Seedance 2.0 model refs were added to the bundled fal video provider with provider-specific duration, resolution, audio, and seed metadata. |
| 2026-04-089 | 2026-04-11 | openclaw 2026.4.11 | 多媒体与生成工具 | Video generation added URL-only asset delivery, typed provider options, reference audio inputs, per-asset role hints, adaptive aspect ratios, and a higher image-input cap. |
| 2026-04-092 | 2026-04-11 | openclaw 2026.4.11 | 插件化与生态 | Plugin manifests can declare activation and setup descriptors for auth, pairing, and configuration flows without hardcoded core cases. |
| 2026-04-079 | 2026-04-12 | openclaw 2026.4.12 | 语音/Talk/Realtime 与会议 | macOS Talk added an experimental local MLX speech provider with explicit selection, local playback, interruption handling, and system-voice fallback. |
| 2026-04-070 | 2026-04-15 | openclaw 2026.4.15 | 语音/Talk/Realtime 与会议 | Google plugin added Gemini text-to-speech with voice selection, WAV reply output, PCM telephony output, setup, and docs. |
| 2026-04-060 | 2026-04-21 | openclaw 2026.4.21 | 多媒体与生成工具 | OpenAI image generation defaulted to `gpt-image-2`, with newer 2K/4K size hints exposed in docs and tool metadata. |
| 2026-04-049 | 2026-04-22 | openclaw 2026.4.22 | 语音/Talk/Realtime 与会议 | Voice Call streaming transcription expanded to Deepgram, ElevenLabs, and Mistral, with ElevenLabs Scribe v2 batch transcription for inbound media. |
| 2026-04-051 | 2026-04-22 | openclaw 2026.4.22 | 插件化与生态 | Onboarding can auto-install missing provider and channel plugins during setup. |
| 2026-04-043 | 2026-04-23 | openclaw 2026.4.23 | 多媒体与生成工具 | Image generation gained provider-supported quality/output format hints plus OpenAI-specific background, moderation, compression, and user hints. |
| 2026-04-044 | 2026-04-23 | openclaw 2026.4.23 | 多媒体与生成工具 | OpenAI image generation and reference-image editing can work through Codex OAuth, and OpenRouter image models can use `image_generate`. |
| 2026-04-046 | 2026-04-23 | openclaw 2026.4.23 | 多媒体与生成工具 | Generation tools for image, video, music, and TTS gained per-call timeout overrides. |
| 2026-04-033 | 2026-04-24 | openclaw 2026.4.24 | 语音/Talk/Realtime 与会议 | Google Meet joined OpenClaw as a bundled participant plugin with personal Google auth, Chrome/Twilio realtime sessions, paired-node Chrome support, artifact/attendance exports, and recovery tooling for already-open Meet tabs. |
| 2026-04-034 | 2026-04-24 | openclaw 2026.4.24 | 语音/Talk/Realtime 与会议 | Talk, Voice Call, and Google Meet can use realtime voice loops that consult the full OpenClaw agent for deeper tool-backed answers. |
| 2026-04-035 | 2026-04-24 | openclaw 2026.4.24 | 语音/Talk/Realtime 与会议 | Gemini Live became a backend realtime voice provider for Voice Call and Google Meet audio bridges. |
| 2026-04-042 | 2026-04-24 | openclaw 2026.4.24 | 插件化与生态 | Local PDF extraction, Anthropic Vertex dependencies, Bonjour discovery, and other capabilities moved into plugins to reduce core dependency ownership. |
| 2026-04-024 | 2026-04-26 | OpenClaw 2026.4.25 | 语音/Talk/Realtime 与会议 | Voice replies received a full TTS upgrade: `/tts latest`, chat-scoped auto-TTS controls, personas, per-agent/per-account overrides, and new Azure Speech, Xiaomi, Local CLI, Inworld, Volcengine, and ElevenLabs v3 coverage. |
| 2026-04-028 | 2026-04-26 | OpenClaw 2026.4.25 | 语音/Talk/Realtime 与会议 | Google Meet added calendar-backed attendance export workflows, export manifests, dry-run previews, and tool parity for meeting records. |
| 2026-04-032 | 2026-04-26 | OpenClaw 2026.4.25 | 插件化与生态 | Plugin hooks expanded with before-agent-finalize hooks, cron job context, permission fingerprints, and Codex MCP hook relay support. |
| 2026-04-018 | 2026-04-27 | OpenClaw 2026.4.26 | 语音/Talk/Realtime 与会议 | Control UI Talk added a generic browser realtime transport contract, Google Live browser Talk sessions with constrained ephemeral tokens, and a Gateway relay for backend-only realtime voice plugins. |
| 2026-04-006 | 2026-04-29 | openclaw 2026.4.29 | 插件化与生态 | Plugin runtime state gained a SQLite-backed keyed store with TTL, eviction, restart safety, and automatic plugin isolation. |
| 2026-05-070 | 2026-05-02 | openclaw 2026.5.2 | 插件化与生态 | External plugin installation cutover covered npm-first packaging, source checkout loading, beta update handling, ClawPack artifact metadata, ClawHub search/install/uninstall, official bundled-plugin migration, and `git:` plugin installs. |
| 2026-05-074 | 2026-05-02 | openclaw 2026.5.2 | 语音/Talk/Realtime 与会议 | Google Meet added API room access controls, managed-space ending, test-listen health checks, live caption health, and richer Voice Call/Meet join diagnostics. |
| 2026-05-064 | 2026-05-03 | OpenClaw 2026.5.3 | 插件化与生态 | A bundled file-transfer plugin added `file_fetch`, `dir_list`, `dir_fetch`, and `file_write` tools for paired nodes, with default-deny per-node path policy, operator approval, refused symlink traversal by default, and a 16 MB round-trip ceiling. |
| 2026-05-065 | 2026-05-03 | OpenClaw 2026.5.3 | 插件化与生态 | Official plugin install, uninstall, update, onboarding, ClawHub fallback, npm dependency-state reporting, and beta-channel update paths were hardened for externalized plugins. |
| 2026-05-056 | 2026-05-04 | OpenClaw Had a Rough Week | 插件化与生态 | Optional tools, channels, and integrations moved toward ClawHub to make core smaller, safer, and more reliable, with an LTS release planned separately. |
| 2026-05-057 | 2026-05-04 | openclaw 2026.5.4 | 语音/Talk/Realtime 与会议 | Google Meet and Voice Call gained faster Twilio dial-in voice bridging through realtime Gemini voice, paced audio streaming, backpressure-aware buffering, barge-in queue clearing, and reduced TwiML fallback. |
| 2026-05-058 | 2026-05-04 | openclaw 2026.5.4 | 插件化与生态 | Plugin migration now emits catalog-backed install hints for official external plugins referenced in config. |
| 2026-05-039 | 2026-05-20 | openclaw 2026.5.20 | 语音/Talk/Realtime 与会议 | Discord voice gained richer session handling and realtime voice context defaults. |
| 2026-05-033 | 2026-05-23 | openclaw 2026.5.24-beta.1 | 语音/Talk/Realtime 与会议 | WebUI and Discord voice users can ask for active OpenClaw run status, cancel, steer, or queue follow-up work while a realtime consult is still running. |
| 2026-05-036 | 2026-05-23 | openclaw 2026.5.24-beta.1 | 多媒体与生成工具 | Image handling added adaptive model-aware compression with an `agents.defaults.imageQuality` preference for token-efficient, balanced, or high-detail media handling. |
| 2026-05-024 | 2026-05-27 | openclaw 2026.5.27 | 插件化与生态 | ClawHub catalog and package listings gained plugin display metadata. |
| 2026-05-025 | 2026-05-27 | openclaw 2026.5.27 | 插件化与生态 | Plugin SDK exposed approval action metadata and compatibility diagnostics for non-bundled embedding provider usage. |
| 2026-05-028 | 2026-05-27 | openclaw 2026.5.26 | 语音/Talk/Realtime 与会议 | Realtime Talk runs can be inspected, steered, cancelled, or followed up from Web UI and Discord voice while wake-name handling stays tolerant but bounded. |
| 2026-05-013 | 2026-05-28 | openclaw 2026.5.28-beta.4 | 插件化与生态 | ClawHub added plugin display names plus skill verification and trust surfaces. |
| 2026-05-015 | 2026-05-28 | openclaw 2026.5.28-beta.4 | 多媒体与生成工具 | PDF tools moved to ClawPDF, added encrypted PDF extraction, and surfaced MCP structured content in agent tool results. |
| 2026-05-016 | 2026-05-28 | openclaw 2026.5.28-beta.4 | 插件化与生态 | Plugin SDK and channel plugins gained typed reply payload hooks and presentation controls for channel-owned replies. |
| 2026-05-005 | 2026-05-31 | openclaw 2026.5.31-beta.4 | 插件化与生态 | Plugins added SecretRef provider integration manifests, shared LLM core packages, SQLite-backed plugin install indexes, and official external Copilot and Tokenjuice packages. |
| 2026-06-076 | 2026-06-02 | openclaw 2026.6.1 | 插件化与生态 | Skill Workshop adds a review-first workflow for turning agent work into reusable skills, with pending PROPOSAL.md files, support files, proposal revision, approval/rejection/quarantine actions, CLI/Gateway review actions, rollback metadata, Control UI navigation, dashboard, today view, file previews, searchable previews, reusable session handoff, and localization. |
| 2026-06-079 | 2026-06-02 | openclaw 2026.6.1 | 插件化与生态 | Tokenjuice and GitHub Copilot agent runtime are externalized as official plugins with npm and ClawHub publish metadata. |
| 2026-06-083 | 2026-06-02 | openclaw 2026.6.1 | 插件化与生态 | Plugins add a SecretRef provider integration manifest contract and shared LLM core packages for provider/plugin reuse. |
| 2026-06-086 | 2026-06-02 | openclaw 2026.6.1 | 插件化与生态 | Core skills index centralizes skills runtime loading, status, filtering, and prompt formatting. |
| 2026-06-065 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 插件化与生态 | ClawHub can install GitHub-backed skills through the resolved install API, using pinned commits, install-policy checks, and success telemetry. |
| 2026-06-045 | 2026-06-17 | openclaw 2026.6.7-beta.1 | 插件化与生态 | Skill Workshop support-file targets now go through guarded lifecycle writes, while ClawHub package publishing/checks stay on the current release path. |
| 2026-06-029 | 2026-06-20 | openclaw 2026.6.10-beta.1 | 插件化与生态 | Zalo is available as an external channel entry, Trello skills declare their curl dependency, stale managed skill links are retargeted, and active providers survive tool discovery. |
| 2026-06-033 | 2026-06-20 | openclaw 2026.6.9 | 插件化与生态 | Official provider packages become first-class standalone npm releases, externally installed channel plugins load at Gateway startup, and StepFun is available from npm and ClawHub. |
| 2026-06-024 | 2026-06-23 | openclaw 2026.6.11-beta.1 | 插件化与生态 | Additional official plugins are externalized cleanly, with bundled plugin icon metadata available to installed clients. |
| 2026-06-011 | 2026-06-30 | openclaw 2026.6.11 | 插件化与生态 | Plugin installation and repair are safer and clearer, with better trust-warning guidance, official plugin icons in ClawHub/catalogs, managed npm plugin update durability, and an official openclaw/openclaw Docker Hub mirror. |
| 2026-06-015 | 2026-06-30 | openclaw 2026.6.11 | 多媒体与生成工具 | Generated images from a remote Codex app-server now arrive as attachments, and completed subagent results return to the active parent run more reliably. |

### DFX

| ID | 时间 | Release | 二级分类 | 原始变更说明 |
| --- | --- | --- | --- | --- |
| 2026-01-051 | 2026-01-21 | clawdbot 2026.1.21 | 性能/可靠性与可观测性 | Added cache TTL pruning and auth-aware cache defaults to reduce cold-request token spend. |
| 2026-01-052 | 2026-01-21 | clawdbot 2026.1.21 | 安全/权限与信任边界 | Added elevated exec approval modes, local/gateway/node targeting, wildcard agent allowlists, and stricter allowlist controls. |
| 2026-01-055 | 2026-01-21 | clawdbot 2026.1.21 | Gateway/Node/远程连接 | Added gateway/node service command restructuring and gateway reachability probes. |
| 2026-01-057 | 2026-01-21 | clawdbot 2026.1.21 | Gateway/Node/远程连接 | Added exec-style node execution with PATH status/describe support. |
| 2026-01-059 | 2026-01-21 | clawdbot 2026.1.21 | 性能/可靠性与可观测性 | Added diagnostics for cache tracing. |
| 2026-01-060 | 2026-01-21 | clawdbot 2026.1.21 | 安全/权限与信任边界 | Made Control UI reject insecure HTTP without device identity by default. |
| 2026-01-061 | 2026-01-21 | clawdbot 2026.1.21 | 性能/可靠性与可观测性 | Changed envelope and system event timestamps to host-local time by default. |
| 2026-01-034 | 2026-01-23 | Clawdbot 2026.1.23 | Gateway/Node/远程连接 | Added a gateway /tools/invoke HTTP endpoint for direct tool calls with auth and tool policy enforcement. |
| 2026-01-036 | 2026-01-23 | Clawdbot 2026.1.23 | CLI/配置/运维与部署 | Added Fly.io deployment support. |
| 2026-01-038 | 2026-01-23 | Clawdbot 2026.1.23 | 安全/权限与信任边界 | Added per-group tool allow/deny policies across built-in and plugin channels. |
| 2026-01-040 | 2026-01-23 | Clawdbot 2026.1.23 | 性能/可靠性与可观测性 | Added CLI system events, heartbeat controls, live auth probes for model status, and default gateway restart after updates. |
| 2026-01-041 | 2026-01-23 | Clawdbot 2026.1.23 | Gateway/Node/远程连接 | Added node-host browser proxy auto-routing for remote gateways. |
| 2026-01-027 | 2026-01-24 | Clawdbot 2026.1.24 | 安全/权限与信任边界 | Added in-chat exec approval via /approve across all channels, including plugins. |
| 2026-01-031 | 2026-01-24 | Clawdbot 2026.1.24 | CLI/配置/运维与部署 | Exposed safe partial config.patch updates through the gateway tool with restart signaling. |
| 2026-01-032 | 2026-01-24 | Clawdbot 2026.1.24 | 性能/可靠性与可观测性 | Added targeted diagnostic flags for config/env-driven debug logs. |
| 2026-01-023 | 2026-01-28 | Introducing OpenClaw | 安全/权限与信任边界 | Shipped a broad security hardening push alongside the rebrand. |
| 2026-01-008 | 2026-01-29 | openclaw 2026.1.29 | 安全/权限与信任边界 | Added beta security/onboarding warnings, legacy config/state path migration, and stronger gateway exposure/auth guidance. |
| 2026-01-009 | 2026-01-29 | openclaw 2026.1.29 | 安全/权限与信任边界 | Removed unauthenticated gateway mode: gateway access now requires token/password unless Tailscale Serve identity is used. |
| 2026-01-010 | 2026-01-29 | openclaw 2026.1.29 | 安全/权限与信任边界 | Added Control UI device-auth bypass auditing and fail-closed gateway auth behavior. |
| 2026-01-011 | 2026-01-29 | openclaw 2026.1.29 | Gateway/Node/远程连接 | Routed browser control and browser.request through gateway/node proxy paths for remote setups. |
| 2026-01-017 | 2026-01-29 | openclaw 2026.1.29 | 安全/权限与信任边界 | Hardened voice-call, Tailscale Serve, mDNS discovery, URL fetch DNS pinning, hook content wrapping, and remote host handling. |
| 2026-01-001 | 2026-01-30 | openclaw 2026.1.30 | CLI/配置/运维与部署 | Added CLI shell completions for Zsh, Bash, PowerShell, and Fish, with auto-setup during postinstall/onboarding. |
| 2026-01-006 | 2026-01-30 | openclaw 2026.1.30 | 安全/权限与信任边界 | Restricted local path extraction in the media parser to prevent LFI. |
| 2026-02-061 | 2026-02-01 | openclaw 2026.2.1 | 安全/权限与信任边界 | Agents add system prompt safety guardrails. |
| 2026-02-065 | 2026-02-01 | openclaw 2026.2.1 | 安全/权限与信任边界 | Gateway TLS listeners now require TLS 1.3 minimum. |
| 2026-02-067 | 2026-02-01 | openclaw 2026.2.1 | 安全/权限与信任边界 | Security hardening covers plugin/hook install path validation, Chrome extension relay CDP sessions, WhatsApp accountId traversal prevention, MEDIA path LFI prevention, message-tool sandbox path validation, host exec environment blocking, web tool content wrapping, and Twitch allowFrom gating. |
| 2026-02-056 | 2026-02-03 | openclaw 2026.2.2 | 安全/权限与信任边界 | Security adds a healthcheck skill and bootstrap audit guidance. |
| 2026-02-058 | 2026-02-03 | openclaw 2026.2.2 | 安全/权限与信任边界 | Security hardening adds gateway approval requirements, stricter Matrix and Slack access gating, shared-secret gateway connect validation, SSRF checks for skill installer downloads, Windows exec allowlist hardening, and safer media-understanding fetches. |
| 2026-02-051 | 2026-02-04 | openclaw 2026.2.3 | CLI/配置/运维与部署 | Shell completion can migrate slow dynamic patterns to cached files and adds completion health checks to doctor, update, and onboard. |
| 2026-02-052 | 2026-02-04 | openclaw 2026.2.3 | 安全/权限与信任边界 | Security keeps untrusted Slack/Discord channel metadata out of system prompts, enforces sandboxed media paths for attachments, requires explicit credentials for gateway URL overrides, and gates whatsapp_login to owner senders by default. |
| 2026-02-040 | 2026-02-06 | OpenClaw Partners with VirusTotal for Skill Security | 安全/权限与信任边界 | ClawHub skills gain automatic VirusTotal security scanning with Code Insight analysis, daily rescans, and approval, warning, and block statuses. |
| 2026-02-046 | 2026-02-06 | openclaw 2026.2.6 | 安全/权限与信任边界 | Security strengthens Gateway canvas/A2UI asset auth, skill/plugin code safety scanning, credential redaction, and sandboxed media/tool attachment paths. |
| 2026-02-032 | 2026-02-08 | openclaw 2026.2.9 | Gateway/Node/远程连接 | iOS alpha node onboarding adds a node app and setup-code flow. |
| 2026-02-033 | 2026-02-08 | openclaw 2026.2.9 | Gateway/Node/远程连接 | Device pairing and phone-control plugins add Telegram /pair plus iOS and Android node controls. |
| 2026-02-037 | 2026-02-08 | openclaw 2026.2.9 | CLI/配置/运维与部署 | OPENCLAW_HOME allows overriding the home directory used by internal path resolution. |
| 2026-02-029 | 2026-02-12 | openclaw 2026.2.12 | CLI/配置/运维与部署 | The CLI adds openclaw logs --local-time for local-timezone log timestamps. |
| 2026-02-031 | 2026-02-12 | openclaw 2026.2.12 | 安全/权限与信任边界 | Hooks now reject POST /hooks/agent sessionKey overrides by default, with explicit configuration for fixed hook context or legacy request-provided session keys. |
| 2026-02-025 | 2026-02-13 | openclaw 2026.2.13 | 安全/权限与信任边界 | Slack outbound routing gains thread-ownership gating through message_sending hooks with @-mention bypass tracking and cancel/modify behavior. |
| 2026-02-028 | 2026-02-13 | openclaw 2026.2.13 | 性能/可靠性与可观测性 | Agent prompt diagnostics now report message counts, prompt sizes, provider/model, and session file details before embedded runner prompt calls. |
| 2026-02-021 | 2026-02-14 | openclaw 2026.2.14 | 安全/权限与信任边界 | Sandbox browser container bind mounts can be configured separately from exec containers. |
| 2026-02-022 | 2026-02-14 | openclaw 2026.2.14 | 安全/权限与信任边界 | Slack and Discord add dmPolicy and allowFrom aliases for DM access control while preserving legacy keys and doctor migration support. |
| 2026-02-001 | 2026-02-26 | openclaw 2026.2.26 | 安全/权限与信任边界 | External Secrets Management adds a full openclaw secrets workflow for audit, configure, apply, and reload, with runtime snapshot activation, stricter target-path validation, safer migration scrubbing, ref-only auth-profile support, and dedicated docs. |
| 2026-02-006 | 2026-02-26 | openclaw 2026.2.26 | 安全/权限与信任边界 | Gemini CLI OAuth onboarding adds an explicit account-risk warning and confirmation gate. |
| 2026-02-007 | 2026-02-26 | openclaw 2026.2.26 | Gateway/Node/远程连接 | Android nodes gain device capability support, device.status and device.info commands, and notifications.list tooling for active device notifications. |
| 2026-02-008 | 2026-02-26 | openclaw 2026.2.26 | 安全/权限与信任边界 | Security hardening covers structured host=node command approvals, plugin channel HTTP auth path normalization, sandbox symlink/path alias boundary checks, and stricter workspace filesystem escape prevention. |
| 2026-02-009 | 2026-02-26 | openclaw 2026.2.26 | Gateway/Node/远程连接 | Platform exposure and gateway setup improve with non-loopback bind warnings, Control UI allowed-origin seeding, Docker/GCP onboarding improvements, gateway auth-mode CLI parity, TLS-aware daemon status probes, and safer Podman loopback defaults. |
| 2026-02-011 | 2026-02-26 | openclaw 2026.2.26 | 安全/权限与信任边界 | Browser and extension relay behavior is hardened around challenge handshakes, relay startup, fill parsing, extension CORS/auth, reconnects, shutdown, and malformed route decoding. |
| 2026-03-165 | 2026-03-01 | openclaw 2026.3.1 | 性能/可靠性与可观测性 | Added built-in HTTP liveness/readiness endpoints for Docker and Kubernetes health checks. |
| 2026-03-166 | 2026-03-01 | openclaw 2026.3.1 | Gateway/Node/远程连接 | Added Android node tools for camera listing, device permissions, device health, and notification actions. |
| 2026-03-169 | 2026-03-01 | openclaw 2026.3.1 | CLI/配置/运维与部署 | Added openclaw config file to print the active config path. |
| 2026-03-181 | 2026-03-01 | openclaw 2026.3.1 | Gateway/Node/远程连接 | Added broader Android node parity for notifications, photos, contacts, calendar, and motion capabilities. |
| 2026-03-148 | 2026-03-02 | openclaw 2026.3.2 | 安全/权限与信任边界 | Expanded SecretRef support across supported user-supplied credential surfaces with planning, apply, audit, onboarding UX, and fail-fast active-surface resolution. |
| 2026-03-155 | 2026-03-02 | openclaw 2026.3.2 | CLI/配置/运维与部署 | Added openclaw config validate with --json and detailed invalid-key paths. |
| 2026-03-162 | 2026-03-02 | openclaw 2026.3.2 | CLI/配置/运维与部署 | Added CLI banner tagline controls. |
| 2026-03-135 | 2026-03-07 | openclaw 2026.3.7 | 安全/权限与信任边界 | Added SecretRef support for gateway.auth.token with auth-mode guardrails. |
| 2026-03-136 | 2026-03-07 | openclaw 2026.3.7 | CLI/配置/运维与部署 | Added OPENCLAW_EXTENSIONS for preinstalling bundled extension dependencies into container images. |
| 2026-03-146 | 2026-03-07 | openclaw 2026.3.7 | 安全/权限与信任边界 | Added hook prompt-injection policy controls for plugins. |
| 2026-03-147 | 2026-03-07 | openclaw 2026.3.7 | 安全/权限与信任边界 | Made gateway auth mode explicit when both token and password are configured. |
| 2026-03-110 | 2026-03-08 | openclaw 2026.3.8 | CLI/配置/运维与部署 | Added openclaw backup create and openclaw backup verify for local state archives, including config-only and workspace-exclusion modes. |
| 2026-03-113 | 2026-03-08 | openclaw 2026.3.8 | CLI/配置/运维与部署 | Included short git commit hashes in openclaw --version output when available. |
| 2026-03-117 | 2026-03-08 | openclaw 2026.3.8 | Gateway/Node/远程连接 | Added browser.relayBindHost for Chrome extension relay binding in WSL2 and cross-namespace setups. |
| 2026-03-123 | 2026-03-08 | openclaw 2026.3.8 | 安全/权限与信任边界 | Added Podman SELinux bind-mount relabel support and setup hardening. |
| 2026-03-125 | 2026-03-08 | openclaw 2026.3.8 | 性能/可靠性与可观测性 | Reduced Docker runtime image size by pruning dev dependencies and build metadata. |
| 2026-03-126 | 2026-03-08 | openclaw 2026.3.8 | CLI/配置/运维与部署 | Added Dockerfile multi-stage build support with slim runtime variant. |
| 2026-03-127 | 2026-03-08 | openclaw 2026.3.8 | 安全/权限与信任边界 | Hardened browser SSRF redirects, Teams authorization, system.run script approvals, and skill download install paths. |
| 2026-03-106 | 2026-03-11 | openclaw 2026.3.11 | Gateway/Node/远程连接 | Improved macOS remote gateway onboarding for shared auth-token discovery and explanation. |
| 2026-03-109 | 2026-03-11 | openclaw 2026.3.11 | Gateway/Node/远程连接 | Added narrow node pending-work queue primitives for dormant-node work delivery. |
| 2026-03-096 | 2026-03-12 | openclaw 2026.3.12 | CLI/配置/运维与部署 | Added starter Kubernetes install path with raw manifests, Kind setup, and deployment docs. |
| 2026-03-091 | 2026-03-13 | openclaw 2026.3.13 | CLI/配置/运维与部署 | Added OPENCLAW_TZ for Docker gateway and CLI timezone pinning. |
| 2026-03-064 | 2026-03-22 | openclaw 2026.3.22 | 安全/权限与信任边界 | Added pluggable sandbox backends, including OpenShell mirror and remote workspace modes. |
| 2026-03-065 | 2026-03-22 | openclaw 2026.3.22 | 安全/权限与信任边界 | Added a core SSH sandbox backend with secret-backed key, certificate, and known_hosts inputs. |
| 2026-03-082 | 2026-03-22 | openclaw 2026.3.22 | CLI/配置/运维与部署 | Expanded config set with SecretRef/provider builder modes, JSON/batch assignment, dry-run validation, and structured JSON output. |
| 2026-03-085 | 2026-03-22 | openclaw 2026.3.22 | 安全/权限与信任边界 | Hardened workspace hooks, remote marketplace manifests, SecretRef diagnostics, and gateway URL allowlist semantics. |
| 2026-03-053 | 2026-03-24 | openclaw 2026.3.24 | 性能/可靠性与可观测性 | Improved CLI container support, install guidance, outbound media access, Node runtime handling, and update prechecks as a visible platform reliability theme. |
| 2026-03-039 | 2026-03-28 | openclaw 2026.3.28 | 安全/权限与信任边界 | Added async requireApproval for plugin before_tool_call hooks, allowing tool execution to pause for user approval across UI and chat channels. |
| 2026-03-041 | 2026-03-28 | openclaw 2026.3.28 | 安全/权限与信任边界 | Enabled apply_patch by default for OpenAI and OpenAI Codex models, aligned to sandbox write permissions. |
| 2026-03-044 | 2026-03-28 | openclaw 2026.3.28 | CLI/配置/运维与部署 | Simplified Podman container setup around the current rootless user and documented the host-CLI openclaw --container workflow. |
| 2026-03-048 | 2026-03-28 | openclaw 2026.3.28 | CLI/配置/运维与部署 | Added openclaw config schema for printing generated JSON schema. |
| 2026-03-014 | 2026-03-30 | openclaw 2026.3.31 | 安全/权限与信任边界 | Added a default-off ACPX plugin-tools MCP bridge configuration with documented trust boundaries. |
| 2026-03-026 | 2026-03-30 | openclaw 2026.3.31 | 安全/权限与信任边界 | Hardened Nostr inbound DMs by verifying event signatures before pairing or sender-authorization side effects. |
| 2026-03-030 | 2026-03-30 | openclaw 2026.3.31 | 性能/可靠性与可观测性 | Added structured TTS provider diagnostics and fallback-attempt analytics. |
| 2026-03-032 | 2026-03-30 | openclaw 2026.3.31 | 安全/权限与信任边界 | Made per-agent tools.exec defaults effective when no inline directive or session override is present. |
| 2026-03-033 | 2026-03-30 | openclaw 2026.3.31 | 安全/权限与信任边界 | Hardened sandboxed SSH subprocess environments and guarded remote fetch paths for marketplace downloads and Ollama requests. |
| 2026-03-009 | 2026-03-31 | openclaw 2026.4.1 | 安全/权限与信任边界 | Added openclaw cron --tools for per-job tool allowlists. |
| 2026-04-125 | 2026-04-01 | openclaw 2026.4.2 | 安全/权限与信任边界 | Gateway/node host exec defaults moved to no-prompt YOLO mode with aligned approval-file fallbacks and doctor reporting. |
| 2026-04-131 | 2026-04-01 | openclaw 2026.4.2 | 安全/权限与信任边界 | Exec approvals can auto-enable DM-first native chat approvals when supported channels can infer approvers from existing owner config. |
| 2026-04-120 | 2026-04-05 | openclaw 2026.4.5 | 性能/可靠性与可观测性 | Prompt caching became more reusable across transport fallback, MCP tool ordering, compaction, embedded image history, prompt fingerprints, and status diagnostics. |
| 2026-04-100 | 2026-04-08 | openclaw 2026.4.9 | 性能/可靠性与可观测性 | QA/lab added character-vibes evaluation reports with model selection and parallel runs. |
| 2026-04-095 | 2026-04-10 | openclaw 2026.4.10 | 性能/可靠性与可观测性 | Matrix live QA gained a disposable homeserver and transport coverage for threading, reactions, restart, and allowlist behavior. |
| 2026-04-080 | 2026-04-12 | openclaw 2026.4.12 | CLI/配置/运维与部署 | `openclaw exec-policy` added local show, preset, and set commands for synchronizing exec approval config with local approval files. |
| 2026-04-086 | 2026-04-12 | openclaw 2026.4.12 | 安全/权限与信任边界 | Plugin loading narrowed CLI/provider/channel activation to manifest-declared needs, preserving trust boundaries while avoiding unrelated runtime loads. |
| 2026-04-061 | 2026-04-20 | openclaw 2026.4.20 | 安全/权限与信任边界 | The setup wizard received a clearer security disclaimer, loading state for model catalog startup, and improved API-key prompts. |
| 2026-04-064 | 2026-04-20 | openclaw 2026.4.20 | CLI/配置/运维与部署 | Cron split runtime state into `jobs-state.json` so git-tracked job definitions stay stable. |
| 2026-04-025 | 2026-04-26 | OpenClaw 2026.4.25 | 性能/可靠性与可观测性 | OpenTelemetry coverage expanded across model calls, token usage, tool loops, harness runs, exec processes, outbound delivery, context assembly, and memory pressure. |
| 2026-04-027 | 2026-04-26 | OpenClaw 2026.4.25 | CLI/配置/运维与部署 | Install/update hardening covered Windows, macOS, Linux, Docker, bundled plugin runtime deps, Node service restarts, LaunchAgent token rotation, and mixed-version gateway verification. |
| 2026-04-021 | 2026-04-27 | OpenClaw 2026.4.26 | 安全/权限与信任边界 | Matrix gained a CLI encryption setup flow with bootstrap recovery and verification status reporting. |
| 2026-04-022 | 2026-04-27 | OpenClaw 2026.4.26 | CLI/配置/运维与部署 | A bundled Claude/Hermes migration flow can preview, back up, and import instructions, MCP servers, skills, command prompts, model/provider hints, memory/plugin hints, and supported credentials. |
| 2026-04-010 | 2026-04-28 | openclaw 2026.4.27 | 安全/权限与信任边界 | Codex Computer Use setup shipped with status/install commands, marketplace discovery, optional auto-install, and fail-closed MCP checks before Codex-mode desktop-control turns. |
| 2026-04-014 | 2026-04-28 | openclaw 2026.4.27 | 安全/权限与信任边界 | OpenClaw added opt-in operator-managed outbound proxy routing with strict forward-proxy validation and Gateway bypass rules. |
| 2026-04-017 | 2026-04-28 | openclaw 2026.4.27 | 安全/权限与信任边界 | Docker sandboxes gained opt-in GPU passthrough for local GPU workloads. |
| 2026-04-001 | 2026-04-29 | How OpenClaw Got Safer in Public | 安全/权限与信任边界 | OpenClaw tightened its public security posture with a clearer SECURITY.md trust model, stricter auth/sandbox/owner-scope handling, reduced core attack surface through plugin extraction, stronger release gates, broader CI coverage, observability upgrades, and safer secret handling. |
| 2026-04-005 | 2026-04-29 | openclaw 2026.4.29 | 安全/权限与信任边界 | Security and operations added OpenGrep scanning, sharper GHSA triage policy, safer exec/pairing/owner-scope handling, Docker onboarding automation, and opt-in IPv6 ULA web-fetch support for trusted proxy stacks. |
| 2026-04-007 | 2026-04-29 | openclaw 2026.4.29 | 性能/可靠性与可观测性 | Gateway diagnostics added an opt-in startup timeline for lifecycle and plugin-load phases. |
| 2026-05-071 | 2026-05-02 | openclaw 2026.5.2 | 性能/可靠性与可观测性 | Gateway and agent hot paths became leaner across startup, session listing, task maintenance, prompt prep, plugin loading, tool descriptor planning, filesystem guards, and large runtime configs. |
| 2026-05-079 | 2026-05-02 | openclaw 2026.5.2 | 安全/权限与信任边界 | Gateway config `$include` can read files from operator-approved `OPENCLAW_INCLUDE_ROOTS` while preserving default config-directory confinement. |
| 2026-05-081 | 2026-05-02 | openclaw 2026.5.2 | CLI/配置/运维与部署 | CLI added `openclaw proxy validate` so operators can verify effective proxy configuration and destination policy before deployment. |
| 2026-05-066 | 2026-05-03 | OpenClaw 2026.5.3 | 性能/可靠性与可观测性 | Gateway startup and Control UI hot paths became faster by lazy-loading plugin/runtime discovery, cron, schema, shutdown, sessions, and model metadata work only when needed. |
| 2026-05-069 | 2026-05-03 | OpenClaw 2026.5.3 | 安全/权限与信任边界 | Exec approvals added a tree-sitter-backed shell command explainer for future approval and command-review surfaces. |
| 2026-05-062 | 2026-05-04 | openclaw 2026.5.4 | 性能/可靠性与可观测性 | Gateway startup moved model-catalog helpers, run-session lookup, QR pairing, and memory schema work out of hot import paths. |
| 2026-05-053 | 2026-05-06 | openclaw 2026.5.7 | 性能/可靠性与可观测性 | Plugin publishing, cron JSON status, channels CLI, agent permissions, Telegram, WhatsApp, and model-provider workflows received broad platform reliability improvements. |
| 2026-05-050 | 2026-05-10 | openclaw 2026.5.10-beta.3 | 性能/可靠性与可观测性 | Messaging, voice, Gateway, and Codex workflows gained stricter builds, smarter Slack and Telegram handling, improved context/model behavior, and stronger auth and runtime reliability. |
| 2026-05-049 | 2026-05-13 | openclaw 2026.5.12-beta.8 | 安全/权限与信任边界 | Core installs became lighter through plugin extraction, with persisted auto-scroll selection, ACP fallback backends, stronger Telegram reliability, and hardened sandbox, config, auth, and update boundaries. |
| 2026-05-045 | 2026-05-16 | openclaw 2026.5.16-beta.4 | 安全/权限与信任边界 | Security audit suppressions, smarter subagent review handoffs, new music-generation providers, xAI OAuth login, cron run waiting, Control UI quota visibility, Mac remote setup, and chat state recovery were added or expanded. |
| 2026-05-044 | 2026-05-19 | openclaw 2026.5.18 | 性能/可靠性与可观测性 | Stable rollup delivered UI polish, stronger realtime voice and mobile flows, and broader reliability gains across Telegram, Discord, Codex, plugins, models, Gateway, QA, security, updates, and session recovery. |
| 2026-05-040 | 2026-05-20 | openclaw 2026.5.20 | 安全/权限与信任边界 | Approval and policy handling expanded with stronger CLI checks and clearer doctor warnings. |
| 2026-05-042 | 2026-05-20 | openclaw 2026.5.20 | 性能/可靠性与可观测性 | Cron, CLI, Gateway, provider, app, and build workflows received broad reliability hardening as a platform theme. |
| 2026-05-035 | 2026-05-23 | openclaw 2026.5.24-beta.1 | 性能/可靠性与可观测性 | Gateway startup and hot paths now cache stable install-record, channel-catalog, bundled-channel, and Telegram session-store metadata while lazy-loading unused handler trees and ACPX runtime work. |
| 2026-05-018 | 2026-05-27 | OpenClaw Is Getting Faster, Smaller, and Easier to Trust | 性能/可靠性与可观测性 | OpenClaw reduced agent turn latency, memory use, and published package size by extracting optional plugins and pruning heavy dependencies from core. |
| 2026-05-019 | 2026-05-27 | openclaw 2026.5.27 | 安全/权限与信任边界 | Security and content boundaries were strengthened: group prompt text stays out of system prompts, repeated-dot hostnames are normalized, unsafe command wrappers and Node env overrides are blocked, no-auth Tailscale exposure is rejected, and node/device-role approvals require admin authority. |
| 2026-05-020 | 2026-05-27 | openclaw 2026.5.27 | 性能/可靠性与可观测性 | Gateway and reply hot paths became faster by reducing repeated session reads, plugin metadata fingerprints, auth env snapshots, auto-enabled plugin config, tool-search catalog work, and stable metadata rediscovery. |
| 2026-05-029 | 2026-05-27 | openclaw 2026.5.26 | 安全/权限与信任边界 | Browser snapshots, fetched file text, system events, ClickClack allowlists, device tokens, and serialized tool-call text received stronger content and dispatch boundaries. |
| 2026-05-031 | 2026-05-27 | openclaw 2026.5.26 | 性能/可靠性与可观测性 | Diagnostics added gateway secret-prep traces, skill/tool usage classification, model stream progress, OpenTelemetry LLM content spans, and alertable telemetry for blocked tools, failover, stale sessions, liveness, oversized payloads, and webhook ingress. |
| 2026-05-017 | 2026-05-28 | openclaw 2026.5.28-beta.4 | 性能/可靠性与可观测性 | Gateway, plugin, and release-split external plugin hot paths reduced repeated install-record, config, catalog, session-store, manifest, token, and viewer asset work while preserving cache correctness. |
| 2026-05-011 | 2026-05-30 | Safer Than YOLO: Auto Mode for Exec Approvals | 安全/权限与信任边界 | Enterprise host exec guardrails added opt-in auto mode with reviewer-first approvals, human fallback, lower prompt noise, chat-app approval routing, and Codex Guardian-style reviewed access. |
| 2026-05-002 | 2026-05-31 | openclaw 2026.5.31-beta.4 | Gateway/Node/远程连接 | Gateway and channel setup added Tailscale Serve service-name bindings, Communication notification settings, safer agent add flows, and more reliable progress drafts. |
| 2026-05-007 | 2026-05-31 | openclaw 2026.5.31-beta.4 | 性能/可靠性与可观测性 | iMessage monitor state, inbound queues, and plugin install ledgers moved toward SQLite-backed state for better restart recovery and less filesystem scanning. |
| 2026-05-009 | 2026-05-31 | openclaw 2026.5.31-beta.4 | 性能/可靠性与可观测性 | Agents and CLI-backed runtimes recover more cleanly from interrupted tool calls, stale session bindings, compaction handoffs, and media delivery retries. |
| 2026-05-010 | 2026-05-31 | OpenClaw Collaborates with NVIDIA for Stronger Agent Skill Security | 安全/权限与信任边界 | ClawHub skill security added pre-publish verification, NVIDIA Skill Cards, SkillSpector risk analysis, and a public Hugging Face dataset of skill scan outcomes. |
| 2026-06-084 | 2026-06-02 | openclaw 2026.6.1 | 性能/可靠性与可观测性 | Plugin install indexes, iMessage monitor state, and inbound queues move toward SQLite-backed state for more durable reload and restart behavior. |
| 2026-06-070 | 2026-06-03 | openclaw 2026.6.2-beta.1 | 安全/权限与信任边界 | Plugin and skill installs use an operator install policy instead of the old dangerous-code scanner path, with clearer doctor, CLI, ClawHub, troubleshooting, package, archive, source, upload, and marketplace surfaces. |
| 2026-06-071 | 2026-06-03 | openclaw 2026.6.2-beta.1 | 安全/权限与信任边界 | Policy and config recovery now reject corrupt shell snapshots, unsupported policy keys, unsafe exec approval precheck environments, malformed script limits, and suspicious gateway startup configs while adding data-handling conformance checks. |
| 2026-06-074 | 2026-06-03 | openclaw 2026.6.2-beta.1 | CLI/配置/运维与部署 | Windows node installer publishing is promoted with verified Windows release asset links. |
| 2026-06-062 | 2026-06-08 | openclaw 2026.6.5-beta.6 | 安全/权限与信任边界 | Agent, tool, and provider loops are stricter around MCP lease timestamps, prompt-cache tool names, local tool catalogs, unreadable dynamic tools, owner-only HTTP tools, and provider catalog metadata. |
| 2026-06-063 | 2026-06-08 | openclaw 2026.6.5-beta.6 | Gateway/Node/远程连接 | macOS node mode no longer silently reconnects away from a healthy direct Gateway session. |
| 2026-06-064 | 2026-06-08 | openclaw 2026.6.5-beta.6 | CLI/配置/运维与部署 | Cron legacy JSON stores migrate during doctor preflight, service env placeholders no longer mask state-dir secrets, WhatsApp startup waits are bounded, and disabled WhatsApp accounts tear down on config reload. |
| 2026-06-069 | 2026-06-08 | openclaw 2026.6.5-beta.6 | CLI/配置/运维与部署 | Release trains switch to YYYY.M.PATCH monthly patch numbering. |
| 2026-06-051 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 性能/可靠性与可观测性 | Trusted diagnostics channels can capture tool input/output content, first-assistant-event traces are available, and slow initial replies produce warnings. |
| 2026-06-054 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | 安全/权限与信任边界 | Security boundaries tighten across transcripts, sandbox binds, host environment inheritance, MCP stdio, Codex HTTP access, native search policy, elevated senders, loopback tools, Discord moderation, Teams group actions, and exec approval timeout handling. |
| 2026-06-055 | 2026-06-09 | OpenClaw 2026.6.6-beta.1 | Gateway/Node/远程连接 | Browser and MCP connectivity add existing-session CDP support, discovered WebSocket validation, default-profile cdpUrl handling, safer browser-output boundaries, Streamable HTTP loopback transport, OAuth/SSE authorization fixes, and broader schema compatibility. |
| 2026-06-044 | 2026-06-17 | openclaw 2026.6.7-beta.1 | CLI/配置/运维与部署 | Operator workflows expose clearer state through SQLite-backed cron status, disabled heartbeat retries, Linux service updates, and external-plugin diagnosis. |
| 2026-06-027 | 2026-06-20 | openclaw 2026.6.10-beta.1 | 安全/权限与信任边界 | Codex app-server SecretRefs, thread context, bounded turn text, routed approval context, and typed SDK approval/session helpers make Codex and approval flows more predictable. |
| 2026-06-030 | 2026-06-20 | openclaw 2026.6.10-beta.1 | 性能/可靠性与可观测性 | Gateway probes distinguish reachable-but-errored from unreachable, plugin methods authorize through the attached registry, session status exposes duration, and provider pricing streams are bounded. |
| 2026-06-037 | 2026-06-20 | openclaw 2026.6.9 | 性能/可靠性与可观测性 | OpenTelemetry log export is added, and remote-node execution is exposed to Codex when a node is connected. |
| 2026-06-023 | 2026-06-23 | openclaw 2026.6.11-beta.1 | CLI/配置/运维与部署 | openclaw agent --message-file and the Raft CLI wake bridge add file-driven and remote wake-up operator workflows. |
| 2026-06-026 | 2026-06-23 | openclaw 2026.6.11-beta.1 | 性能/可靠性与可观测性 | Gateway and plugin tooling add channel identity hook context and per-agent usage-cost reporting. |
| 2026-06-019 | 2026-06-25 | openclaw 2026.6.10 | 安全/权限与信任边界 | Approval-sensitive Gateway and plugin tools stay protected when connected extensions change, preserving trusted tool policy enforcement. |
| 2026-06-020 | 2026-06-25 | openclaw 2026.6.10 | 安全/权限与信任边界 | Authenticated package-source tokens are no longer sent to redirected downloads on another origin. |
| 2026-06-010 | 2026-06-30 | openclaw 2026.6.11 | 性能/可靠性与可观测性 | Sessions, compaction, QMD-backed memory, Tool Search, Matrix recovery, tool policies, and approvals retain state more consistently across reconnects, stops, retries, and trust boundaries. |
| 2026-06-013 | 2026-06-30 | openclaw 2026.6.11 | 性能/可靠性与可观测性 | Long-context, tool-heavy agent sessions keep prompt-cache reuse steadier and reduce avoidable CPU, memory, and filesystem overhead. |
| 2026-06-014 | 2026-06-30 | openclaw 2026.6.11 | 安全/权限与信任边界 | Trusted OpenClaw package sources now reject lookalike sibling paths, tightening package-source trust boundaries. |
| 2026-07-007 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 安全/权限与信任边界 | Scoped conversation capability profiles prepare per-conversation tool and access boundaries while preserving the existing default profile. |
| 2026-07-008 | 2026-07-05 | openclaw 2026.7.1-beta.2 | CLI/配置/运维与部署 | The macOS app can install and start its local Gateway automatically, reducing first-run setup. |
| 2026-07-012 | 2026-07-05 | openclaw 2026.7.1-beta.2 | CLI/配置/运维与部署 | CLI and node workflows add node context-path support, device-approval recovery guidance, soft-resume CLI sessions when prompt metadata changes, and clearer plugin install exit diagnostics. |
| 2026-07-014 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 性能/可靠性与可观测性 | Doctor diagnostics now surface auth-profile, workspace, device-pairing, channel-plugin, memory-provider, systemd exhaustion, and Windows LAN firewall findings. |
| 2026-07-016 | 2026-07-05 | openclaw 2026.7.1-beta.2 | 性能/可靠性与可观测性 | Reliability work is grouped around product-visible durability for Telegram delivery, agent and context recovery, provider/network safety, channel routing, cron correctness, Windows execution, mobile/UI stability, plugin health, runtime process safety, Node runtime compatibility, and QQBot media delivery. |

# 复用调查

日期：2026-10-30。每项区分源码、说明和实测。

| 能力 | 已查来源 | 复用决定与证据边界 |
| --- | --- | --- |
| 桌面 UI | moeru-ai/airi | 保留 Electron、Vue、现有设置与聊天页。原版首次引导已运行 |
| 3D | AIRI stage-ui-three | 已有 VRM、VRMA、表情、嘴型和骨骼点击区域。写实效果未实测 |
| 模型服务 | AIRI provider-inference | 已有 Ollama 和 OpenAI 兼容接入。优先使用现有适配器 |
| 中文识别 | AIRI sherpaw-transcription | 已登记 Paraformer 与 X-ASR 中英文模型。权重许可和语音效果待逐项核查 |
| 语音合成 | AIRI Kokoro、local-audio | Kokoro 有实际 worker。App Local Speech 页面仍是 WIP，不能宣称中文开箱可用 |
| 原生语音备选 | k2-fsa/sherpa-onnx | 官方代码 Apache-2.0。仅备选，未安装整套方案，模型许可另查 |
| 本地推理 | ggml-org/llama.cpp | Linux 官方 b12000 二进制完成 CPU 中文 API 测试，未整合进安装包 |
| 桌面伴侣备选 | jofizcd/Soul-of-Waifu | 搜索命中并读 README。其记忆、VRM 与桌面能力仍是上游说明，未实测或复制代码 |
| 原计划备选 | Open-LLM-VTuber/Open-LLM-VTuber | README 仍以 Live2D 为主，且 v2 在规划。不以换底座牺牲第一版 3D |
| 写实素材工具 | makehumancommunity/makehuman | 官方仓库与安装说明已查。具体资产许可、成年形象和导出链路仍待验证 |
| 写实素材工具备选 | animate1978/MB-Lab | 仓库已归档。暂不采用，不把生成角色算成已取得合法成品素材 |

本项目不把所有候选项目拼装进来。第一步先完成 AIRI 原版聊天与 Windows 打包闭环。
下载上游内置模型是运行原版的验证步骤，不代表用户认可外观，也不代表本产品通过素材分发审查。

## 来源

- https://github.com/moeru-ai/airi
- https://github.com/ggml-org/llama.cpp
- https://github.com/k2-fsa/sherpa-onnx
- https://github.com/jofizcd/Soul-of-Waifu
- https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
- https://github.com/makehumancommunity/makehuman
- https://github.com/animate1978/MB-Lab

# Windows AI 陪伴程序

当前阶段：M0，部分完成，尚未通过运行门槛。

本仓库目前保存需求约束、选型调查和验证记录。完整 AIRI 源码尚未检出。
没有可运行应用、真实 UI 截图或 EXE。没有连接用户 Windows。

- [项目进度](docs/status.md)
- [技术决策](docs/decisions.md)
- [M0 验证记录](docs/verification/m0-2026-10-28.md)
- [Windows 构建路线](docs/verification/windows-build.md)
- [内容包草案](docs/content-packs.md)

## 正式代码与协作

唯一工作仓库：`/workspace/airi`。当前是本地引导仓库，尚未绑定用户远程仓库。
上游只读来源：`https://github.com/moeru-ai/airi`。
上游审查提交：`dfd9453beaab3af43a40f9bdacebdcb0d51f2723`。
此提交仅用于固定调查证据，尚未选为通过验证的开发底座。

每次开始先执行 `git status --short --branch`，再阅读 `docs/status.md`。
切换环境前提交工作并同步同一个用户远程仓库。不要覆盖另一端的改动。
网络恢复后，在本仓库获取上游历史，从固定提交建立开发分支。
保留当前引导分支，逐项迁入本项目文档，保留上游 README 和目录结构。
不要把证据快照复制成应用源码，也不要在不完整源码上安装依赖。

## 运行与构建

当前无法运行。前置条件为完整源码、依赖下载和可用构建环境。
上游已核查的入口为 `pnpm dev:tamagotchi` 与 `pnpm -F @proj-airi/stage-tamagotchi build:win`。
实际构建还需要原生依赖和 Godot 资源。完整调查见 Windows 构建路线。
这些命令尚未执行，不能据此标记构建成功。


# Windows 构建路线调查

状态：根据固定提交的 CI 源码整理，尚未执行，不是可用构建产物。

来源：
https://github.com/moeru-ai/airi/blob/dfd9453beaab3af43a40f9bdacebdcb0d51f2723/.github/workflows/release-tamagotchi.yml

## 上游步骤

1. Windows x64 runner 获取完整源码。
2. Node 26.7.0，pnpm 11.24.0。
3. 执行 `pnpm install --frozen-lockfile`。
4. 执行 `pnpm run build:packages`。
5. 安装 .NET 10.0.x、Godot 4.7.1 与导出模板。
6. 在 engines/stage-tamagotchi-godot 导出 Windows Desktop 至 out/win/godot-stage.exe。
7. 执行桌面 build，再执行 electron-builder build --windows --x64 --publish=never。
8. 检查 apps/stage-tamagotchi/dist 中的安装包，记录哈希与日志。

原版命名模板为 AIRI-${version}-windows-${arch}-setup.exe。
上游 extraResources 引用 Godot 导出目录，不能忽略该步骤并宣称完整复现。
上游含原生 Node 模块，Linux 交叉构建是否足够仍需实际验证。
优先 Windows runner。当前没有可用 runner 或用户远程仓库。

## 定制发布前检查

- 保留 MIT 版权声明，完成第三方资源清单。
- 修改卸载删数据行为，并验证用户选择与数据保留。
- 隔离应用 ID、产品数据目录、更新源。禁止定制应用被上游更新覆盖。
- 核查默认摄像头、屏幕采集、主动互动与遥测行为。
- 不使用上游签名密钥、发布凭据或发布目的地。
- 仅生成工件不等于签名、公开发布或 Windows 验收通过。
- 安装包下载完成后，在无 Node/Python 的 Windows 上执行验收。
- 记录 EXE 哈希、Windows 版本、GPU 显存、内存和端到端延迟。

## 2026-10-30 复用路线

完整源码已经包含 release-tamagotchi.yml，可直接复用其手动构建入口。
不复制一份删减工作流。首次测试使用平台 windows、artifacts_only=true、build_only=false。
该组合按上游逻辑生成安装工件并禁用发布。先在隔离 Windows 测试环境中验证。
调用前还需核对 workflow_dispatch 输入及目标提交，不能在上游仓库触发。
目标私有仓库创建被 CreateRepository 权限拒绝，因此尚未触发任何 Windows runner。
当前没有 EXE、Windows 构建日志或安装测试结果。

当前原版配置仍会删除卸载数据，并使用上游更新来源。
原版 M0 工件仅用于无个人记录的隔离测试，不可当成本产品安装包分发。
进入定制打包前必须完成前述数据、应用标识和更新隔离。

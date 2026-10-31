# Blender 制作链路验证

该脚本供开发者使用。最终桌面应用不运行 Python 或 Blender。
复用 MPFB 2.0.18 的 HumanService 和自带游戏骨架，没有复制人物生成逻辑。
源码示例：[create human](https://github.com/makehumancommunity/mpfb2/blob/v2.0.18/script_samples/01_create_a_basic_human.py)、[add rig](https://github.com/makehumancommunity/mpfb2/blob/v2.0.18/script_samples/03_adding_a_default_rig.py)。

## 输入和输出

输入为已核验的 MPFB `src/mpfb` 路径，以及尚不存在的输出目录。
脚本在独立 Blender 进程中注册本地插件，生成默认中性网格和 game_engine 骨架。
输出包括 `.blend`、report.json 及该次运行的扩展副本。
参数均为上游默认值，不能解释为用户已选择的身体或外观。
发现输出目录已存在时直接失败，不覆盖旧模型。

在命令行启动前，将 BLENDER_USER_RESOURCES 指向专用开发缓存，隔离正常 Blender 配置。
Windows 的源码、输出和缓存均使用 `E:\ai` 下的目录。
云端已验证命令如下，Windows 尚未执行：

```bash
BLENDER_USER_RESOURCES=/workspace/tooling/character-authoring/blender-resources \
blender --background --factory-startup --offline-mode --python-exit-code 1 \
  --python scripts/character-authoring/probe-mpfb.py -- \
  --mpfb-source /workspace/tooling/character-authoring/mpfb2-2.0.18/src/mpfb \
  --output /workspace/artifacts/character-authoring/probe-new
```

成功退出码为 0。参数、注册或生成失败时退出码为 1，详情保留在标准输出日志。
取消时停止该 Blender 进程。未完成的目录保留，重试使用新目录。
这不是运行时内容包导入器，不向应用内容包授予脚本执行能力。

该验证没有导出 VRM、烘焙写实材质或验证嘴型。
下一阶段先制作并确认候选外观，再验证导出资产在 AIRI 中的实际效果。

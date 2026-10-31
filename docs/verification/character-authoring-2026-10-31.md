# 角色制作链路验证

执行环境：Linux 云端。日期：2026-10-31。不是用户 Windows 或 E 盘。
用户已确认：成年、成熟优雅、自然真人感。上游 VRM 外观被否决，仅保留技术测试用途。

## 复用来源与许可

| 工具或资产 | 固定版本 | 核验 |
| --- | --- | --- |
| Blender | 本机 4.3.2 | 后台进程启动和保存文件通过 |
| MPFB | v2.0.18 | 源码 GPL-3.0-or-later，随附资产 CC0-1.0 |
| VRM Add-on for Blender | 4.10.3 | 下载并读取 MIT OR GPL-3.0-or-later 声明，导出尚未执行 |

MPFB 的 LICENSE.md 将代码、资产和输出分别说明。外部素材包必须另查。
本次调用其 HumanService.create_human 和 add_builtin_rig，不复制建模或自动绑骨逻辑。

来源：

- https://github.com/makehumancommunity/mpfb2/tree/v2.0.18
- https://github.com/makehumancommunity/mpfb2/blob/v2.0.18/LICENSE.md
- https://github.com/makehumancommunity/mpfb2/blob/v2.0.18/LICENSE.ASSETS.md
- https://github.com/saturday06/VRM-Addon-for-Blender/releases/tag/v4.10.3

下载文件 SHA256：

```text
mpfb2-v2.0.18.tar.gz
2909fdf3de140d7ba13b024f3316e8c9862b312d80b39469dfeaba25af30d1c8
vrm-addon-4.10.3.zip
dcf6d55f3d28de8c0de2f72abcc7fe06b2b300195e6b4da2e9cf476fd59165a2
```

## 实测结果

- 首次注册因 MPFB 日志写入只读主目录失败。
- 改用 Blender 官方 BLENDER_USER_RESOURCES，将所有开发配置定向到专用缓存。
- 第二次成功生成 19158 顶点、18486 面、204 个顶点组和 53 根骨骼。
- 保存约 5.7 MiB 的 mpfb-rig-probe.blend，再次启动 Blender 读取成功。
- 重新打开后检查到 1 个网格、1 个骨架和正确的 Armature 修改器关联。
- 对已存在输出目录再次运行，预期失败且原文件 SHA256 不变。
- Python 语法解析通过。pnpm lint 退出码 0，0 错误、673 个上游警告。

产物：/workspace/artifacts/character-authoring/probe-2026-10-31-r2/mpfb-rig-probe.blend。
结构统计见 character-authoring-2026-10-31.json。
复现命令见 scripts/character-authoring/README.md。
开发工具副本在云端 tooling 目录，未进入产品依赖或 Git 源码。

## 尚未完成

当前是上游默认中性技术底模，不是女友角色设计，也不作为审美候选。
未选择肤色、脸型、发型或衣装，没有正式人物外观预览。
未验证 VRM 导出、写实材质在 AIRI 的表现、嘴型、表情、动作和 Q版。
未生成 Windows 安装包，未连接用户 Blender。
私有仓库准确地址仍返回 404。仅配置本地 origin，没有推送。

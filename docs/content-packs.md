# 内容包规范草案

状态：需求记录，尚未实现或验证。进入 M2 后对接上游扩展点。

包包含 manifest.json、预览图和资源。
清单包含 schemaVersion、id、version、type、name、entry、compatibleCharacters、rigProfile、license、attribution。
不适用字段按类型省略。voice 配置不携带密钥。scene 只预留。

第一版类型：character、expression、motion、outfit、persona。
导入目录或压缩包前检查路径、文件类型、大小、版本和骨骼兼容性。
禁止绝对路径、路径穿越及借助符号链接逃逸。
限制压缩和解压大小。具体上限在实际资源测量后记录。
启用前展示预览与授权信息。不运行包内脚本。

角色 identityId 与外观 appearanceId 分离。
禁用或删除内容包不删除聊天与记忆。
模型只能请求已注册动作或表情语义。未知语义回退为待机或默认。
打断按轮次取消语音和表现，迟到响应不能触发旧动作。
点击区域使用稳定 ID，按角色骨骼或碰撞区域配置。
区域及反馈含义必须由用户确认。

验收：新增一个表情或动作包，无需改聊天核心。
至少一个错误包必须被拒绝，且程序保持可用。
目前全部未执行。


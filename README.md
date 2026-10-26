# 本少的qq机器人功能包

> AstrBot 插件 · **占位版，持续开发中**

本少的 QQ 机器人功能包。围绕 QQ 机器人的日常使用逐步补充能力，当前为占位版本，用于打通插件骨架、加载链路与发版流程。

## 现状

| 项 | 值 |
|---|---|
| 版本 | 0.1.0 |
| 支持平台 | `aiocqhttp`（OneBot v11） |
| AstrBot 版本 | `>=4.29.0` |
| 额外依赖 | 无 |

## 指令

| 指令 | 说明 |
|---|---|
| `/qqsvc` | 查看插件版本与会话标识 |

## 安装

**方式一：从链接安装**（推荐，无需审核）

AstrBot 管理面板 → 插件 → 插件市场 → 右下角 `+` → **从链接安装** → 填入：

```
https://github.com/DanDingBenShao/astrbot_plugin_qq_kit
```

**方式二：手动放入**

把本仓库内容复制到 `AstrBot/data/plugins/astrbot_plugin_qq_kit/`，然后在面板里点「重载」。

**方式三：插件市场**（需 AstrBot Cloud 账号并通过审核）

见 <https://cloud.astrbot.app/publish>。

## 更新

1. 改代码
2. **同时**改两处版本号：`metadata.yaml` 的 `version`、`main.py` 的 `PLUGIN_VERSION`
3. 推到 GitHub
4. 用户在面板点「更新」

版本号是面板判断"有没有新版本"的唯一依据，两处必须一致。

## 开发

```bash
# 无需额外依赖
# 改完代码在面板点「重载」即可，不用重启 AstrBot
```

调试指令可以用 WebUI 的聊天页直接发 `/qqsvc`，不必经过 QQ。

## Roadmap

- [ ] 群消息处理钩子
- [ ] 群管理与白名单联动
- [ ] 外部服务对接
- [ ] 插件自带配置页
- [ ] 消息归档与检索

## 许可证

[MIT](LICENSE)

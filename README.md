# 本少的qq机器人功能包

> AstrBot 插件 · **套件门面 v0.2.0**

本少的 QQ 机器人套件主框架的「壳」：自动探测本机已装的本少系组件插件，`/qqkit` 输出聚合状态页。组件可散装单装，也可全家桶聚合使用；门面自身不做业务逻辑。

## 架构定位

```
┌─ astrbot_plugin_qqmind（判读门+记忆+人设 主体）─┐
qq_kit（门面）── 探测/状态页 ──┤ 未来的散装组件（日记/token/人设…）├─ 各自独立启停
```

- **组件**：独立插件，独立配置、独立数据目录（plugin_data）、独立启停
- **门面**：只做「发现 + 状态汇总」，不持有组件逻辑；卸掉门面组件照常跑

## 指令

| 指令 | 说明 |
|---|---|
| `/qqkit` | 套件组件状态页（安装/启停/版本聚合） |
| `/qqsvc` | 门面自身在线检查（0.1 兼容保留） |

## 组件识别约定

- 插件 `name` 以 `astrbot_plugin_qqmind` / `astrbot_plugin_qq_kit` 开头
- 或 `author` 含 DanDingBenShao 且 `name` 以 `astrbot_plugin_` 开头

## 安装

从 AstrBot 插件市场或仓库安装：

```
https://github.com/DanDingBenShao/astrbot_plugin_qq_kit
```

## License

MIT

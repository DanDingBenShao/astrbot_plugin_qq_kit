"""本少的qq机器人功能包 —— 套件门面（v0.2.0）。

定位：套件主框架的「壳」。自身不做业务，启动时探测本机已装的本少系
组件插件（按 metadata.author / name 前缀识别），`/qqkit` 输出组件状态
聚合页。组件插件各自独立运行、独立启停（AstrBot 面板开关），套件门面
只做「发现 + 状态汇总」，不持有任何组件逻辑。

组件识别约定（本少系散装插件）：
- name 以 `astrbot_plugin_qqmind` 开头（主体/未来拆分件）
- 或 metadata.author 含 `DanDingBenShao` 且 name 以 `astrbot_plugin_` 开头
"""

from __future__ import annotations

from astrbot.api import logger, star
from astrbot.api.event import AstrMessageEvent, filter

PLUGIN_VERSION = "0.2.0"

# 组件名前缀 → 展示名（本少系套件家族）
_FAMILY_PREFIXES = ("astrbot_plugin_qqmind", "astrbot_plugin_qq_kit")


def _is_family(md) -> bool:
    name = (getattr(md, "name", "") or "")
    author = (getattr(md, "author", "") or "")
    if any(name.startswith(p) for p in _FAMILY_PREFIXES):
        return True
    return "DanDingBenShao" in author and name.startswith("astrbot_plugin_")


class QQKitPlugin(star.Star):
    """套件门面：探测本少系组件插件，输出聚合状态页。"""

    def __init__(self, context: star.Context) -> None:
        super().__init__(context)
        logger.info(f"[qq_kit] loaded v{PLUGIN_VERSION}")

    def _scan_family(self) -> list[tuple[str, str, str, bool]]:
        """扫已载入插件，返回本少系组件 [(展示名, 版本, 一句话描述, 激活)]。"""
        out = []
        try:
            stars = self.context.get_all_stars()
        except Exception as e:
            logger.warning(f"[qq_kit] get_all_stars failed: {e!r}")
            return out
        for md in stars:
            if not _is_family(md):
                continue
            desc = (getattr(md, "desc", "") or "").strip()
            out.append((
                (getattr(md, "display_name", "") or md.name),
                (getattr(md, "version", "") or "?"),
                desc.splitlines()[0][:40] if desc else "",
                bool(getattr(md, "activated", True))))
        return out

    @filter.command("qqkit")
    async def cmd_qqkit(self, event: AstrMessageEvent):
        """套件状态页：本少系组件插件的安装/启停/版本聚合。"""
        fam = self._scan_family()
        lines = [f"🧰 本少的qq机器人功能包 v{PLUGIN_VERSION}"]
        if not fam:
            lines.append(
                "（未检测到套件组件——装上 astrbot_plugin_qqmind 等组件后这里会显示）")
        else:
            lines.append(f"组件 {len(fam)} 个：")
            for name, ver, desc, active in fam:
                flag = "✅" if active else "⏸ 未启用"
                lines.append(f"· {name} v{ver} {flag}"
                             + (f" — {desc}" if desc else ""))
            if any(not a for *_, a in fam):
                lines.append("（有组件被停用，AstrBot 面板可重新启用）")
        yield event.plain_result("\n".join(lines))

    @filter.command("qqsvc")
    async def qqsvc(self, event: AstrMessageEvent):
        """查看插件状态（0.1 兼容保留）。"""
        yield event.plain_result(
            f"本少的qq机器人功能包 v{PLUGIN_VERSION} 在线\n"
            f"会话: {event.unified_msg_origin}\n"
            f"组件状态请用 /qqkit"
        )

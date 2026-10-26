"""本少的qq机器人功能包 —— 为 QQ 机器人服务的基础设施插件（占位版）。

版本号与 metadata.yaml 保持一致；每次发版记得两处一起改。
"""

from astrbot.api import logger, star
from astrbot.api.event import AstrMessageEvent, filter

PLUGIN_VERSION = "0.1.0"


class QQKitPlugin(star.Star):
    """占位插件：先让骨架跑起来，后续往里加能力。"""

    def __init__(self, context: star.Context) -> None:
        super().__init__(context)
        logger.info(f"[qq_kit] loaded v{PLUGIN_VERSION}")

    @filter.command("qqsvc")
    async def qqsvc(self, event: AstrMessageEvent):
        """查看插件状态。"""
        yield event.plain_result(
            f"本少的qq机器人功能包 v{PLUGIN_VERSION} 在线\n"
            f"会话: {event.unified_msg_origin}"
        )

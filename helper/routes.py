import re
import time
import math
import logging
import secrets
import mimetypes
from aiohttp import web
from aiohttp.http_exceptions import BadStatusLine
from Dxbots.bot import multi_clients, work_loads, DxStreamBot
from Dxbots.server.exceptions import FIleNotFound, InvalidHash
from Dxbots import StartTime, __version__
from ..utils.time_format import get_readable_time
from ..utils.custom_dl import ByteStreamer
from Dxbots.utils.render_template import render_page
from Dxbots.vars import Var


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(_):
    return web.json_response(
        {
            "server_status": "running",
            "uptime": get_readable_time(time.time() - StartTime),
            "telegram_bot": "@" + DxStreamBot.username,
            "connected_bots": len(multi_clients),
            "loads": dict(
                ("bot" + str(c + 1), l)
                for c, (_, l) in enumerate(
                    sorted(work_loads.items(), key=lambda x: x[1], reverse=True)
                )
            ),
            "version": __version__,
        }
    )

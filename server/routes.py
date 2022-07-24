from sanic import Request
from sanic.views import HTTPMethodView
from sanic.response import json
from loguru import logger

from bot.bot import TgBot
from gitlab.webhooks.pipeline.proc import PipeLineDataProc


class BaseWebhook(HTTPMethodView):
    route: str


class PiplineWebhook(BaseWebhook):
    route = "/webhook/pipeline"

    async def post(self, r: Request):
        # TODO handle x-gitlab-event in r.headers to avoid boilerplate code
        logger.warning(r.json)
        pipe = PipeLineDataProc(r.json)
        b: TgBot = r.app.ctx.bot
        await b.send_data(pipe.to_message())
        return json({"status": "ok"})

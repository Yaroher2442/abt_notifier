from sanic import Sanic

from bot.bot import TgBot
from config.config import ServerConfig
from server.routes import BaseWebhook
from database.connection import init


class Server:

    def __init__(self, config: ServerConfig, bot: TgBot):
        self.config = config
        self.sanic_app = Sanic("App")
        self.bot = bot
        "http://5.35.30.9:8888/"

    async def _before_start(self, app: Sanic, loop):
        await init(self.config.database)

    async def _after_start(self, app: Sanic, loop):
        await app.add_task(self.bot.run())

    def _configure(self):
        self.sanic_app.ctx.bot = self.bot
        self.sanic_app.before_server_start(self._before_start)
        self.sanic_app.after_server_start(self._after_start)
        for view in BaseWebhook.__subclasses__():
            self.sanic_app.add_route(view.as_view(), view.route)

    def run(self):
        self._configure()
        self.sanic_app.run(self.config.host, self.config.port)

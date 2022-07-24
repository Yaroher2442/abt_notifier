import asyncio
import json

from bot.bot import TgBot
from config.config import AppConfig
from server.log_ext import LogsHandlerExt
from server.server import Server


class App:
    def __init__(self, config: AppConfig):
        self.bot = TgBot(config.bot)
        self.server = Server(config.server, self.bot)

    def run(self):
        LogsHandlerExt.set_logger()
        self.server.run()
        # asyncio.run(self.bot.run())


if __name__ == '__main__':
    conf = json.loads(open("config/config.json", "r").read())
    app = App(AppConfig(**conf))
    app.run()

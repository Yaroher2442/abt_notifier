from loguru import logger
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from config.config import TgBotConfig


class TgBot:

    def __init__(self, config: TgBotConfig):
        self.bot = AsyncTeleBot(config.token)

    async def send_data(self, data: str) -> None:
        await self.bot.send_message("446387634", data)  # TODO avoid hardcode id

    def _chat_callbacks(self):
        @self.bot.message_handler(commands=["start"])
        async def _on_start_cmd(msg: Message):
            logger.warning(msg)
            await self.bot.send_message(msg.chat.id, "Hi, i am tg bot with gitlab sense")

    async def run(self):
        self._chat_callbacks()
        logger.info("Bot started")
        # self.bot.polling(none_stop=True)
        await self.bot.infinity_polling()

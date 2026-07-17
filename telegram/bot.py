import asyncio
import configparser

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from handlers.init import register_handlers

config = configparser.ConfigParser()
config.read('config.ini')

try:
    TELEGRAM_API_BASE_URL = config['DEFAULT']['TELEGRAM_API_BASE_URL']
    api = TelegramAPIServer.from_base(TELEGRAM_API_BASE_URL)
    session = AiohttpSession(api=api)
except:
    session = None

bot = Bot(
    token=config['DEFAULT']['TOKEN'],
    default=DefaultBotProperties(parse_mode="HTML"),
    session=session
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)


async def set_commands():
    commands = [

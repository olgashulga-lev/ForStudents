import asyncio
import configparser
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from handlers.init import register_handlers

config = configparser.ConfigParser()
config.read('config.ini')

bot = Bot(
    token=config['DEFAULT']['TOKEN'],
    default=DefaultBotProperties(parse_mode="HTML")
)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)


async def set_commands():
    commands = [

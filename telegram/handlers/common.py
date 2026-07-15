from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    text = """

    """
    await message.answer(text)
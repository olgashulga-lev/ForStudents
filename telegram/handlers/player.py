import os
from aiogram import Router, types
from aiogram.filters import Command
import api
from .common_utils import get_player_or_none
from aiogram.types import FSInputFile

router = Router()

@router.message(Command("avatar"))
async def cmd_avatar(message: types.Message):
    
    # Проверяем существует ли файл
    if os.path.exists(player.photo):
        try:
            photo = FSInputFile(player.photo)
            
        except Exception as e:
            
            
    else:
        # Если файл не найден, отправляем только текст
        
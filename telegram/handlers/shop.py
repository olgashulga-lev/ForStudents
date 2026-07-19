from aiogram import Router, types, F
from aiogram.filters import Command

import api
from .common_utils import get_player_or_none
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(Command("shop"))
async def cmd_shop(message: types.Message):
    
    shop_items = [i for i in items if i.type == 'shop']
    shop_items = []  # Создаем пустой список
    for i in items:  # Перебираем каждый предмет
        if i.type == 'shop':  # Если тип == 'shop'
            shop_items.append(i)  # Добавляем в список
            
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    for item in shop_items:
        text += f"<b>{item.name}</b>\n"
        text += f"   {item.description}\n"
        text += f"   {item.price} монет\n\n"
        
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=f"Купить {item.name} ({item.price})",
                callback_data=f"buy_{item.id}"
            )
        ])
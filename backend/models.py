from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Player:
    def __init__(self, chat_id, user_id, name, photo, exp=0, money=100, hp=100, damage=20, luck=0.2, level=1):
        self.chat_id = chat_id
        self.user_id = user_id
        self.name = name
        self.photo = photo
        self.exp = exp
        self.money = money
        self.hp = hp
        self.damage = damage
        self.luck = luck
        self.level = level

    def __str__(self):
        return f"{self.name} (Ур. {self.level})"
    
    def get_exp_for_next_level(self):

    
    def get_max_level(self):

    
    def add_exp(self, amount):

        
        leveled_up = False
        while 
            needed =
            if self.exp >= needed:
                self.exp -= needed
                self.level += 1
                self.apply_level_bonus()
                leveled_up = True
            else:
                break
        
        if self.level >= self.get_max_level():
            self.exp = 0
        
        return leveled_up
    
    def apply_level_bonus(self):
        

class Achievement:


class Event:


class Boss:


class Item:

# День 3
import random
from aiogram import Router, types
from aiogram.filters import Command

import api
from .common_utils import get_player_or_none

router = Router()

@router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    player = get_player_or_none(message)#получает игрока из базы
    if #? нет игрока
        await message.answer("??? /registration")
        return
    
    bet = ?? #ставка
    if # денег игрока меньше чем ставка
        await message.answer(f"??? {bet}, есть: {player.money}")
        return
    
    player_dice = random.randint(?? от скольки и до)
    bot_dice = random.randint(??)
    
    text = f"""
<b>Игра в кости</b>
???
    """
    
    if ???
        win ???
        player.money ???
        api.update_player(player)
        text += f"\n<b>Вы победили!</b> +{win} монет!"
    elif ???
        player.money ???
        api.update_player(player)
        text += f"\n<b>Вы проиграли!</b> -{bet} монет!"
    else:
        text += "\n<b>Ничья!</b> Ставка возвращена."
    
    await message.answer(text)


@router.message(Command("dice_big"))
async def cmd_dice_big(message: types.Message):
    player = get_player_or_none(message)
    if not player:
        await message.answer("Сначала зарегистрируйтесь: /registration")
        return
    
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Укажите ставку: /dice_big 50")
        return
    
    try:
        bet = int(args[1])
        if bet <= 0:
            await message.answer("Ставка должна быть положительной!")
            return
    except ValueError:
        await message.answer("Введите число!")
        return
    
    if player.money < bet:
        await message.answer(f"У вас недостаточно денег! Нужно: {bet}, есть: {player.money}")
        return
    
    player_dice = random.randint(1, 6)
    bot_dice = random.randint(1, 6)
    
    text = f"""
<b>Игра в кости (большая ставка)</b>
Ставка: {bet} монет

Ваш бросок: {player_dice}
Бросок бота: {bot_dice}
    """
    
    if player_dice > bot_dice:
        win = bet * 2
        player.money += win
        api.update_player(player)
        text += f"\n<b>Вы победили!</b> +{win} монет!"
    elif player_dice < bot_dice:
        player.money -= bet
        api.update_player(player)
        text += f"\n<b>Вы проиграли!</b> -{bet} монет!"
    else:
        text += "\n<b>Ничья!</b> Ставка возвращена."
    
    await message.answer(text)


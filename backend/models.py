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

# fight
import random
import asyncio
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import api
from .common_utils import get_player_or_none

router = Router()
active_duels = {} #Словарь для хранения активных дуэлей. Ключ — chat_id, значение — список дуэлей в этом чате

async def perform_duel(player1, player2, challenger_id, target_id, callback):
    api.clear_expired_effects(callback.message.chat.id, player1.user_id) #Очистка эффектов у игрока 1
    # очистка у 2 игрока
    
    effects1 = api.get_active_effects(callback.message.chat.id, player1.user_id)#Получение активных эффектов игрока 1
    # у второго
    
    player1_damage = player1.damage
    # для хранения урона, удачи и здоровья игроков 1 и 2
    
    
    for e in effects1:
        if e.get('effect_type') == 'damage_bonus':
            player1_damage += e.get('value', 0)
        elif e.get('effect_type') == 'luck_bonus':
            player1_luck += e.get('value', 0) / 100
        elif e.get('effect_type') == 'hp_bonus':
            player1_hp += e.get('value', 0)
    
    # сделать цикл для эффектов 2 игрока
    
    initial_hp1 = player1_hp #начальное здоровье игрока 1
    #написать для 2 игрока
    
    text = f"<b>ДУЭЛЬ НАЧАЛАСЬ!</b>\n\n"
    text += f"{player1.name} {player1_hp} HP | {player1_damage} урона\n"
    text += f"{player2.name} {player2_hp} HP | {player2_damage} урона\n\n"
    text += f"<b>Бой идёт до 3 раундов или до смерти!</b>\n"
    text += "═" * 30 + "\n\n"
    
    max_rounds = 3
    round_num = 1
    
    while # пока раунд не макс. и здоровье обоих игроков больше 0
        text += f"<b>РАУНД {round_num}</b>\n"
        initiative1 = random.randint(1, 20) + player1_luck * 10#инициатива игрока
        #написать для 2
        base_damage1 = random.randint(5, 15) + player1_damage // 3#базовый урон игрока 
        #написать для 2
        if random.random() < #удача 1 игрока
            base_damage1 = int(base_damage1 * 1.5)#Увеличь урон на 50% и округли вниз до целого числа
            text += f"{player1.name} повезло! Критический удар!\n"
        
        #написать для 2
        
        if #инициатива 1 игрока больше 2
            player2_hp -= base_damage1
            if player2_hp <= 0:
                player2_hp = 0
                text += f"{player1.name} нанёс {base_damage1} урона → {player2_hp} HP\n"
                text += f"{player2.name} повержен!\n"
                break
            
            #написать про здоровье 1 игрока
            
            text += f"{player1.name} нанёс {base_damage1} урона → {player2_hp} HP\n"
            #написать для 2 игрока
        else:
            player1_hp -= #урон 2 игрока
            if # здоровье 1 игрока меньше или равно 0
                #здоровье 1 игрока 0
                text += f"{} нанёс {} урона → {} HP\n"
                text += f"{} повержен!\n"
                break
            
            player2_hp -= # урон 1 игрока
            #написать про здоровье 2 игрока
            
            text += f"{} нанёс {} урона → {} HP\n"
            text += f"{} нанёс {} урона → {} HP\n"
        
        text += "\n"
        round_num += 1
    
    text += "═" * 30 + "\n\n"
    
    exp_for_winner = random.randint(?)#опыт для победителя
    exp_for_loser = random.randint(?)#опыт для проигравшего
    
    if # здоровье 1 больше 2
        win_money = random.randint(?)
        player1.money += ?
        player1.hp = player1_hp
        #написать про здоровье 2
        
        leveled1 = player1.add_exp(exp_for_winner)#добавляет опыт и проверяет повышение уровня
        leveled2 ???
        
        api.update_player(player1)#отправляет запрос на обновление игрока 1 в базе данных
        #для 2
        
        text += f"<b>{} ПОБЕДИЛ!</b>\n"
        text += f"+{} монет!\n"
        text += f"+{} опыта"
        if leveled1:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
        text += f"\nОсталось HP: {}\n"
        
        text += f"\n{} проиграл\n"
        text += f"+{} опыта (за участие)"
        if leveled2:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
        
        if player2_hp <= 0:
            text += f"\n{} мёртв!"
    
    elif player2_hp > player1_hp:
        win_money = random.randint()
        player2.money += 
        player1.hp = 
        player2.hp = 
        
        leveled1 = player1.add_exp(exp_for_loser)
        leveled2 =
        
        api.update_player(player1)
        #для 2
        
        text += f"<b>{} ПОБЕДИЛ!</b>\n"
        text += f"+{} монет!\n"
        text += f"+{} опыта"
        if leveled2:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
        text += f"\nОсталось HP: {}\n"
        
        text += f"\n{} проиграл\n"
        text += f"+{} опыта"
        if leveled1:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
        
        if player1_hp <= 0:
            text += f"\n{} мёртв!"
    
    else:
        #сохранение здоровья
        
        exp_draw = random.randint()
        leveled1 = player1.add_exp(exp_draw)
        #про 2
        
        #сохранение в базу
        
        text += f"<b>НИЧЬЯ!</b>\n"
        text += f"У обоих осталось {} HP\n"
        text += f"Оба получают +{} опыта!"
        if leveled1:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
        if leveled2:
            text += f"{} ПОВЫСИЛ УРОВЕНЬ ДО {}!"
    
    if player1_hp < 0:
        player1_hp = 0
    # про 
    
    player1.hp = min(100, player1_hp)
    player2.hp = min(100, player2_hp)
    api.update_player(player1)
    api.update_player(player2)
    
    return text

@router.message(Command("fight"))
async def cmd_duel(message: types.Message):
    player = get_player_or_none(message)
    if #нет игрока
        await message.answer("   /registration")
        return
    
    all_players = api.get_all_players()
    available_players = []
    for #игрок из списка
        if ?.user_id == message.from_user.id:#ID пользователя, который написал команду /fight
            continue
        
        in_duel = False
        if Проверяем, есть ли в этом чате активные дуэли
            for дуэль в активных дуэлях [message.chat.id]:
                if Если ID текущего игрока совпадает с ID первого игрока в дуэли ИЛИ с ID второго игрока в дуэли, значит, этот игрок уже участвует в дуэли
                    in_duel = True
                    break
        
        if not in_duel:
            Добавляем этого игрока в список доступных для дуэли
    
    if not available_players:
        await message.answer("")
        return
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])#Это клавиатура, которая появляется под сообщением в виде кнопок. При нажатии на кнопку отправляется callback-запрос.
    
    for p in available_players[??]:
        keyboard.inline_keyboard.append([
            InlineKeyboardButton(
                text=f"{??} (Ур. {??} | {??} HP)",
                callback_data=f"duel_select_{???}"
            )
        ])
    
    keyboard.inline_keyboard.append([
        InlineKeyboardButton(
            text="Отмена",
            callback_data="duel_cancel"
        )
    ])
    
    await message.answer(
        "<b>Выберите противника для дуэли:</b>\n\n"
        f"Ваш баланс: {} монет\n"
        f"Ваше HP: {}\n"
        f"Ваш урон: {}\n\n"
        f"Бой будет длиться до 3 раундов или до смерти!",
        reply_markup=?? кнопки
    )


@router.callback_query(F.data.startswith("duel_select_"))
async def cmd_duel_select(callback: types.CallbackQuery):
    data = callback.data.split('_')
    
    if len(data) <???
        await callback.answer("???")
        return
    
    try:
        target_id = int(???)
    except ValueError:
        await callback.answer("???")
        return
    
    player = api.get_player(callback.message.chat.id, callback.from_user.id)#Получи данные игрока из базы по chat_id и user_id, которые взяты из callback-запроса".
    if нет игрока
        await callback.answer("???")
        return
    
    if player.hp <= 
        await callback.answer("???")
        return
    
    all_players = api.get_all_players()#Получи список всех зарегистрированных игроков из базы данных
    target = next((p for p in all_players if ???), если не нашли)#Пройти по всем игрокам, найти первого, у кого user_id равен target_id. Если такого игрока нет — вернуть None
    
    if not target:
        await callback.answer("???")
        return
    
    if здоровье
        await callback.answer("???")
        return
    
    if id одинаковое
        await callback.answer("???")
        return
    
    if callback.message.chat.id in active_duels:
        for duel in active_duels[callback.message.chat.id]:
            if duel['player1'] == target_id или ??
                await callback.answer("???")
                return
    
    if callback.message.chat.id not in active_duels:
        active_duels[callback.message.chat.id] = []
    
    active_duels[callback.message.chat.id].append({
        'player1': callback.from_user.id,
        'player2': ???
        'status': 'waiting',#ожидание
        'challenger_chat_id': callback.message.chat.id,
        'target_chat_id':???
    })
    
    keyboard = создание клавиатуры
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="???",
                    callback_data=f"accept_duel_{callback.from_user.id}_{target_id}"#данные при нажатие на кнопку
                )
            ],
            [
                InlineKeyboardButton(
                    text="???",
                    callback_data=f"refuse_duel_???"
                )
            ]
        ]
    )
    
    await callback.message.edit_text(
        f"<b>Вы вызвали {???} на дуэль!</b>\n\n"
        f"Ожидайте ответа...\n"
    )
    
    try:
        await callback.bot.send_message(
            chat_id=target.chat_id,
            text=(
                f"<b>ВЫЗОВ НА ДУЭЛЬ!</b>\n\n"
                f"<b>{???}</b> вызывает вас на дуэль!\n\n"
                f"<b>Статистика вызывающего:</b>\n"
                f"   HP: {???}\n"
                f"   Урон: {???}\n"
                f"   Удача: {int(player.luck * 100)}%\n\n"
                f"<b>Ваша статистика:</b>\n"
                f"   HP: {???}\n"
                f"   Урон: {???}\n"
                f"   Удача: {int(target.luck * 100)}%\n\n"
            ),
            reply_markup=keyboard#кнопки принять отказаться
        )
    except Exception as e:
        print(f"Ошибка отправки сообщения противнику: {e}")
        await callback.message.edit_text(
            f"Не удалось отправить вызов {???}!\n"
            f"Убедитесь, что бот может писать ему в личные сообщения."
        )
        return
    
    await callback.answer(f"Вызов отправлен {???}!")


@router.callback_query(F.data.startswith("refuse_duel_"))
async def cmd_duel_refuse(callback: types.CallbackQuery):#команда отказа от дуэли
    data = callback.data.split('_')
    if len(data) < ???
        await callback.answer("??")
        return
    
    try:
        challenger_id = int(??
        target_id = ??
    except ValueError:
        await ???
        return
    
    if callback.from_user.id ??? target_id:
        await ???
        return
    
    if callback.message.chat.id in active_duels:#Если в этом чате есть активные дуэли
        for duel in active_duels[callback.message.chat.id][:]:#Копия списка дуэлей в чате
            if duel['player1'] == challenger_id ???:
                active_duels[callback.message.chat.id].remove(duel)#Удаляем эту дуэль из списка активных
                break
    
    await callback.message.edit_text(
        f"{callback.from_user.first_name} ???"
    )
    await callback.answer("???")


@router.callback_query(F.data == "duel_cancel")
async def cmd_duel_cancel(callback: types.CallbackQuery):
    await callback.message.delete()
    await ???

@router.callback_query(F.data.startswith("accept_duel_"))
async def cmd_duel_accept(callback: types.CallbackQuery):#команда принятия дуэли
    data = ?
    
    if len(data) < ?:
        await ?
        return
    
    try:
        challenger_id = ?
        target_id = ?
    except ValueError:
        await callback.answer("?")
        return
    
    if callback.from_user.id ?? target_id:
        await ?
        return
    
    duel = None
    duel_key = None
    for key, duels in active_duels.items():
        for d in duels:
            if d['player1'] ???:
                duel = d
                duel_key = key
                break
        if duel:
            break
    
    if not duel:
        await ???
        return
    
    player1 = api.get_player(duel['challenger_chat_id'], challenger_id)#Получи данные вызывающего игрока по его chat_id и user_id
    if not player1:
        all_players = api.get_all_players()#Получаем всех игроков из базы
        player1 = next((p for p in all_players if p.user_id == challenger_id), None)#Если не удалось получить игрока по chat_id, попробуй найти его по user_id среди всех игроков
    
    player2 ? написать для 2
    
    if not player1 or not player2:
        await ??
        return
    
    if player1.hp ???
        await callback.answer("??")
        active_duels[duel_key].remove(duel)
        await callback.message.edit_text("???")
        return
    
    if player2.hp ??
        await callback.answer("???")
        return
    
    duel['status'] = 'fighting'
    
    await callback.message.edit_text(
        f"<b>ДУЭЛЬ НАЧИНАЕТСЯ!</b>\n\n"
        f"{} {} HP\n"
        f"{} {} HP\n\n"
        f"Идёт расчёт боя..."
    )
    
    try:
        await callback.bot.send_message(
            chat_id=duel['challenger_chat_id'],#Отправь сообщение в чат вызывающего игрока
            text=(
                f"<b>{???} ПРИНЯЛ ДУЭЛЬ!</b>\n\n"
                f"Бой начинается!"
            )
        )
    except Exception as e:
        print(f"Ошибка уведомления вызывающего: {e}")
    
    await asyncio.sleep(2)#Функция — приостанавливает выполнение на 2 секунды
    text = await perform_duel(???)#Выполни функцию perform_duel(), которая рассчитывает все раунды боя, и сохрани результат в переменную text
    active_duels[duel_key].remove(duel)
    
    try:
        await callback.bot.send_message(
            chat_id=duel['challenger_chat_id'],
            text=text
        )
    except Exception as e:
        print(f"Ошибка отправки результата вызывающему: {e}")
    
    await callback.message.edit_text(???)
    await ???


@router.message(Command("fight_cancel"))
async def cmd_duel_cancel_all(message: types.Message):#команда отмены всех дуэлей
    if message.chat.id not ???
        await ???
        return
    
    removed = False
    for duel in active_duels[message.chat.id][:]:
        if duel['player1'] == message.from_user.id ????:
            active_duels[message.chat.id].remove(???)
            removed = True
    
    if removed:
        await ???
    else:
        await ???


#День 4

from aiogram import Router, types
from aiogram.filters import Command
import api
from .common_utils import get_player_or_none
from aiogram.types import FSInputFile

router = Router()

@router.message(Command("avatar"))
async def cmd_avatar(message: types.Message):
    player = get_player_or_none(message)
    if not player:
        await message.answer("Сначала зарегистрируйтесь: /registration")
        return
    
    current_level = player.level
    max_level = player.get_max_level()
    
    if current_level < max_level:
        exp_for_next = player.get_exp_for_next_level()
        exp_text = f"Опыт: {player.exp}/{exp_for_next}"
    else:
        exp_text = "МАКСИМУМ!"
    
    text = f"""
<b>{player.name}</b>

Уровень: {player.level}/30
{exp_text}

HP: {player.hp}/100
Урон: {player.damage}
Удача: {int(player.luck * 100)}
Деньги: {player.money}
"""
    try:
        await message.answer_photo(FSInputFile(player.photo), caption=text)
    except:
        await message.answer(text)

@router.message(Command("inventory"))
async def cmd_inventory(message: types.Message):
    player = get_player_or_none(message)
    if not player:
        await message.answer("Сначала зарегистрируйтесь: /registration")
        return
    
    inventory = api.get_inventory(message.chat.id, message.from_user.id)
    
    if not inventory:
        await message.answer(f"<b>Инвентарь {player.name}:</b>\n\nПока пуст...")
        return
    
    text = f"<b>Инвентарь {player.name}:</b>\n\n"
    
    items_by_type = {}
    for item in inventory:
        item_type = item.get('type', 'Прочее')
        if item_type not in items_by_type:
            items_by_type[item_type] = []
        items_by_type[item_type].append(item)
    
    for item_type, items in items_by_type.items():
        text += f"<b>{item_type}:</b>\n"
        for item in items:
            text += f"{item['name']} x{item['quantity']}\n"
        text += "\n"
    
    await message.answer(text)

@router.message(Command("achievement"))
async def cmd_achievement(message: types.Message):
    player = get_player_or_none(message)#Получи данные игрока из базы. Если игрок не зарегистрирован — вернет None
    if 
        await 
        return
    
    achievements = api.get_user_achievements(message.chat.id, message.from_user.id)#Запроси у бэкенда список достижений этого игрока
    
    if 
        await 
        return
    
    text = f"<b>Достижения {???}:</b>\n\n"
    
    for ach in achievements[???]:
        text += f"<b>{???}</b>\n"
        text += f"   {???}\n\n"
    
    if len(achievements) > ???:
        text += f"\n... и еще {len(achievements) - ???} достижений"
    
    await message.answer(text)

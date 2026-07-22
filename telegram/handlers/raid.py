from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
import api
from .common_utils import get_player_or_none
import random
import uuid
import os

router = Router()
active_raids = {}

BOSS_IMAGES = {
    1: "static/bosses/big_frog.jpg",
    2: "static/bosses/orc.jpg",
    3: "static/bosses/dragon.jpg"
}

def generate_raid_id():
    return str(uuid.uuid4())[:8]

async def perform_raid_battle(raid, boss, callback=None):
    

@router.message(Command("raid"))
async def cmd_raid(message: types.Message):
            text += f"Создатель: {creator_name}\n"
            text += f"{status}\n"
            text += f"HP: {raid.get('boss_current_hp', boss.hp)}\n"
            
            if not is_participant and raid['status'] == 'recruiting':
                text += f"/join {creator_name} - присоединиться\n"
            elif is_participant:
                text += f"Вы уже в этом рейде!\n"
            else:
                text += f"Рейд уже начался!\n"
            
            text += "\n"

@router.message(Command("join"))
async def cmd_join_by_name(message: types.Message):
            
    creator_name = ' '.join(args[1:]).strip()
        
        for raid_id, raid in active_raids.items():
        if raid['status'] != 'recruiting':
            continue
            
        creator = None
        all_players = api.get_all_players()
        for p in all_players:
            if p.user_id == raid['creator_id']:
                creator = p
                break
        
        if creator and creator.name.lower() == creator_name.lower():
            found_raid = raid
            found_raid_id = raid_id
            break
    
    if not found_raid:
        await message.answer(
            f"Рейд с создателем '{creator_name}' не найден!\n"
            f"Используйте /raid для списка активных рейдов."
        )
        return
    
    for other_raid in active_raids.values():
        if message.from_user.id in other_raid['players']:
            await message.answer("Вы уже участвуете в другом рейде!")
            return
    
    if len(found_raid['players']) >= found_raid.get('max_players', 5):
        await message.answer("Рейд полон! (максимум 5 игроков)")
        return
    
    found_raid['players'].append(message.from_user.id)
    
    creator = None
    all_players = api.get_all_players()
    for p in all_players:
        if p.user_id == found_raid['creator_id']:
            creator = p
            break
    
    if creator:
        try:
            await message.bot.send_message(
                chat_id=creator.chat_id,
                text=f"Игрок {player.name} присоединился к вашему рейду!\n"
                     f"Теперь участников: {len(found_raid['players'])}\n\n"
                     f"Когда наберётся 2+ игроков, нажмите «Начать бой»"
            )
        except:
            pass
    
    await message.answer(
        f"Вы присоединились к рейду {creator_name}!\n"
        f"Участников: {len(found_raid['players'])}\n\n"
        f"Команды:\n"
        f"/raid_status - статус рейда\n"
        f"/leave_raid - выйти из рейда"
    )

async def start_raid(message: types.Message, boss_id: int):
    boss_image = BOSS_IMAGES.get(boss_id)
    if boss_image and os.path.exists(boss_image):
        try:
            photo = FSInputFile(boss_image)
            await message.answer_photo(
                photo=photo,
                caption=f"<b>{boss.name}</b>\nHP: {boss.hp}\nУрон: {boss.damage}"
            )
        except Exception as e:
            print(f"Ошибка при отправке фото босса: {e}")
    

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Начать бой",
                    callback_data=f"start_raid_battle_{raid_id}"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Отменить рейд",
                    callback_data=f"cancel_raid_{raid_id}"
                )
            ]
        ]
    )

    await message.answer(
        f"<b>Рейд создан!</b>\n\n"
        f"Босс: \n"
        f"HP: \n"
        f"Награда:  монет\n"
        f"Опыт: \n\n"
        f"Создатель: \n"
        f"Участников: 1/5\n\n"
        f"Друзья могут присоединиться из любого чата с ботом:\n"
        f"/join \n\n"
        f"Когда наберётся 2+ игроков, нажмите «Начать бой»",
        reply_markup=keyboard
    )

@router.message(Command("boss1"))
async def cmd_boss1(message: types.Message):
    await start_raid(message, 1)



@router.message(Command("raid_status"))
async def cmd_raid_status(message: types.Message):
    

@router.message(Command("leave_raid"))
async def cmd_leave_raid(message: types.Message):
    for raid_id, raid in active_raids.items():
        if message.from_user.id in raid['players']:
            if raid[''] != '':
                
            
            
            

@router.callback_query(F.data.startswith("start_raid_battle_"))
async def cmd_raid_battle(callback: types.CallbackQuery):
    raid_id = callback.data.replace("start_raid_battle_", "")
    
    
    boss = next((b for b in api.get_bosses() if b.id == raid['boss_id']), None)
    
    
    for user_id in raid['players']:
        
    
    
    
    boss_hp = battle_result['boss_hp']
    
    
    
    for i, name in enumerate(players_names):
        
    
    
    if boss_hp <= 0:
        

        for  in raid['']:
            for p in all_players:
                if  == :
                    
                    has_achievement = any(a.name == achievement_config[boss.id]['name'] for a in existing)
                
                    if not has_achievement and boss.id in achievement_config:
                        result = api.give_achievement(
                            chat_id=p.chat_id,
                            user_id=user_id,
                            name=achievement_config[boss.id]['name'],
                            description=achievement_config[boss.id]['desc'],
                            condition=f"Победа над боссом {boss.name}"
                        )
                        if result:
                            achievement_messages.append(f"{p.name} получил достижение '{achievement_config[boss.id]['name']}'!")
                    break
    
        
        for  in raid['']:
            for p in all_players:
                if  == :
                    player = 
                    if player:
                        
    
        if level_up_messages:
            text += "\n\n" + "\n".join(level_up_messages)
        
        for  in raid['']:
            
        
        
        
    else:
        
        
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Начать бой снова",
                        callback_data=f"start_raid_battle_{raid_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Отменить рейд",
                        callback_data=f"cancel_raid_{raid_id}"
                    )
                ]
            ]
        )
        
        for  in raid['']:
            
        
        await callback.message.edit_text(text, reply_markup=keyboard)
    
    

@router.callback_query(F.data.startswith("cancel_raid_"))
async def cmd_cancel_raid(callback: types.CallbackQuery):
    raid_id = callback.data.replace("cancel_raid_", "")
    
    
    
    
    for  raid['']:
        

async def check_and_give_boss_achievements(boss_id, user_id, chat_id, bot):
    achievement_config = {
        1: {
            
        },
        2: {
            
        },
        3: {
            
        }
    }
    

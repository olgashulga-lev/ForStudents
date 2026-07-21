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


@router.message(Command("join"))
async def cmd_join_by_name(message: types.Message):
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
    

async def start_raid(message: types.Message, boss_id: int):
    

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
    

@router.callback_query(F.data.startswith("start_raid_battle_"))
async def cmd_raid_battle(callback: types.CallbackQuery):
    
        achievement_config = {
            1: {"name": "", "desc": ""},
            2: {"name": "", "desc": ""},
            3: {"name": "", "desc": ""}
        }

        

@router.callback_query(F.data.startswith("cancel_raid_"))
async def cmd_cancel_raid(callback: types.CallbackQuery):
   
async def check_and_give_boss_achievements(boss_id, user_id, chat_id, bot):
    achievement_config = {
        1: {
            'name': "",
            'description': ""
        },
        2: {
            'name': "",
            'description': ""
        },
        3: {
            'name': "",
            'description': ""
        }
    }
    
    
    await callback.message.edit_text("Рейд отменён")

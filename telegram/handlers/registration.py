from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models import Player
import api
from .common_utils import check_player
import os
from pathlib import Path

router = Router()

class RegistrationState(StatesGroup):
    waiting_name = State()
    waiting_photo = State()


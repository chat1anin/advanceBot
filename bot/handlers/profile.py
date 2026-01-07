from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class ProfileStates(StatesGroup):
    last_name = State()
    first_name = State()
    middle_name = State()
    position = State()
    employee_id = State()
    confirm = State()

router = Router()

# Хендлеры для каждого шага FSM
# TODO: добавить валидацию и сохранение в БД

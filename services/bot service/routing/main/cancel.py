from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from routers import main_router

@main_router.message(Command("cancel"))
async def cancel(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    msg_text = "Дія відмінена"
    await message.answer(msg_text)
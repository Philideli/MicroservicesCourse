from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import requests

from routers import main_router
from consts import SERVICE_URLS

@main_router.message(Command("my_orders"))
async def my_orders(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    adress = f'{SERVICE_URLS[0]}/clients/add'
    data = {
        "clientId": str(message.from_user.id)
    }
    response = requests.post(adress, data=data)
    if response.status_code == 200:
        data = response.json()
        msg_text = "e\n"
        for k in data.keys():
            msg_text += f"'{k}': {data[k]}"
            # TODO 
            # Понять, как правильно парсить запрос и в зависимости от этого генерить сообщение
            # Здесь будет просто 1 сообщение со всеми заказами пользователя
    await message.answer(msg_text)
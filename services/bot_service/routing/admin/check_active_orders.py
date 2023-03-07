from aiogram import types
from aiogram.filters import Command
import requests

from routers import main_router
from consts import SERVICE_URLS

@main_router.message(Command("check_active_orders"))
async def check_active_orders(message: types.Message) -> None:
    # TODO
    # Решить, где фильтровать активные заказы от выполненных
    adress = f'{SERVICE_URLS[0]}/...'
    data = {
        ...
    }
    response = requests.post(adress, data=data)
    if response.status_code == 200:
        data = response.json()
        msg_text = "e\n"
        for k in data.keys():
            msg_text += f"'{k}': {data[k]}"
    await message.answer(msg_text)
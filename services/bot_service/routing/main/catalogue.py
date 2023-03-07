from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import requests

from routers import main_router
from consts import SERVICE_URLS

@main_router.message(Command("catalogue"))
async def catalogue(message: types.Message) -> None:
    # TODO
    # Проверить, будет ли обнуляться 
    # await state.clear()
    adress = f'{SERVICE_URLS[1]}/...'
    data = {
        ...
    }
    response = requests.post(adress, data=data)
    if response.status_code == 200:
        msg_text = "e\n"
        for k in data.keys():
            msg_text += f"'{k}': {data[k]}"
            # TODO 
            # Понять, как правильно парсить запрос и в зависимости от этого генерить сообщение
            # Здесь будет сообщение с 10 цветками
            # Для просмотра остальных цветов будет использоваться reply markup
    await message.answer(msg_text)
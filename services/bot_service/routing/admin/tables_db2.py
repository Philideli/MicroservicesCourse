from aiogram import types
from aiogram.filters import Command
import requests

from routers import admin_router
from consts import Adresses

@admin_router.message(Command("tables_db2"))
async def start(message: types.Message) -> None:
    adress = Adresses.Tables.db2
    response = requests.get(adress)

    if response.status_code == 200:
        data = response.json()
        msg_text = ""
        for table in data:
            msg_text += f"{table}\n"
    
    else:
        msg_text = f"Відбулась помилка ({response.status_code}) при отриманні даних для каталогу. " \
                    "Повторіть спробу або зверніться до адміністратора боту"
    return await message.answer(msg_text)
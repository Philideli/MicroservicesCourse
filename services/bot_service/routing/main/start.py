from aiogram import types
from aiogram.filters import Command

from routers import main_router
from consts import ADMINS

@main_router.message(Command("start"))
async def start(message: types.Message) -> None:
    msg_text = "Вітаємо вас у каталозі магазину квітів Мікрон\n" \
               "\n" \
               "/start - повідомлення із списком команд\n" \
               "/cancel - відмінити ввід даних у боті\n" \
               "/catalogue - переглянути каталог квітів\n" \
               "/register - зареєструватись в боті для створення замовлень\n" \
               "/my_orders - переглянути свої замовлення"
    if message.from_user.id in ADMINS:
        msg_text += "\n\n" \
                    "### Команди адміністратора ###\n" \
                    "Поки ще не створили :р"
    await message.answer(msg_text)
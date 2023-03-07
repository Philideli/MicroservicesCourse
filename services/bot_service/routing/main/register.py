from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from re import match

from routers import main_router
from consts import DB1_ADRESS

class EmailInput(StatesGroup):
    email = State()

@main_router.message(Command("register"))
async def register(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    msg_text = "Будь ласка, введіть свою електронну скриньку"
    await message.answer(msg_text)
    await state.set_state(EmailInput.email)

@main_router.message(EmailInput.email)
async def email_recieved(message: types.Message, state: FSMContext):
    regex = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    if match(regex, message.text):
        email = await state.get_data(EmailInput.email)
        await state.clear()
        adress = f"{DB1_ADRESS}/clients/add"
        data = {
            "id": str(message.from_user.id),
            "name": message.from_user.username,
            "email": email
        }
        status = status = requests.post(adress, data=data).status_code
        
        if status == 200:
            msg_text = "Все, ми вас успішно додали до бази користувачів. Насолоджуйтесь нашими послугами :)"
        else:
            msg_text = f"Відбулась помилка ({status}) при додаванні вас до Бази Даних. Повторіть спробу або зверніться до адміністратора боту"
    else:
        msg_text = "Ви ввели недійсну електронну скриньку\n" \
                   "\n" \
                   "Для відміни дії скористайтесь /cancel"

    await message.answer(msg_text)
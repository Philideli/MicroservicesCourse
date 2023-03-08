from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from re import match

from routers import main_router
from consts import Adresses

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
    # email regex
    regex = r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    if match(regex, message.text):
        await state.clear()

        email = message.text
        adress = Adresses.Clients.add
        data = {
            "id": str(message.from_user.id),
            "name": message.from_user.username,
            "email": email
        }
        status = requests.post(adress, json=data).status_code
        
        if status == 200:
            # Successfully added user to the DB
            msg_text = f"Все, ми вас ({email}) успішно додали до бази користувачів. " \
                        "Насолоджуйтесь нашими послугами :)"
        else:
            # Failed to add user to DB for some reason
            msg_text = f"Відбулась помилка ({status}) при додаванні вас до Бази Даних. " \
                        "Повторіть спробу або зверніться до адміністратора боту"
    else:
        # Wrong input
        msg_text = "Ви ввели недійсну електронну скриньку\n" \
                   "\n" \
                   "Для відміни дії скористайтесь /cancel"

    await message.answer(msg_text)
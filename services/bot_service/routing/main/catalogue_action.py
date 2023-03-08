from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests

from routers import main_router
from consts import Adresses
from callback_data import catalogue, switch
from .catalogue_gen import gen_catalogue

# Arrows are pressed
@main_router.callback_query(switch.SwitchCallbackFactory.filter())
async def catalogue_message(
        callback: types.CallbackQuery, 
        callback_data: switch.SwitchCallbackFactory
):
    prev_page = callback_data.page
    prev_way = callback_data.way
    page = prev_page+1 if prev_way == "forward" else prev_page-1
    await gen_catalogue(callback.message, page)


class AmountInput(StatesGroup):
    item_id = State()
    item_name = State()
    amount = State()

# Numbers are pressed
@main_router.callback_query(catalogue.CatalogueCallbackFactory.filter())
async def view_flower(
        callback: types.CallbackQuery, 
        callback_data: catalogue.CatalogueCallbackFactory,
        state: FSMContext
):
    msg_text = f"Квітка {callback_data.name}. Найкраще вічуває себе у кліматі {callback_data.climate}\n" \
               f"Коштує {callback_data.price}$. Скільки ви хочете придбати?\n" \
                "\n"\
                "Для відміни дії скористайтесь /cancel"
    await callback.message.answer(msg_text)
    await state.update_data(
        item_id=callback_data.id,
        item_name=callback_data.name
    )
    await state.set_state(AmountInput.amount)

@main_router.message(AmountInput.amount)
async def amount_recieved(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        state_data = await state.get_data()
        await state.clear()

        adress = Adresses.Orders.add
        data = {
            "client_id": str(message.from_user.id),
            "item_id": str(state_data["item_id"]),
            "amount": str(message.text)
        }
        status = requests.post(adress, json=data).status_code
        
        if status == 200:
            # Successfully added user to the DB
            msg_text = f"{message.text} {state_data['item_name']} було успішно замовлено. " \
                        "Сподіваємося, ви й надалі будете купляти наші квіти!\n" \
                        "\n" \
                        "Список ваших замовлень можна переглянути у /my_orders"
        else:
            # Failed to add user to DB for some reason
            msg_text = f"Відбулась помилка ({status}) при створенні замовлення. " \
                        "Повторіть спробу або зверніться до адміністратора боту"
    else:
        # Wrong input
        msg_text = "Ви ввели не кількість квітів для замовлення\n" \
                   "\n" \
                   "Для відміни дії скористайтесь /cancel"
    await message.answer(msg_text)
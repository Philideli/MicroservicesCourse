from aiogram import types
from aiogram.filters import Command
import requests

from routers import main_router
from consts import Adresses

@main_router.message(Command("my_orders"))
async def my_orders(message: types.Message) -> None:
    adress = Adresses.Orders.get_by_client
    request_data = {
        "clientId": str(message.from_user.id)
    }
    response = requests.get(adress, json=request_data)
    
    if response.status_code == 200:
        order_data = response.json()

        msg_text = f"Замовлення користувача {message.from_user.username}:\n"
        i = 1
        for order in order_data:
            adress = Adresses.Flowers.get_by_id
            request_data = {
                "id": str(order["item_id"])
            }
            response = requests.get(adress, json=request_data)
            
            if response.status_code == 200:
                flower_data = response.json()[0]
                msg_text += f"{i}. {flower_data[1]} x{order['amount']}\n"
            else:
                msg_text = f"Виникла помилка ({response.status_code}) при отриманні ваших замовлень. " \
                            "Повторіть спробу або зверніться до адміністратора боту"
                break
            i+=1
    else:
        msg_text = f"Виникла помилка ({response.status_code}) при отриманні ваших замовлень. " \
                    "Повторіть спробу або зверніться до адміністратора боту"
    await message.answer(msg_text)
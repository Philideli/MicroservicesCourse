from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests

from consts import Adresses, INT2EMOJI
from callback_data import catalogue, switch

async def gen_catalogue(message:types.Message, page:int):
    adress = Adresses.Flowers.get_all
    response = requests.get(adress)

    if response.status_code == 200:
        data = response.json()
        msg_text = f"Каталог квітів, сторінка {page}\n"
        builder = InlineKeyboardBuilder()
        for i in range((page-1)*10, page*10):
            if len(data) == i:
                # Чем ближе дедлайн, тем больше костылей
                i-=1
                break
            # flower = { climate, color, id, name, price }
            flower = data[i]
            msg_text += f"\n{i+1}. {flower['name']}, коштує {flower['price']}$"
            builder.button(
                text=INT2EMOJI[i%10+1], callback_data=catalogue.CatalogueCallbackFactory(
                    climate=flower["climate"],
                    id=flower["id"],
                    name=flower["name"],
                    price=flower["price"]
                    )
                )
        # Backwards button
        if page == 1:
            builder.button(text="⬅️", callback_data="a")
        else:
            builder.button(
                    text="⬅️", callback_data=switch.SwitchCallbackFactory(
                        page=page, way="backwards"
                )
            )
        # Forward button
        if page*10 > len(data):
            builder.button(text="➡️", callback_data="a")
        else:
            builder.button(
                    text="➡️", callback_data=switch.SwitchCallbackFactory(
                        page=page, way="forward"
                )
            )
            
        # Determine button placement
        i = i%10+1
        builder.adjust(i,2) if i <= 5 else builder.adjust(5,i-5,2)
        
        return await message.answer(msg_text, reply_markup=builder.as_markup())
    else:
        msg_text = f"Відбулась помилка ({response.status_code}) при отриманні даних для каталогу. " \
                    "Повторіть спробу або зверніться до адміністратора боту"
        return await message.answer(msg_text)
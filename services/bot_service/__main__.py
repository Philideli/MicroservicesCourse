import asyncio
import logging

from consts import dp, bot
from routers import main_router, admin_router
import routing


async def main():

    dp.include_router(main_router)
    main_router.include_router(admin_router)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    asyncio.run(main())

# TODO
# 1. Добавить АПИ для удаления пользователя из БД
# 2. Доделать команды для второго микросервиса
# 3. Избавиться от "id" в АПИ первого микросервиса на add_order()
# 3.1. Убрать "id" в функции, заменив на автоинкремент в БД
# 3.2. Прикреплять к ответу айдишник созданной записи
# 4. Понять, как правильно парсить HTTP-ответы
# 5. Проверить, будет ли обнуляться FSMContext, если его не передавать в функцию команды
# 6. Добавить поле статуса "выполнено/невыполнено" в таблицу Orders
# 6.1. Добавить функцию в АПИ для получения только "невыполненных" заказов
# (хотя, я не знаю, фильтровать лучше будет на уровне АПИ или бота)
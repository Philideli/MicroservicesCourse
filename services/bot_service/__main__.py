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
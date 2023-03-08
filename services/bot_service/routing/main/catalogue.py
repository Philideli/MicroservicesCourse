from aiogram import types
from aiogram.filters import Command

from routers import main_router
from .catalogue_gen import gen_catalogue

@main_router.message(Command("catalogue"))
async def catalogue(message: types.Message) -> None:
    await gen_catalogue(message, 1)
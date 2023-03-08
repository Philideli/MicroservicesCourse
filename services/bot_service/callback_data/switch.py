from aiogram import types
from aiogram.filters.callback_data import CallbackData

class SwitchCallbackFactory(CallbackData, prefix="switch"):
    page: int
    way: str
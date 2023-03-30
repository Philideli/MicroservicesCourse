from aiogram.types import URLInputFile
from aiogram.filters.callback_data import CallbackData

class CatalogueCallbackFactory(CallbackData, prefix="catalogue"):
    flower_id: int
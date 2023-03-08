from aiogram.filters.callback_data import CallbackData

class CatalogueCallbackFactory(CallbackData, prefix="catalogue"):
    climate: str
    id: int
    name: str
    price: int
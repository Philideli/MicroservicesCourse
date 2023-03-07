from aiogram import Bot, Dispatcher

from config import token

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

ADMINS = [
    448565207   # @boryaxta
]

BASE_URL = "http://localhost"
SERVICE_PORTS = [
    8080,   # Users and orders
    0000    # Catalogue
]
SERVICE_URLS = []
for port in SERVICE_PORTS:
    SERVICE_URLS.append(f"{BASE_URL}:{port}")
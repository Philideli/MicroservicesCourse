from aiogram import Bot, Dispatcher

from config import token

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

ADMINS = [
    448565207   # @boryaxta
]

MINIKUBE_IP = "192.168.49.2"
DB1_ADRESS = f"http://{MINIKUBE_IP}:31317"
DB2_ADRESS = f"http://{MINIKUBE_IP}:xxxxx"
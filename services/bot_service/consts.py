from aiogram import Bot, Dispatcher

from config import token

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

ADMINS = [
    448565207   # @boryaxta
]

DB1_ADRESS = "http://db1-service/api/db1"
DB2_ADRESS = "http://db2-service/api/db2"
class Adresses:
    class Clients:
        """Database 1 tables"""
        add = DB1_ADRESS + "/clients/add"
        get_by_id = DB1_ADRESS + "/clients/getbyid"
        get_all = DB1_ADRESS + "/clients/getall"
    
    class Orders:
        """Database 1 tables"""
        add = DB1_ADRESS + "/orders/add"
        get_by_id = DB1_ADRESS + "/orders/getbyid"
        get_by_client = DB1_ADRESS + "/orders/getbyclient"
        get_all = DB1_ADRESS + "/orders/getall"
    
    class Flowers:
        """Database 2 tables"""
        add = DB2_ADRESS + "/flowers/add"
        get_by_id = DB2_ADRESS + "/flowers/getbyid"
        get_by_name = DB2_ADRESS + "/flowers/getbyname"
        get_all = DB2_ADRESS + "/flowers/getall"
    
    class Tables:
        db1 = None
        db2 = DB2_ADRESS + "/db2/tables"

INT2EMOJI = [
    '0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟'
]
from mock_input import clients, orders
import sqlite3

class Client:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Order:
    def __init__(self, client_id, item_id, amount):
        self.client_id = client_id
        self.item_id = item_id
        self.amount = amount
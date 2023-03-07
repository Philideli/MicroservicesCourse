from mock_input import clients, orders
import sqlite3

class Client:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Order:
    def __init__(self, id, client_id, items):
        self.id = id
        self.client_id = client_id
        self.items = items
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

class SalesRepository:
    def __init__(self):
        self.conn = sqlite3.connect('sales.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, client_id INTEGER, items TEXT)')
    
    def add_client(self, client):
        self.cursor.execute('INSERT INTO clients (id, name, email) VALUES (?, ?, ?)', (client.id, client.name, client.email))
        self.conn.commit()
    
    def get_all_clients(self):
        self.cursor.execute('SELECT id, name, email FROM clients')
        rows = self.cursor.fetchall()
        clients = [Client(*row) for row in rows]
        return clients

    def get_client_by_id(self, client_id):
        self.cursor.execute("SELECT * FROM orders WHERE id=?", (client_id,))
        client = self.cursor.fetchall()
        if client is not None:
            return Client(*client)
        else:
            return None
    
    def add_order(self, order):
        self.cursor.execute('INSERT INTO orders (id, client_id, items) VALUES (?, ?, ?)', (order.id, order.client_id, str(order.items)))
        self.conn.commit()
    
    def get_all_orders(self):
        self.cursor.execute('SELECT id, client_id, items FROM orders')
        rows = self.cursor.fetchall()
        orders = [Order(*row) for row in rows]
        return orders

    def get_all_orders_for_client(self, client_id):
        self.cursor.execute("SELECT * FROM orders WHERE client_id=?", (client_id,))
        rows = self.cursor.fetchall()
        orders = [Order(*row) for row in rows]
        return orders

    def get_order_by_id(self, order_id):
        self.cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
        order = self.cursor.fetchall()
        if order is not None:
            return Order(*order)
        else:
            return None
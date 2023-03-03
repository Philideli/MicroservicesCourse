from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

class Client:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class ClientRepository:
    def __init__(self):
        self.conn = sqlite3.connect('clients.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    
    def add(self, client):
        self.cursor.execute('INSERT INTO clients (id, name, email) VALUES (?, ?, ?)', (client.id, client.name, client.email))
        self.conn.commit()
    
    def get_all(self):
        self.cursor.execute('SELECT id, name, email FROM clients')
        rows = self.cursor.fetchall()
        clients = [Client(*row) for row in rows]
        return clients

    def get_by_id(self, client_id):
        self.cursor.execute("SELECT * FROM orders WHERE id=?", (client_id,))
        client = self.cursor.fetchall()
        if client is not None:
            return client.to_dict()
        else:
            return None

class Order:
    def __init__(self, id, client_id, items):
        self.id = id
        self.client_id = client_id
        self.items = items

class OrderRepository:
    def __init__(self):
        self.conn = sqlite3.connect('orders.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, client_id INTEGER, items TEXT)')
    
    def add(self, order):
        self.cursor.execute('INSERT INTO orders (id, client_id, items) VALUES (?, ?, ?)', (order.id, order.client_id, str(order.items)))
        self.conn.commit()
    
    def get_all(self):
        self.cursor.execute('SELECT id, client_id, items FROM orders')
        rows = self.cursor.fetchall()
        orders = [Order(*row) for row in rows]
        return orders

    def get_all_orders_for_client(self, client_id):
        self.cursor.execute("SELECT * FROM orders WHERE client_id=?", (client_id,))
        orders = self.cursor.fetchall()
        return orders

    def get_by_id(self, order_id):
        self.cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
        order = self.cursor.fetchall()
        if order is not None:
            return order.to_dict()
        else:
            return None


client_repo = ClientRepository()
order_repo = OrderRepository()

@app.route('/clients/add', methods=['POST'])
def add_client():
    client = request.get_json()
    if not client or 'id' not in client or 'name' not in client or 'email' not in client:
        return jsonify({'error': 'Invalid request'}), 400
    client = Client(client['id'], client['name'], client['email'])
    client_repo.add(client)
    
    return jsonify({'message': 'Client added successfully'}), 200

@app.route('/get/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = client_repo.get_by_id(client_id)
    if client is not None:
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route('/clients/getall', methods=['GET'])
def get_all_clients():
    clients = [vars(client) for client in client_repo.get_all()]
    return jsonify(clients), 200

@app.route('/orders/add', methods=['POST'])
def add_order():
    order = request.get_json()
    if not order or 'id' not in order or 'client_id' not in order or 'items' not in order:
        return jsonify({'error': 'Invalid request'}), 400
    order = Order(order['id'], order['client_id'], order['items'])
    order_repo.add(order)
    return jsonify({'message': 'Order added successfully'}), 200

@app.route('/get/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = order_repo.get_by_id(order_id)
    if order is not None:
        return jsonify(order), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/getall', methods=['GET'])
def get_all_orders():
    orders = [vars(order) for order in order_repo.get_all()]
    return jsonify(orders), 200

@app.route('/clients/<int:client_id>/orders', methods=['GET'])
def get_all_orders_for_client(client_id):
    try:
        orders = [vars(order) for order in order_repo.get_all_orders_for_client(client_id)]
        if orders:
            return jsonify(orders), 200
        else:
            return jsonify({'message': f'No orders found for client {client_id}'}), 200
    except:
        return jsonify({'error': 'An error occurred while retrieving the orders'}), 500

if __name__ == '__main__':
    app.run(port=8080)

from flask import Flask, jsonify, request, g
import sqlite3
from time import sleep

from sales_database import Client, Order
from mock_input import clients, orders

SERVICE_NAME = "db1"
PREFIX = "/api/" + SERVICE_NAME

app = Flask(SERVICE_NAME)

def get_db_connection():
    conn = getattr(g,'_database',None)
    if conn is None:
        conn = g._database = sqlite3.connect('sales.db')
    return conn

@app.route(PREFIX + '/')
def start_point():
    return "Start service 1 for clients and orders"

@app.route(PREFIX + '/clients/add', methods=['POST'])
def add_client():
    """ add new client to database
        Args:
            client (dict): with following fields
                id (int): client id
                name (str): client name
                email (str): client email
        Returns:
            message (json): response message
            response code
    """
    client = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    if not client or 'id' not in client or 'name' not in client or 'email' not in client:
        return jsonify({'error': 'Invalid request'}), 400
    client = Client(client['id'], client['name'], client['email'])
    cursor.execute('INSERT INTO clients (id, name, email) VALUES (?, ?, ?)', (client.id, client.name, client.email))
    db.commit()
    
    return jsonify({'message': 'Client added successfully'}), 200

@app.route(PREFIX + '/clients/getbyid', methods=['GET'])
def get_client():
    """ get client by id from database
        Args:
            clientId (str): client id
        Returns:
            client (json): client from database
            response code
    """
    args = request.args
    client_id = args.to_dict()['clientId']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clients WHERE id=?", (client_id,))
    client = cursor.fetchall()
    if client:
        clients = [Client(*row) for row in client]
        clients = [vars(client) for client in clients]
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route(PREFIX + '/clients/getall', methods=['GET'])
def get_all_clients():
    """ get all clients from database
        Returns:
            clients (json): all the retrieved clients from database
            response code
    """
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT id, name, email FROM clients')
    rows = cursor.fetchall()
    clients = [Client(*row) for row in rows]
    clients = [vars(client) for client in clients]
    return jsonify(clients), 200

@app.route(PREFIX + '/orders/add', methods=['POST'])
def add_order():
    """ add new order to database
        Args:
            order (dict): with following fields
                client_id (int): client id
                item_id (int): item from the order
                amount (int): amount of flowers
        Returns:
            message (json): response message
            response code
    """
    order = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    if not order or 'client_id' not in order or 'item_id' not in order or 'amount' not in order:
        return jsonify({'error': 'Invalid request'}), 400
    order = Order(order['client_id'],order['item_id'],order['amount'])
    cursor.execute('INSERT INTO orders (client_id, item_id, amount) VALUES (?, ?, ?)',
                   (order.client_id, order.item_id, order.amount))
    db.commit()
    return jsonify({'message': 'Order added successfully'}), 200

@app.route(PREFIX + '/orders/getbyid', methods=['GET'])
def get_order():
    """ get order by id from database
        Args:
            orderId (str): order id
        Returns:
            order (json): order from database
            response code
    """
    args = request.args
    order_id = args.to_dict()['orderId']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
    order = cursor.fetchall()
    if order:
        orders = [Order(*row) for row in order]
        orders = [vars(order) for order in orders]
        return jsonify(orders), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@app.route(PREFIX + '/orders/getall', methods=['GET'])
def get_all_orders():
    """ get all orders from database
        Returns:
            orders (json): all the retrieved orders from database
            response code
    """
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT id, client_id, items FROM orders')
    rows = cursor.fetchall()
    orders = [Order(*row) for row in rows]
    orders = [vars(order) for order in orders]
    return jsonify(orders), 200

@app.route(PREFIX + '/orders/getbyclient', methods=['GET'])
def get_all_orders_for_client():
    """ get all orders made by the client from database
        Returns:
            orders (json): all the orders clients from database
            response code
    """
    client_id = request.get_json()['clientId']
    db = get_db_connection()
    cursor = db.cursor()
    # try:
    cursor.execute("SELECT client_id, item_id, amount FROM orders WHERE client_id=?", (client_id,))
    rows = cursor.fetchall()
    orders = [Order(*row) for row in rows]
    orders = [vars(order) for order in orders]
    if orders:
        return jsonify(orders), 200
    else:
        return jsonify({'message': f'No orders found for client {client_id}'}), 200
    # except:
    #     return jsonify({'error': 'An error occurred while retrieving the orders'}), 500


""" Lab 4 things """

is_pod_broken = False
BROKEN_POD_COOLDOWN = 10    # in secs

# /api/db1/test
@app.route(PREFIX + '/test')
def start_point():
    if is_pod_broken:
        sleep(BROKEN_POD_COOLDOWN)
        return "Oh no! I am soooooo slow!"
    return "Yup, im completely fine and fast guy"

# /api/db1/break
@app.route(PREFIX + '/break')
def start_point():
    if is_pod_broken:
        is_pod_broken = True
        return "Pod was successfully broken"
    else:
        is_pod_broken = False
        return "Pod was successfully fixed"


if __name__ == '__main__':
    # this port parameter doesn't do SHIT
    app.run(port=5000)
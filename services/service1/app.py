from flask import Flask, jsonify, request
from sales import SalesRepository, Client, Order

app = Flask('service1')

sales_repo = SalesRepository()

@app.route('/clients/add', methods=['POST'])
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
    if not client or 'id' not in client or 'name' not in client or 'email' not in client:
        return jsonify({'error': 'Invalid request'}), 400
    client = Client(client['id'], client['name'], client['email'])
    sales_repo.add_client(client)
    
    return jsonify({'message': 'Client added successfully'}), 200

@app.route('/clients/get_by_id?<int:client_id>', methods=['GET'])
def get_client(client_id):
    """ get client by id from database
        Args:
            client_id (str): client id
        Returns:
            client (json): client from database
            response code
    """
    client = sales_repo.get_client_by_id(client_id)
    if client is not None:
        return jsonify(client), 200
    else:
        return jsonify({'error': 'Client not found'}), 404

@app.route('/clients/getall', methods=['GET'])
def get_all_clients():
    """ get all clients from database
        Returns:
            clients (json): all the retrieved clients from database
            response code
    """
    clients = [vars(client) for client in sales_repo.get_all_clients()]
    return jsonify(clients), 200

@app.route('/orders/add', methods=['POST'])
def add_order():
    """ add new order to database
        Args:
            order (dict): with following fields
                id (int): order id
                client_id (int): client id
                items (str): items from the order
        Returns:
            message (json): response message
            response code
    """
    order = request.get_json()
    if not order or 'id' not in order or 'client_id' not in order or 'items' not in order:
        return jsonify({'error': 'Invalid request'}), 400
    order = Order(order['id'], order['client_id'], order['items'])
    sales_repo.add_order(order)
    return jsonify({'message': 'Order added successfully'}), 200

@app.route('/get/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """ get order by id from database
        Args:
            order_id (str): order id
        Returns:
            order (json): order from database
            response code
    """
    order = sales_repo.get_order_by_id(order_id)
    if order is not None:
        return jsonify(order), 200
    else:
        return jsonify({'error': 'Order not found'}), 404

@app.route('/orders/getall', methods=['GET'])
def get_all_orders():
    """ get all orders from database
        Returns:
            orders (json): all the retrieved orders from database
            response code
    """
    orders = [vars(order) for order in sales_repo.get_all_orders()]
    return jsonify(orders), 200

@app.route('/clients/<int:client_id>/orders', methods=['GET'])
def get_all_orders_for_client(client_id):
    """ get all orders made by the client from database
        Returns:
            orders (json): all the orders clients from database
            response code
    """
    try:
        orders = [vars(order) for order in sales_repo.get_all_orders_for_client(client_id)]
        if orders:
            return jsonify(orders), 200
        else:
            return jsonify({'message': f'No orders found for client {client_id}'}), 200
    except:
        return jsonify({'error': 'An error occurred while retrieving the orders'}), 500

if __name__ == '__main__':
    app.run(port=8080)

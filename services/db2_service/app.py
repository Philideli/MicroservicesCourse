from flask import Flask, jsonify, request, g
import psycopg2
from flower import Flower

app = Flask('service2')

def get_db_connection():
    conn = psycopg2.connect(
        database="flowers", user='demo', password='demo', host="postgres", port='5432'
    )
    return conn


@app.route('/')
def start_point():
    return "Start service 2 for flowers"


@app.route('/flowers/getbyid', methods=['GET'])
def get_flower_by_id():
    """
    :id (str): flower id
    :return 1: flower info (json)
    :return 2: error message (json)
    """
    flower_id = request.get_json()['id']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(f'SELECT id, "name", color, climate, price, image FROM flower WHERE id={flower_id}')
    flower = cursor.fetchall()
    if flower:
        flowers = [Flower(*row) for row in flower]
        flowers = [vars(flower) for flower in flowers]
        return jsonify(flower), 200
    else:
        return jsonify({'error': 'Flower not found'}), 404


@app.route('/flowers/getbyname', methods=['GET'])
def get_flower_by_name():
    """
    :name (str): flower name
    :return 1: flower data (json)
    :return 2: error message (json)
    """
    args = request.args
    flowerName = args.to_dict()['flowerName']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM flower WHERE "name"=?', (flowerName,))
    flower = cursor.fetchall()
    if flower:
        flowers = [Flower(*row) for row in flower]
        flowers = [vars(flower) for flower in flowers]
        return jsonify(flower), 200
    else:
        return jsonify({'error': 'Flower not found'}), 404


@app.route('/flowers/add', methods=['POST'])
def add_flower():
    """
    :flower (dict): flower (id, name, color, climate, price, image)
    :return 1: error message (json)
    :return 2: success message (json)
    """
    flower = request.get_json()
    db = get_db_connection()
    cursor = db.cursor()
    if not flower or 'id' not in flower or 'name' not in flower or 'price' <= 0:
        return jsonify({'error': 'Invalid request'}), 400
    flower = Flower(flower['id'], flower['name'], flower['color'],
                    flower['climate'], flower['price'], flower['image'])
    cursor.execute('INSERT INTO flower (id, "name", color, climate, price) VALUES (?, ?, ?, ?, ?, ?)',
                   (flower.id, flower.name, flower.color, flower.climate, flower.price, flower.image))
    db.commit()

    return jsonify({'message': 'Flower added successfully'}), 200


@app.route('/flowers/getall', methods=['GET'])
def get_all_flowers():
    """
    :return: all flowers (json)
    """
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute('SELECT id, name, color, climate, price, image FROM flower')
    rows = cursor.fetchall()
    flowers = [Flower(*row) for row in rows]
    flowers = [vars(flower) for flower in flowers]
    return jsonify(flowers), 200


@app.route('/db2/tables', methods=['GET'])
def get_tables():
    """
    :return: all tables (json)
    """
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    rows = cursor.fetchall()
    return jsonify(rows), 200


if __name__ == '__main__':
    app.run(port=8080)

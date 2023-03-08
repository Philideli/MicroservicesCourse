from mock_input import clients, orders
import sqlite3

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, client_id INTEGER, items TEXT)')
cursor.executemany('INSERT INTO clients values (?,?,?)', clients)
cursor.executemany('INSERT INTO orders values (?,?,?,?)', orders)
conn.commit()
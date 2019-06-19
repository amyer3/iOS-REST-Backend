from flask import abort, jsonify, json
import dbHandler
from sqlite3 import Error
import time
import string
import random
from dao import databaseAccessObject as dao


"""
portfolio (
name text NOT NULL,
ticker text NOT NULL,
num_stocks real NOT NULL,
cost integer NOT NULL,
buy_date int NOT NULL, 
sell_date int NOT NULL,
sell_price real NOT NULL,
txn_id text NOT NULL,
user_id integer NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id)
);
"""
now = int(round(time.time() * 1000))
d = dao.databaseAccess()


def generate_id():
    return str('TXN' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)))


def buy_stock(name, ticker, num_stocks, price, user_id):
    thisID = generate_id()
    try:
        d.insert("""
        INSERT INTO portfolio (name, ticker, num_stocks, cost, buy_date, txn_id, user_id) VALUES 
        (?, ?, ?, ?, ?, ?, ?);""", (name, ticker, num_stocks, price, now, thisID, user_id))
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}


def sell_stock(txn_id, sell_date, sell_price):
    try:
        d.insert("""
        UPDATE portfolio
        SET
        sell_date = ?,
        sell_price = ?
        WHERE
        txn_id = ?;""", (sell_date, sell_price, txn_id))
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}


def get_stocks(user_id):
    p = []
    try:
        data = d.get_data("SELECT * FROM portfolio WHERE user_id=?;", (user_id,))
        for stock in data:
            td = {
                "name": stock[0],
                "ticker": stock[1],
                "num_stocks": stock[2],
                "opening": 191,
                "closing": 233.11,
                "cost": stock[3],
                "pct": stock[3] / (233.11 * stock[2]),
                "txn_id": stock[7]
            }
            p.append(td)

        return json.dumps({'success': True, "portfolio": {"stocks": p}}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}

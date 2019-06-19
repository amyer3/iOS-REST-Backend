import random
import string
import time
from sqlite3 import Error

from flask import abort, json

import databaseAccessObject as dao

now = int(round(time.time() * 1000))
d = dao.databaseAccess()


def generate_id():
    return str('GOAL' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(60)))


def new_goal(name, price, added_funds, logo, proj_completion, user_id):
    try:
        this_id = generate_id()
        d.insert("""
        INSERT INTO goals (name, price, added_funds, logo, goal_id, date_started, proj_completion, completed, user_id, closed) VALUES 
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (name, price, added_funds, "", this_id, now, proj_completion, 0, user_id, 0))
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    except Error as e:
        print("New Goal Error %s" % e)
        abort(404)


def add_to_goal(goal_id, added_funds):
    try:
        d.insert("""UPDATE goals SET added_funds = added_funds + ? WHERE goal_id = ?;""", (added_funds, goal_id))
        d.insert("""INSERT INTO goal_log(goal_id, date, added_funds) VALUES (?,?,?);""", (goal_id, now, added_funds))
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}


def get_goals(user_id):
    try:
        data = d.get_data("""SELECT * FROM goals WHERE user_id = ?;""", (user_id,))
        g = []
        for goal in data:
            td = {
                "name": goal[0],
                "price": goal[1],
                "added_funds": goal[2],
                "logo": goal[3],
                "goal_id": goal[4]
            }
            g.append(td)
        print(data)

        return json.dumps({'success': True, "goals": g}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}


def delete_goal(goal_id):
    try:
        d.insert("""UPDATE portfolio SET closed = 1, date_close = ? WHERE goal_id = ?;""", (now, goal_id))
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}

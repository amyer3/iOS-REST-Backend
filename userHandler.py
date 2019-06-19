import random
import string
import time
from sqlite3 import Error

from flask import json

import databaseAccessObject as dao


def generate_id():
    return str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32)))


def new_basic_user():
    d = dao.databaseAccess()
    id = generate_id()
    now = int(round(time.time()*1000))
    try:
        d.insert("INSERT INTO users (id, date_created) VALUES (?, ?);", (id, now))
        return json.dumps({'success': True, "user_id": id}), 201, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}




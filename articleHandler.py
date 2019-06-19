from sqlite3 import Error

from flask import json

import databaseAccessObject as dao

d = dao.databaseAccess()


def get_articles():
    try:
        d.get_data("""SELECT * FROM articles;""", )
        print(d)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}

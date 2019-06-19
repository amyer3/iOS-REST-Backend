from flask import jsonify, abort, json
from sqlite3 import Error
import dbHandler
from dao import databaseAccessObject as dao


d = dao.databaseAccess()


def get_nonprofts():
    try:
        d.get_data("""SELECT * FROM nonprofit;""", )
        print(d)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}

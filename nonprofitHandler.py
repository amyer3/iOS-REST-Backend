from flask import jsonify, abort, json
from sqlite3 import Error
import dbHandler
from dao import databaseAccessObject as dao

nonprofits = [
        {
            "name": "Red Cross",
            "subtitle": "Helping others in need",
            "logo": "cross",
            "category": "Disaster Relief"
        },

        {
            "name": "United Negro College Fund",
            "subtitle": "A mind is a terrible thing to waste.",
            "logo": "torch",
            "category": "Scholarship Fund"
         },
        {
            "name": "St. Jude Children’s Research Hospital",
            "subtitle": "Finding cures.  Saving children.",
            "logo": "child",
            "category": "Medical Research"
         },
        {
            "name": "Boys & Girls Clubs of America",
            "subtitle": "Clubs Change Lives.",
            "logo": "handshake",
            "category": "Youth Organization"
         },
        {
            "name": "Hispanic Federation",
            "subtitle": " To empower and advance the Hispanic community.",
            "logo": "circles",
            "category": "Advocacy"
         },
        {
            "name": "United Way",
            "subtitle": "The United Way advances the common good in communities across the world.",
            "logo": "hand",
            "category": "Community Improvement"
         }
    ]
d = dao.databaseAccess()


def get_nonprofts():
    try:
        d.get_data("""SELECT * FROM nonprofit;""", )
        print(d)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}

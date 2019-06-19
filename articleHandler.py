from flask import jsonify, json, abort
from sqlite3 import Error
from dao import databaseAccessObject as dao

article = [
        {
        "title": "So what is a stock?",
        "id": 1010101,
        "status": 0,
        "lede": "AAPL",
        "brief": "<b>Here we try provide the basics of a stock.</b>",
        "author": "Sean",
        "date": "9/20/18",
        "image": "NaN",
        "preview_image": "NaN",
        "special_id": 0,
        "text": "<p>Ever wondered what a stock is?</p> <p>Think about it this way; if we bought one stock in Apple (AAPL) we are now are owners.  Congratulations!  You are now the owner of the biggest company on the planet, well you and the other millions of Apple stockholders.  So now what?</p> <p>Well as a stock owner there are a couple of things.  First, at any point, you can sell.  Second, as an owner, you have a say in the company’s future through voting.  Third, the value of your stock depends on the company’s and economic news.  Good news increases the value, and bad news decreases it.  Fourth, when the company we own does well, management will share some of their earnings by issuing a dividend.  Investors have the option of cashing out their dividend or reinvesting it in the company to buy more shares.  Finally, if the company goes bankrupt, stockholders are the last to get paid because we are owners – the captain must go down with the ship.</p>"
    }
]
d = dao.databaseAccess()


def get_articles():
    try:
        d.get_data("""SELECT * FROM articles;""", )
        print(d)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    except Error as e:
        return json.dumps({'success': False, "error": e}), 422, {'ContentType': 'application/json'}
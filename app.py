#!flask/bin/python
from flask import Flask, jsonify, abort, request
import articleHandler
import nonprofitHandler
import portfolioHandler
import goalsHandler
import userHandler
import sqlite3


app = Flask(__name__)


@app.route('/loop/app/api/v1/newuser', methods=['POST'])
def add_user():
    user = userHandler.new_basic_user()
    print(request.form)
    return user


@app.route('/loop/app/api/v1/<string:user_id>/portfolio', methods=['GET'])
def get_portfolio(user_id):
    portfolio = portfolioHandler.get_stocks(user_id)
    return portfolio


@app.route('/loop/app/api/v1/<string:user_id>/portfolio', methods=['POST'])
def buy_stock(user_id):
    name = request.get_json()['name']
    ticker = request.get_json()['ticker']
    num_stocks = request.get_json()['num_stocks']
    price = request.get_json()['price']
    portfolio = portfolioHandler.buy_stock(
        name=name,
        ticker=ticker,
        num_stocks=num_stocks,
        price=price,
        user_id=user_id
    )
    return portfolio


@app.route('/loop/app/api/v1/<string:user_id>/portfolio/<string:txn_id>', methods=['PUT'])
def sell_stock(txn_id):
    portfolio = portfolioHandler.sell_stock()
    return portfolio


@app.route('/loop/app/api/v1/<string:user_id>/goals/newgoal', methods=['POST'])
def new_goal(user_id):
    name = request.get_json()['name']
    added_funds = request.get_json()['added_funds']
    proj_completion = request.get_json()['proj_completion']
    price = request.get_json()['price']
    goals = goalsHandler.new_goal(
        name=name,
        price=price,
        added_funds=added_funds,
        logo="",
        proj_completion=proj_completion,
        user_id=user_id
    )
    return goals


@app.route('/loop/app/api/v1/<string:user_id>/goals', methods=['GET'])
def get_goals(user_id):
    goals = goalsHandler.get_goals(user_id)
    return goals


@app.route('/loop/app/api/v1/<string:user_id>/goals/<string:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goals = goalsHandler.delete_goal(goal_id)
    return goals


@app.route('/loop/app/api/v1/<string:user_id>/goals/<string:goal_id>', methods=['PUT'])
def update_goal(user_id, goal_id):
    added_funds = request.get_json()['added_funds']
    goals = goalsHandler.add_to_goal(goal_id, added_funds)
    return goals


@app.route('/loop/app/api/v1/articles', methods=['GET'])
def get_articles():
    articles = articleHandler.get_articles()
    return articles


@app.route('/loop/app/api/v1/nonprofits', methods=['GET'])
def get_nonprofits():
    nonprofits = nonprofitHandler.get_nonprofts()
    return nonprofits


if __name__ == '__main__':
    app.run(debug=True)

import sqlite3
from sqlite3 import Error
import os


class databaseAccess:
    def __init__(self):
        if not os.path.isfile(os.getcwd() + '/data.db'):
            self.connect_and_make_table()

    sql_create_user_table = """CREATE TABLE IF NOT EXISTS users (
                                        id text PRIMARY KEY,
                                        email text,
                                        first_name text, 
                                        last_name text,
                                        date_created int NOT NULL, 
                                        date_closed int
                                    ); """

    sql_create_goals_table = """CREATE TABLE IF NOT EXISTS goals (
                                    name text NOT NULL,
                                    price integer,
                                    added_funds real NOT NULL,
                                    logo text NOT NULL,
                                    goal_id integer NOT NULL,
                                    date_started int NOT NULL,
                                    proj_completion int NOT NULL,
                                    date_close real,
                                    user_id integer NOT NULL,
                                    completed integer NOT NULL,
                                    closed integer,
                                    FOREIGN KEY (user_id) REFERENCES users(id)
                                );"""
    sql_create_goal_log = """CREATE TABLE IF NOT EXISTS goal_log(
                            goal_id integer NOT NULL, 
                            date int NOT NULL,
                            added_funds real NOT NULL,
                            FOREIGN KEY (goal_id) REFERENCES goals(goal_id)
                            );
                            """

    sql_create_portfolio_table = """CREATE TABLE IF NOT EXISTS portfolio (
                                    name text NOT NULL,
                                    ticker text NOT NULL,
                                    num_stocks real NOT NULL,
                                    cost integer NOT NULL,
                                    buy_date int NOT NULL, 
                                    sell_date int,
                                    sell_price real,
                                    txn_id text NOT NULL,
                                    user_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users(id)
                                );"""

    sql_create_nonprofit_table = """CREATE TABLE IF NOT EXISTS nonprofit (
                                    name text NOT NULL,
                                    subtitle text NOT NULL,
                                    logo text NOT NULL,
                                    category text NOT NULL,
                                    unique_key integer NOT NULL
                                );"""

    sql_create_article_table = """CREATE TABLE IF NOT EXISTS articles (
                                    title integer PRIMARY KEY,
                                    status integer,
                                    lede text NOT NULL,
                                    brief text NOT NULL,
                                    author text NOT NULL,
                                    date int NOT NULL, 
                                    image text, 
                                    preview_image text, 
                                    special_id integer, 
                                    body text NOT NULL
                                );"""

    array = [
        sql_create_user_table,
        sql_create_article_table,
        sql_create_nonprofit_table,
        sql_create_portfolio_table,
        sql_create_goals_table,
        sql_create_goal_log
    ]

    def connect_and_make_table(self):
        dir_path = os.getcwd()
        try:
            conn = sqlite3.connect(dir_path + '/data.db')
            for command in self.array:
                try:
                    conn.execute(command)
                    conn.commit()
                except Error as e:
                    print("Creation Error %s" % e)
        except Error as e:
            print("Connection_make_table Error %s " % e)

    def insert(self, statement, tup):
        dir_path = os.getcwd()
        try:
            conn = sqlite3.connect(dir_path + '/data.db')
            cur = conn.cursor()
            cur.execute(statement, tup)
            conn.commit()
        except Error as e:
            print("Data Insertion Error %s on statement %s args %s" % (e, statement, tup))

    def get_data(self, statement, tup):
        dir_path = os.getcwd()
        try:
            conn = sqlite3.connect(dir_path + '/data.db')
            cur = conn.cursor()
            cur.execute(statement, tup)
            d = cur.fetchall()
            print(d)
            return d
        except Error as e:
            print("Data Retrieval Error %s on statement %s args %s" % (e, statement, tup))


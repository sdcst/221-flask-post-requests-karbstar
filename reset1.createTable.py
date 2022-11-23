#!python3


import sqlite3

file = 'quoteholder.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = """
create table if not exists customers (
    id integer primary key autoincrement,
    quote tinytext);
"""
cursor.execute(query)


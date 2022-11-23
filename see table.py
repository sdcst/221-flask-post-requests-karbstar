#!python3
import sqlite3

file = 'quoteholder.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "select quote from customers"
cursor.execute(query)
result = cursor.fetchall()
print('quotes:')
for i in result:
    print(i)
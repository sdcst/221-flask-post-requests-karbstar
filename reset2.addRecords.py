#!python3
import sqlite3

file = 'quoteholder.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()

cursor.execute('delete from customers')

#note, you don't want to delete the table data regularly, this is just for demo purposes

data = [
   'All right, i''ve been thinking, when life gives you lemons, don''t make lemonade! Make life take the lemons back! Get mad! I don''t want your damn lemons! What am I supposed to do with these? Demand to see life''s manager!Make life rue the day it thought it could give Cave Johnson lemons! Do you know who I am? I''m the man whose gonna burn your house down - with the lemons!-cave johnson(portal 2)','Science isn''t about why, it''s about why not.-cave johnson(portal 2)','The definition of ''insanity'' is doing the same thing over and over again and expecting different results-unknown','you shallnot pass-gandaf(lord of the rings)','ascend with Gorb-Gorb(hollow knight)','ogers have layers-Shreak(Shreak)','you are my best friend. i will add a single greain of sand to your room till you succumb to the desert.-pukicho','A-Horror Movie protagonist'
    ]
for i in data:
    query = f"insert into customers (quote) values ('{i}')" 
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)

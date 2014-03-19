import sqlite3
connection = sqlite3.connect('tweetdb.db')

cursor = connection.cursor()
# Create our table
cursor.execute('''CREATE TABLE tweets
             (user text, userid text, content text, coor text, time text, tweetid text)''')

import sqlite3


conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute('''CREATE TABLE weather (city TEXT, temp_now TEXT, max_temp TEXT, min_temp TEXT)''')

c.close()
conn.close()
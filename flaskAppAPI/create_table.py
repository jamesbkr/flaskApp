import psycopg2



connection = psycopg2.connect("dbname='flasks2' user='flasks' host='localhost' password='password'")
cursor = connection.cursor()
# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO users VALUES(1,'admin','password')")
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)
connection.commit()
connection.close()

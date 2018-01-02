import psycopg2

conn = psycopg2.connect("dbname='flasks' user='flasks' host='localhost' password='password'")
cursor = conn.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO users VALUES(1,'frasssnko','password')")
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

conn.commit()

conn.close()

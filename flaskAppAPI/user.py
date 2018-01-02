import psycopg2

class User:
    def __init__(self, _id, username,password):
        self.id= _id
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls, username):
        conn = psycopg2.connect("dbname='flasks2' user='flasks' host='localhost' password='password'")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = psycopg2.connect("dbname='flasks2' user='flasks' host='localhost' password='password'")
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE id=%s"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

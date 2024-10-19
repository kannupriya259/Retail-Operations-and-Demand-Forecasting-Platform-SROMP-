import psycopg2
from psycopg2.extras import RealDictCursor

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="retail_db",
        user="your_username",
        password="your_password"
    )
    return conn

def create_tables():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute(open("db/schema.sql", "r").read())
            conn.commit()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()

from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="exampledb",
                user="postgres",
                password="postgres"
            )
            return conn
        except:
            print("Waiting for database...")
            time.sleep(2)

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT message FROM greetings;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return "<br>".join([row[0] for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
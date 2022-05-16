import sqlite3

from flask import Flask, render_template, request
import traceback

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def setup_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, address TEXT)')
    conn.close()


def insert_user(name, address):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, address) VALUES (?,?)", (name, address))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def fetch_detail():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select * from users")
    rows = cur.fetchall()
    conn.close()
    return rows


@app.route("/photo_resizer")
def photo_resizer():
    return render_template('photo_resizer.html')

@app.route("/")
@app.route("/add_record", methods=['GET', 'POST'])
def add_record():
    setup_db()
    if request.method == 'POST':
        name = request.form['username']
        address = request.form['address']
        insert_user(name, address)
        return render_template('add_record.html', rows=fetch_detail())

    return render_template('home.html', rows=fetch_detail())


if __name__ == '__main__':
    app.run(debug=True)

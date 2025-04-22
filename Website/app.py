from flask import Flask, render_template, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from internal.state_cords import state_coords

load_dotenv(dotenv_path='../.env')

app = Flask(__name__)


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT", "5432")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT name FROM birds ORDER BY name;')
    birds = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return render_template('index.html', birds=birds, state_coords=state_coords)

@app.route('/bird_states/<bird_name>')
def bird_states(bird_name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT state FROM birds WHERE name = %s;", (bird_name,))
    states = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(states=states)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
from flask import Flask, render_template, jsonify
import psycopg2
import os
from dotenv import load_dotenv

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

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path:''):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT name FROM birds ORDER BY name;')
    birds = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()
    return render_template('index.html', birds=birds)

@app.route('/bird/<name>')
def get_bird(name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, scientific_name, observation_count FROM birds WHERE name = %s LIMIT 1;', (name,))
    bird = cur.fetchone()
    cur.close()
    conn.close()
    if bird:
        return jsonify({
            "name": bird[0],
            "scientific_name": bird[1],
            "observation_count": bird[2]
        })
    else:
        return jsonify({"error": "Bird not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

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

    placeholders = ','.join(f"'{state.upper()}'" for state in states) 

    conn = get_db_connection()
    curr2 = conn.cursor()
    curr2.execute(f'''
      WITH input_states AS (
        SELECT UNNEST(ARRAY[{placeholders}]) AS state
      ),
      state_crime_totals AS (
        SELECT nc.state, nc.category, SUM(nc.value) AS total
        FROM normalized_crime nc
        JOIN input_states s ON nc.state = s.state
        WHERE nc.category NOT IN ('total_all_classes', 'other_offenses', 'other_assaults')
        GROUP BY nc.state, nc.category
      ),
      state_top_category AS (
        SELECT DISTINCT ON (state) state, category
        FROM state_crime_totals
        ORDER BY state, total DESC
      ),
      state_count AS (
        SELECT COUNT(*) AS num_states FROM input_states
      ),
      majority_top_category AS (
        SELECT category, COUNT(*) AS freq
        FROM state_top_category
        GROUP BY category
      )
      SELECT 
        CASE 
          WHEN sc.num_states = 1 THEN (SELECT category FROM state_top_category)
          WHEN sc.num_states > 1 THEN (
            SELECT category
            FROM majority_top_category
            WHERE freq > 1
            LIMIT 1
          )
        END AS category
      FROM state_count sc;
    ''')
    top_crime = curr2.fetchone()
    curr2.close()
    conn.close()
    return jsonify(states=states,top_crime=top_crime)

@app.route('/crime/by_bird/<bird_name>/<state_name>')
def crime_states(bird_name,state_name):
    conn = get_db_connection()
    cur = conn.cursor()

    # Now get the crime data for that state, ensuring the 'total_all_classes' category is excluded
    cur.execute("""
        SELECT category, value
        FROM normalized_crime
        WHERE state = (
            SELECT distinct UPPER(state)
            FROM birds
            WHERE name = %s 
            and state = %s
        )
        AND category != 'total_all_classes' and category != 'other_offenses' and category != 'other_assaults'
        ORDER BY value DESC
        LIMIT 1;
    """, (bird_name,state_name,))

    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return jsonify(category=row[0], max_value=row[1])
    else:
        return jsonify(error="No crime data found"), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
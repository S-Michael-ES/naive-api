import psycopg2
from flask import Flask, jsonify

DB_NAME = "naive"
DB_USER = "postgres"
DB_PASS = "14159265"
DB_HOST = "localhost"
DB_PORT = "5432"

app = Flask(__name__)

@app.route('/api/artists')
def get_artists():
    conn = None
    try:
        # Establish the database connection
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()

        # Execute a query
        cur.execute("SELECT artist_id, artist_name FROM artist ORDER BY artist_name;")

        # Fetch the results
        artists_data = cur.fetchall()

        # Close the cursor
        cur.close()

        # Format the data as a list of dictionaries
        artists = []
        for row in artists_data:
            artists.append({'id': row[0], 'name': row[1]})

        # Return the data as a JSON response
        return jsonify(artists)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return jsonify({"error": "Database error"}), 500
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

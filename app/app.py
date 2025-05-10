from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS")
        )
        return "✅ Flask app connected to PostgreSQL!"
    except Exception as e:
        return f"❌ Connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Reuse database connection function
def get_conn():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS")
    )

@app.route("/")
def home():
    try:
        conn = get_conn()
        conn.close()
        return "✅ Connected to DB!"
    except Exception as e:
        return f"❌ Connection failed: {str(e)}"

@app.route("/add", methods=["POST"])
def add_visitor():
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO visitors (name) VALUES (%s)", (name,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": f"Visitor '{name}' added."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/visitors", methods=["GET"])
def get_visitors():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, name, visit_time FROM visitors ORDER BY id DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([
            {"id": r[0], "name": r[1], "visit_time": r[2].isoformat()} for r in rows
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

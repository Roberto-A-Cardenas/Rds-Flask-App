#!/bin/bash
yum update -y
yum install -y python3 git
pip3 install flask psycopg2-binary

cat <<EOF > /home/ec2-user/app.py
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host="${db_host}",
            database="${db_name}",
            user="${db_user}",
            password="${db_pass}"
        )
        return "Connected to DB!"
    except Exception as e:
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
EOF

nohup python3 /home/ec2-user/app.py &

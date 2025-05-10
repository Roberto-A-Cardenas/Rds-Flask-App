CREATE DATABASE flaskdb;

\connect flaskdb

CREATE TABLE visitors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    visit_time TIMESTAMP DEFAULT current_timestamp
);
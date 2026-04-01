import sqlite3
import os

os.makedirs("logs", exist_ok=True)

DB_PATH = "logs/network_logs.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Logs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            ip TEXT,
            status TEXT,
            latency INTEGER,
            packet_loss INTEGER
        )
    ''')

    # Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Default user
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
              ("Nero S", "2705"))

    conn.commit()
    conn.close()


# 🔥 ADD THIS FUNCTION (MISSING)
def insert_log(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''
        INSERT INTO logs (name, ip, status, latency, packet_loss)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data["name"],
        data["ip"],
        data["status"],
        data["latency"],
        data["packet_loss"]
    ))

    conn.commit()
    conn.close()


def validate_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, password))

    user = c.fetchone()
    conn.close()

    return user is not None
import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

c.execute("DELETE FROM users")
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
c.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")

conn.commit()
conn.close()

print("Database initialized successfully.")
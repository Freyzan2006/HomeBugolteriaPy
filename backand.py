import sqlite3

connection = sqlite3.connect('finance.db')
cur = connection.cursor()

def db():

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            amount REAL,
            comment TEXT
        )
    """)

    connection.commit()

def All_info():
    cur.execute("""
        SELECT * FROM transactions
    """)
    rows = cur.fetchall()

    return rows

def add_item(transaction_type, amount, comment):
    cur.execute("""
        INSERT INTO transactions (type, amount, comment)
        VALUES (?, ?, ?)
    """, (transaction_type, amount, comment))
    connection.commit() 
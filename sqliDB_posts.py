import sqlite3

class dataBaseConfig:
    conn: sqlite3.Connection
    c: sqlite3.Cursor
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute("select sql from sqlite_master where type = 'table' and name = 'USER'")
    if not c.fetchall():
        c.execute(''' CREATE TABLE NOTES (
                                             id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                             title TEXT,
                                             note TEXT
                                             )''')

        conn.commit()


if "__name__" == "__main__":
    db = dataBaseConfig()
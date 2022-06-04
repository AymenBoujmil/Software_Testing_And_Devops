import sqlite3

class dataBaseConfig:
    conn: sqlite3.Connection
    c: sqlite3.Cursor
    conn = sqlite3.connect('notes.db')
    conn2 = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("select sql from sqlite_master where type = 'table' and name = 'NOTES'")
    if not c.fetchall():
        c.execute(''' CREATE TABLE NOTES (
                                             id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                             title TEXT,
                                             note TEXT
                                             )''')

        conn.commit()
    c = conn2.cursor()
    c.execute("select sql from sqlite_master where type = 'table' and name = 'USER'")
    if not c.fetchall():
        c.execute(''' CREATE TABLE USER (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                                username TEXT,
                                                password TEXT
                                                )''')

        conn2.commit()


if "__name__" == "__main__":
    db = dataBaseConfig()
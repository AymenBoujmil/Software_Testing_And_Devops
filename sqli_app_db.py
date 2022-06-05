import sqlite3


def createDB(dbName):
    conn: sqlite3.Connection
    c: sqlite3.Cursor
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute("select sql from sqlite_master where type = 'table' and name = 'NOTES'")
    if not c.fetchall():
        c.execute(''' CREATE TABLE NOTES (
                                             id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                             title TEXT,
                                             note TEXT
                                             )''')
        c.execute("INSERT INTO NOTES  (title, note) VALUES ('note','note')")

        conn.commit()
    c.execute("select sql from sqlite_master where type = 'table' and name = 'USER'")
    if not c.fetchall():
        c.execute(''' CREATE TABLE USER (
                                                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                                username TEXT,
                                                password TEXT
                                                )''')
        c.execute("INSERT INTO USER (username, password) VALUES('admin','admin')")

        conn.commit()


if __name__ == "__main__":
    createDB("appDB.db")

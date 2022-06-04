import sqlite3


def signUp(username, password):
    # Connect to db
    db = sqlite3.connect('user.db')
    cursor = db.cursor()

    # Insert data into db
    cursor.execute("INSERT INTO USER(USERNAME,PASSWORD) VALUES(?, ?)", (username, password))
    db.commit()


    # Close db connection
    db.close()


def signIn(username, password):
    # Connect to db
    db = sqlite3.connect('user.db')
    cursor = db.cursor()

    # Get data from db
    user = cursor.execute('SELECT USERNAME FROM USER WHERE USERNAME="%s" AND PASSWORD="%s"' % (username, password))
    db.commit()
    if user.fetchone() is None:
        error = "Wrong Credentials! Please check again"
        return False, error

    # Close db connection
    db.close()

    return True, ""

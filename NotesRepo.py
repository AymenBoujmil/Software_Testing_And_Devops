import sqlite3


def fetchAll():
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get data from db
    cursor.execute('SELECT * FROM notes ORDER BY id DESC')
    notes = cursor.fetchall()

    # Close db connection
    db.close()
    return notes


def fetchone(_id):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get data from db
    cursor.execute('SELECT * FROM notes WHERE id=%s' % _id)
    note = cursor.fetchone()

    # Close db connection
    db.close()
    return note


def noteAdd(title, note):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Insert data into db
    cursor.execute('INSERT INTO notes(title, note) VALUES("%s", "%s")' % (title, note.replace('"', "'")))
    db.commit()

    # Close db connection
    db.close()


def noteUpdate(_id, title, note):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Update data in db
    cursor.execute('UPDATE notes SET title="%s", note="%s" WHERE id=%s' % (title, note.replace('"', "'"), _id))
    db.commit()

    # Close db connection
    db.close()


def noteDelete(_id):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Update data in db
    cursor.execute('DELETE FROM notes WHERE id=%s' % _id)
    db.commit()

    # Close db connection
    db.close()


def notesNumber(notes):
    number = 0
    for i in notes:
        number = number + 1
    return number

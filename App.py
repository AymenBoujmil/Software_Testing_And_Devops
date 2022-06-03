from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def root():
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get data from db
    cursor.execute('SELECT * FROM notes ORDER BY id DESC')
    notes = cursor.fetchall()
    number = notesNumber(notes)

    # Close db connection
    db.close()

    return render_template('notes.html', notes=notes, number = number)


@app.route('/note/<_id>')
def note(_id):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get data from db
    cursor.execute('SELECT * FROM notes WHERE id=%s' % _id)
    note = cursor.fetchone()

    # Close db connection
    db.close()
    return render_template('note.html', note=note)


def notesNumber(list):
    number = 0
    for i in list:
        number = number + 1
    return number


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/edit')
def edit():
    # Get request args
    title = request.args.get('title')
    note = request.args.get('note')
    _id = request.args.get('_id')

    return render_template('edit.html', title=title, note=note, _id=_id)


@app.route('/insert')
def insert():
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get request args
    title = request.args.get('title')
    note = request.args.get('note')

    # Insert data into db
    cursor.execute('INSERT INTO notes(title, note) VALUES("%s", "%s")' % (title, note.replace('"', "'")))
    db.commit()

    # Close db connection
    db.close()
    return redirect('/')


@app.route('/update/<_id>')
def update(_id):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Get request args
    title = request.args.get('title')
    note = request.args.get('note')

    # Update data in db
    cursor.execute('UPDATE notes SET title="%s", note="%s" WHERE id=%s' % (title, note.replace('"', "'"), _id))
    db.commit()

    # Close db connection
    db.close()
    return redirect('/')


@app.route('/delete/<_id>')
def delete(_id):
    # Connect to db
    db = sqlite3.connect('notes.db')
    cursor = db.cursor()

    # Update data in db
    cursor.execute('DELETE FROM notes WHERE id=%s' % _id)
    db.commit()

    # Close db connection
    db.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

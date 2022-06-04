from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import flash
import sqlite3
from NotesRepo import *
app = Flask(__name__)
app.secret_key = "flaskSecret"


@app.route('/')
def root():
    notes = fetchAll()
    number = notesNumber(notes)
    return render_template('notes.html', notes=notes, number=number)


@app.route('/note/<_id>')
def note(_id):

    note = fetchone(_id)
    return render_template('note.html', note=note)


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
    # Get request args
    title = request.args.get('title')
    note = request.args.get('note')
    noteAdd(title, note)
    flash("Note added successfully", "success")
    return redirect('/')


@app.route('/update/<_id>')
def update(_id):
    # Get request args
    title = request.args.get('title')
    note = request.args.get('note')
    noteUpdate(_id, title, note)
    flash("Note updated successfully","success")
    return redirect('/')


@app.route('/delete/<_id>')
def delete(_id):
    noteDelete(_id)
    flash('Note deleted successfully', "success")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

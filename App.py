from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import flash
from flask import session
from flask import url_for
import sqlite3
from NotesRepo import *
from functools import wraps
import AuthRepo




def create_app():
    @app.route('/register')
    def register():
        return render_template('register.html')


    @app.route('/signup')
    def signup():
        username = request.args.get('username')
        password = request.args.get('password')
        AuthRepo.signUp(username, str(password))
        flash("User Registered successfully", "success")
        return render_template('login.html')


    @app.route('/signin')
    def login():
        print(request.args)
        username = request.args.get('username')
        password = request.args.get('password')
        print(username,'usern')

        result, error = AuthRepo.signIn(username, str(password))
        print(result)
        if result:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully', 'success')
            return redirect(url_for("root"))
        else:
            return render_template('login.html', error=error)


    def is_logged_in(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                flash('Not Connected', 'danger')
                return render_template('login.html')

        return wrap


    @app.route('/logout')
    @is_logged_in
    def logout():
        session.clear()
        flash('Logged out successfully', 'success')
        return render_template('login.html')


    @app.route('/')
    @is_logged_in
    def root():
        notes = fetchAll()
        number = notesNumber(notes)
        return render_template('notes.html', notes=notes, number=number)


    @app.route('/note/<_id>')
    @is_logged_in
    def note(_id):
        note = fetchone(_id)
        return render_template('note.html', note=note)


    @app.route('/create')
    @is_logged_in
    def create():
        return render_template('create.html')


    @app.route('/edit')
    @is_logged_in
    def edit():
        # Get request args
        title = request.args.get('title')
        note = request.args.get('note')
        _id = request.args.get('_id')

        return render_template('edit.html', title=title, note=note, _id=_id)


    @app.route('/insert')
    @is_logged_in
    def insert():
        # Get request args
        title = request.args.get('title')
        note = request.args.get('note')
        noteAdd(title, note)
        flash("Note added successfully", "success")
        return redirect('/')


    @app.route('/update/<_id>')
    @is_logged_in
    def update(_id):
        # Get request args
        title = request.args.get('title')
        note = request.args.get('note')
        noteUpdate(_id, title, note)
        flash("Note updated successfully", "success")
        return redirect('/')


    @app.route('/delete/<_id>')
    @is_logged_in
    def delete(_id):
        noteDelete(_id)
        flash('Note deleted successfully', "success")
        return redirect('/')


if __name__ == '__main__':
    app = Flask(__name__)
    create_app()
    app.secret_key = 'flaskSecret'
    app.run(debug=True)
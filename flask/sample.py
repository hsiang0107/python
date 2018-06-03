__author__ = 'twlhgs'
import sqlite3
from flask import Flask, url_for, render_template, request, session, g, redirect, abort, flash
from contextlib import closing
import configuration as config
# configuration
# DATABASE = 'tmp/flaskr.db'
# DEBUG = True
# SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASSWORD = 'admin'

app = Flask(__name__)
# app.config.from_object(__name__)
app.config.from_object(config)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add/', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))






@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>/', methods=['GET'])
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>/', methods=['GET'])
def show_post(post_id):
    return 'post id %d' % post_id

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('hello', next='/'))
#     print(url_for('show_user_profile', username='sean'))

if __name__ == "__main__":
    app.run(host='127.0.0.1')
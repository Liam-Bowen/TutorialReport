from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'#\x9dlU#\xd2y\x04\xb90\x0b]\xc6\x0b\xef/'

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


from user import routes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

from flask import Flask, render_template, request, redirect, url_for
from message import Message
from user import User

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
  message = Message()

  if request.method == 'POST':
    message.save('frankSinatra', request.form['message-text'])

  return render_template('index.html', messages=message.all())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    user = User()
    user.save(request.form['email-address'], request.form['password'])
    return redirect( url_for('index') )

  return render_template('singup.html')
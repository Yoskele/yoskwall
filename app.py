from flask import Flask, render_template, request
from message import Message

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
  message = Message()

  if request.method == 'POST':
    message.save('frankSinatra', request.form['message-text'])

  # message.close()

  return render_template('index.html', messages=message.all())
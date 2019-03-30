from flask import Flask, flash, render_template, request, url_for, redirect
from message import Message

from user import Users

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
@app.route('/The_wall', methods=['POST', 'GET'])
def index():
  message = Message()

  if request.method == 'POST':
    message.save('admin', request.form['message-text'])
  # message.close()
  return render_template('index.html', messages=message.all())
#----------------------------------------
@app.route('/delete', methods=["POST"])
def delete():
    delete = Message()
    delete.delete()
    return redirect(url_for('index'))



# Works well after sign up it redirect u to index page.
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
	if request.method =='GET':
		return render_template('sign_up.html')
	username =  request.form.get('username', None)
	password = request.form.get('password', None)
	user = Users()
	user.create_user(username, password)
	return redirect(url_for('index'))

@app.route("/login/")
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        request.form.get('delete')
        user = Users()
        if user.check_user(username, password):
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route("/login/")
def logout():
    return redirect(url_for('login'))






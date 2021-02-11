from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')

def index():
	return render_template("index.html")

@app.route('/user/<name>')


def user(name):
		return "<h1>Hello {}!!</h1>".format(name)	
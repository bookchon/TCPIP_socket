from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

btnPin = 14
global push_btn
push_btn = False

app = Flask(__name__)

@app.route('/')
def home():
	return "Hello Flask"

@app.route('/test/')
def get():
	return render_template('get.html')

@app.route('/post')
def post():
	return render_template('default.html')

@app.route('push_switch')
def push_switch():
	global push_btn
	push_btn = not push_btn

if __name__ == "__main__":
	app.run(host='0.0.0.0', post="8080", debug=True)

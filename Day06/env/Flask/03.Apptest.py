from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Flask Server Test"

@app.route('/user/<username>')
def show_username(username):
	return "User: %s" % username

@app.route('/port/<int:port_id>')
def show_posrt(post_id):
	return "post %d" % post_id

if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8900')

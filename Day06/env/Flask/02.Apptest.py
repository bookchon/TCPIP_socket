from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello world"

@app.route('/name')
def namefunc():
	return "Yena"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="1111") # 호스트, 포트로 외부 접속 허락

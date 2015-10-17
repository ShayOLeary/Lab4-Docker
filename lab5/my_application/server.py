



from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)


@app.route('/')
def index(): pass


@app.route('hello')
def hello(): 
	return 'Hello'

@app.route('user/user')
def profile(user):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id









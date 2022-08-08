from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "my web app"
@app.route("/home")
def index():
    return "this is 2nd page"

if __name__ == '__main__':
    app.run()
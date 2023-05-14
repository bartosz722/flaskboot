from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/a")
def a():
    return "<p>Hello, World!xcffd</p>"

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/some")
def some():
    args = {
        'title': 'My Page',
        'username': 'John',
        'age': 20,
    }
    return render_template('some.html', **args)
from flask import Flask,  render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/some")
def some():
    args = {
        'title': 'My Page',
        'username': 'John',
        'age': 20,
    }
    return render_template('some.html', **args)
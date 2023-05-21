from flask import Flask, redirect,  render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/buy")
def buy():
    return render_template('buy.html')

@app.route("/sell")
def sell():
    return render_template('sell.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return redirect(url_for('main'))

@app.route("/some")
def some():
    args = {
        'title': 'My Page',
        'username': 'John',
        'age': 20,
    }
    return render_template('some.html', **args)
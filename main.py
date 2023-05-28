from flask import Flask, make_response, redirect,  render_template, request, url_for

from models.user import User

app = Flask(__name__)
user_cookie = 'shop_user_name'

@app.route("/")
def main():
    user = _get_user()
    return render_template('index.html', user=user)

@app.route("/buy")
def buy():
    user = _get_user()
    return render_template('buy.html', user=user)

@app.route("/sell")
def sell():
    user = _get_user()
    return render_template('sell.html', user=user)

@app.route("/profile")
def profile():
    user = _get_user()
    return render_template('profile.html', user=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('userName', '').strip()
        passwd = request.form.get('password', '').strip()
        if name and passwd:
            resp = redirect(url_for('main'))
            resp.set_cookie(user_cookie, name)
        else:
            resp = redirect(url_for('login', login_failed=1))
        return resp
    else:
        login_failed = bool(request.args.get('login_failed'))
        return render_template('login.html', login_failed=login_failed)

@app.route("/logout")
def logout():
    resp = redirect(url_for('main'))
    resp.delete_cookie(user_cookie)
    return resp

@app.route("/some")
def some():
    args = {
        'title': 'My Page',
        'username': 'John',
        'age': 20,
    }
    return render_template('some.html', **args)

def _get_user():
    uc = request.cookies.get(user_cookie)
    if uc:
        ret = User()
        ret.name = uc
        return ret

from flask import Flask, make_response, redirect,  render_template, request, url_for
from models import User
from utils import *
from ui_utils import *
import db

app = Flask(__name__)
user_cookie = 'shop_user_name'

@app.route("/")
def main():
    user = _get_user()
    return render_template('index.html', user=user)

@app.route("/buy")
def buy():
    page = request.args.get('page', default=1, type=int)
    user = _get_user()
    model = db.get_buy_model(page, 5)
    return render_template('buy.html', user=user, model=model)

@app.route("/buy/items/<item_id>")
def buy_item(item_id):
    user = _get_user()
    model = db.get_buy_item_model(item_id)
    bought = 'bought' in request.args
    question_asked = 'question_asked' in request.args
    return render_template('buy_item.html', user=user, model=model, bought=bought, question_asked=question_asked)

@app.route("/buy/item", methods=['POST'])
def buy_item_confirmed():
    item_id = request.form.get('itemId', '').strip()
    delivery = request.form.get('delivery')
    print('delivery: {}'.format(delivery))
    return redirect(url_for('buy_item', item_id=item_id, bought=1))

@app.route("/question/items/<item_id>", methods=['POST'])
def question_for_item(item_id):
    question = request.form.get('question')
    print('question: {}'.format(question))
    return redirect(url_for('buy_item', item_id=item_id, question_asked=1))

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

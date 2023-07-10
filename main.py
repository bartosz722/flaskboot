from flask import Flask, make_response, redirect,  render_template, request, url_for
from models import BuyItem, BuyItemModel, BuyModel, User
from utils import *
from ui_utils import *

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
    model = _get_buy_model(page, 5)
    return render_template('buy.html', user=user, model=model)

@app.route("/buy/items/<item_id>")
def buy_item(item_id):
    user = _get_user()
    model = _get_buy_item_model(item_id)
    return render_template('buy_item.html', user=user, model=model)

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

def _get_buy_model(page, page_size):
    total_items = 35
    ret = BuyModel()
    start, end = get_start_end_indexes(page, page_size, total_items)
    if start < 0:
        return ret    
    set_pagination(ret.pag, page, page_size, total_items)
    
    for i in range(start, end):
        item = BuyItem()
        item.id = str(i + 1)
        item.name = f'Rzecz {i + 1}'
        item.description = 'To jest niesamowita rzecz.'
        item.image = f'/static/item{i%4}.jpg'
        ret.items.append(item)

    return ret

def _get_buy_item_model(item_id):
    items = _get_buy_model(1, 1000)
    model = BuyItemModel()
    try:
        item = next(i for i in items.items if i.id == item_id)
        model.item = item
    except:
        pass
    return model

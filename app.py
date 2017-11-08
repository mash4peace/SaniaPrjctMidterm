from flask import Flask,render_template, request
import models, database

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return  render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/order', methods=['POST', 'GET'])
def order():
    cookieLists = database.showCookie("%")

    return render_template('order.html', cookieList = cookieLists)
"""
def order():




"""

@app.route("/save", methods=['POST'])
def sumbit():
    cookieName = request.form['cookieNames']
    models.addCookieToCart(cookieName)
    models.cartItems()
    cartCookieItems = models.cartItems()
    cookies = list(cartCookieItems)
    # Cookie Price
    cookiePrx = [cookie[1] for cookie in cookies]
    total = sum(cookiePrx)
    return render_template("total.html", catItems=cartCookieItems, total = total)


if __name__ == '__main__':
    app.run(debug=True)

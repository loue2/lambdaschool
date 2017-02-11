from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'July 14 1972'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello %s' % name

@app.route('/add/<int1>/<int2>')
def add(int1, int2):
    return str(int(int1)+int(int2))

@app.route('/multiply/<int1>/<int2>')
def multipy(int1, int2):
    return str(int(int1)*int(int2))

@app.route('/subract/<int1>/<int2>')
def subract(int1, int2):
    return str(int(int1)-int(int2))

@app.route('/favoritefoods')
def favoritefoods():
    foodlist = ['pizza', 'chicken tenders', 'hamburger and fries']

    return jsonify(foodlist)

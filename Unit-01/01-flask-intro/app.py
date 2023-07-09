from flask import Flask
#have a route for /welcome, which responds with the string "welcome"
app=Flask(__name__)
@app.route('/welcome')
def welcone():
  return "Welcome"
  #have a route for /welcome/home, which responds with the string "welcome home"
@app.route('/welcome/home')
def home():
  return "welcome home"
  #have a route for /welcome/back, which responds with the string "welcome back"
@app.route('/welcome/back')
def back():
  return "welcome back"
app.route('/sum')
def sum():
  sum = 5 + 5
  return sum

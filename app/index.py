from flask import Flask, session, redirect, url_for, request, render_template
app = Flask(__name__)
app.secret_key = "phiona is good"
@app.route('/')

def index():
   if 'username' in session:
      username = session['username']
      return '<p> Logged in as </p>' + username + '<br>' + \
         "<b><a href = '/logout'><p>click here to log out</p></a></b>"
   return "You are not logged in <br><a href = 'http://127.0.0.1:5000/login'></b>" + \
      "click here to log in</b></a> <p>Your are not registered<br><a href = '/registration'></b>" + \
      "click here to register</b></a></p>"
  
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)
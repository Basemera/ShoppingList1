from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def users():
   dict = {}
   return render_template('users.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def createlist():
    return render_template('createlist.html')

@app.route('/users',methods = ['POST', 'GET'])
def veiwitems():
    if request.method == 'POST':
        item = request.form
        
        return render_template("items.html", result = item)
        


if __name__ == '__main__':
   app.run(debug = True)
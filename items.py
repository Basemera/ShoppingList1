from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/items')
def viewitems():
    return render_template("items.html")
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)
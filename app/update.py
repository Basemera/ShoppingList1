from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/update' methods=['GET', 'POST'])
def deleteitem():
    if request.method == 'POST':
        del dict[key]
        return redirect(url_for('items'))
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True) 
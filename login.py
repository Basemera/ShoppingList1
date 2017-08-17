from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request['username']
        return redirect(url_for('index'))
    return render_template("login.html")
	
 



if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)
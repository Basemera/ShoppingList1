from flask import Flask, session, redirect, url_for, request, render_template
app = Flask(__name__)
app.secret_key = "phiona is good"
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)
from flask import Flask, session, redirect, url_for, request, render_template, app
from wtforms import Form, BooleanField, StringField, PasswordField, validators, flash

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

    @app.route('/registration', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User(form.username.data, form.email.data,
            form.password.data)
        
        flash('Thanks for registering')
        return redirect(url_for('login'))
        return render_template('registration.html', form=form)
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)  
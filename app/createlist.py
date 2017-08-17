from wtforms import Form, BooleanField, StringField, PasswordField, validators
app = Flask(__name__)

class RegistrationForm(Form):
    itemname = StringField('Itemname', [validators.Length(min=4)])
    Price = StringField('Price', [validators.Length(min=6, max=35)])
    Currency = StringField('Currency', [validators.Length(max=20)

@app.route('/createlist', methods = ['GET', 'POST'])
def createlist():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        item = Item(form.itemname.data, form.price, form.currency.data)
        flash('Thanks for adding an item')
        return redirect(url_for('items'))
    return render_template('createlist.html', form=form)
def veiwlist():
    if the request.method == 'GET':
       item = Item(form.itemname.data, form.price, form.currency.data)
       return redirect(url_for('items')) 
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug= True)
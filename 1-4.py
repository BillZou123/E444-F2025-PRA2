from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret'  

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()

    if form.validate_on_submit():
        user = form.name.data.strip()
        email = form.email.data.strip()

        # Check for UofT email
        if 'utoronto' in email.lower():
            return render_template('register.html', form=form, ok=True, user=user, email=email)
        else:
            flash('Please fill in a UofT email address (must contain "utoronto").')

    # GET or validation failure
    return render_template('register.html', form=form, ok=False)

if __name__ == '__main__':
    app.run(debug=True)
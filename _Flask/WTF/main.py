from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)

bootstrap = Bootstrap5(app)

app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', login_form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'static/files'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    return user
    # return User.get(user_id)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
        if new_user:
            flash("You've already signed up with that email. Please log in instead.")
            return redirect(url_for('login'))
        else:
            new_user = User(
                email=request.form['email'],
                password=generate_password_hash(request.form['password'], method='pbkdf2', salt_length=8),
                name=request.form.get('name')
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            # flash('Logged in successfully.')

            return render_template("secrets.html")
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()
        if user:
            if check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash("Password incorrect. Please try again.")
                return redirect(url_for('login'))
        else:
            flash("This email doesn't exist. Please try again.")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        path='cheat_sheet.pdf',
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)

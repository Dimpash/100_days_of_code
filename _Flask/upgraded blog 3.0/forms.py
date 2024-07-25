from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, URL, Length, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterUserForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=100)])
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Sign me up")


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(max=100)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Let me in")


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField(label="The body of the comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
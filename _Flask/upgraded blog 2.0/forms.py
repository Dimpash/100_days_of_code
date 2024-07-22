from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, HiddenField
from wtforms.validators import DataRequired, Length, URL
from flask_ckeditor import CKEditorField



class BlogPostAddForm(FlaskForm):
    title = StringField(label='The blog post title', validators=[DataRequired(), Length(max=250)])
    subtitle = StringField(label='The subtitle', validators=[DataRequired(), Length(max=250)])
    author = StringField(label="The author's name", validators=[DataRequired(), Length(max=250)])
    img_url = StringField(label="A URL for the background image", validators=[DataRequired(), URL()])
    body = CKEditorField(label="The body (the main content) of the post", validators=[DataRequired()])
    submit = SubmitField('Add Post')




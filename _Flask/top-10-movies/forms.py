from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, HiddenField
from wtforms.validators import DataRequired, Length, URL


class MovieEditForm(FlaskForm):
    # movie_id = HiddenField(validators=[DataRequired()])
    rating = DecimalField(label='Your Rating Ouf of 10 e.g. 7.3', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Done')


class MovieAddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Add Movie')

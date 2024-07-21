from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv
from datetime import datetime

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

coffee_choices = ['✘']
for i in range(1, 6):
    coffee_choices.append('☕️' * i)

wifi_choices = ['✘']
for i in range(1, 6):
    wifi_choices.append('💪' * i)

power_choices = ['✘']
for i in range(1, 6):
    power_choices.append('🔌' * i)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired(), Length(max=30)])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = DateTimeField(label='Opening time e.g. 8:00AM', format='%H:%M%p', validators=[DataRequired()])
    close = DateTimeField(label='Closing time e.g. 5:30PM', format='%H:%M%p', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=coffee_choices)
    wifi = SelectField(label='Wifi Strength Rating', choices=wifi_choices)
    power = SelectField(label='Power Socket Availability', choices=power_choices)
    # default = datetime.strftime('8:00AM', '%H:%M%p'),
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            # print(form.cafe.data)
            row = [
                form.cafe.data,
                form.location.data,
                form.open.data.strftime('%H:%M%p'),
                form.close.data.strftime('%H:%M%p'),
                form.coffee.data,
                form.wifi.data,
                form.power.data
            ]
            # print(row)
            csv_data.writerow(row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

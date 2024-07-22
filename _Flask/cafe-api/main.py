from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
from pprint import pprint

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    random_cafe = choice(all_cafes)
    cafe_json = jsonify(cafe=random_cafe.to_dict())
    # cafe_json = jsonify(
    #     cafe={
    #         # Omit the id from the response
    #         # "id": random_cafe.id,
    #         "name": random_cafe.name,
    #         "map_url": random_cafe.map_url,
    #         "img_url": random_cafe.img_url,
    #         "location": random_cafe.location,
    #
    #         # Put some properties in a sub-category
    #         "amenities": {
    #             "seats": random_cafe.seats,
    #             "has_toilet": random_cafe.has_toilet,
    #             "has_wifi": random_cafe.has_wifi,
    #             "has_sockets": random_cafe.has_sockets,
    #             "can_take_calls": random_cafe.can_take_calls,
    #             "coffee_price": random_cafe.coffee_price,
    #         }
    #     }
    # )
    return cafe_json


@app.route("/all_cafes", methods=['GET'])
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    all_cafes_list = [cafe.to_dict() for cafe in all_cafes]
    cafe_json = jsonify(cafes=all_cafes_list)
    return cafe_json


@app.route("/search", methods=['GET'])
def get_cafes_by_location():
    location = request.args.get('location', type=str)
    location_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location).order_by(Cafe.name)).scalars().all()
    if location_cafes:
        cafe_json = jsonify(cafes=[cafe.to_dict() for cafe in location_cafes])
    else:
        cafe_json = jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    return cafe_json


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    response = jsonify(response={"success": "Successfully added a new cafe."})
    return response


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_coffee_price(cafe_id):
    new_price = request.args.get('new_price', type=str)
    # cafe_to_update = db.get_or_404(Cafe, cafe_id)
    cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        response = jsonify(response={"success": "Successfully updated the price."})
    else:
        response = jsonify(error={"Not Found": "Sorry, a cafe with that id not found in database."})
    return response


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key', type=str)
    # if api_key == 'TopSecretAPIKey':
    #     try:
    #         cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    #         db.session.delete(cafe_to_delete)
    #         db.session.commit()
    #         return jsonify(response={"success": "Successfully deleted the cafe."}), 200
    #     except Exception as e:
    #         return jsonify(error=f"{e}"), 404
    # else:
    #     return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 401

    if api_key == 'TopSecretAPIKey':
        cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id not found in the database."}), 404
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 401


if __name__ == '__main__':
    app.run(debug=True)

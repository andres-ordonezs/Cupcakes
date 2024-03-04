"""Flask app for Cupcakes"""
import os
from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)



@app.get("/api/cupcakes")
def list_all_cupcakes():
    """Return JSON {'desserts': [{id, name, calories}, ...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def list_cupcake(cupcake_id):
    """Return JSON {'desserts': [{id, name, calories}, ...]}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def add_a_cupcake():
    """Return JSON {'desserts': [{id, name, calories}, ...]}"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"]


    new_cupcake = Cupcake(flavor= flavor,
                        size = size,
                        rating = rating,
                        image_url = image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(new_cupcake=serialized), 201)




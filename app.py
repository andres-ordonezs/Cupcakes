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
    """Return JSON {'dessert': [{id, name, calories}]}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post("/api/cupcakes")
def add_a_cupcake():
    """Return JSON {'dessert': [{id, name, calories}]}"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image_url = request.json["image_url"]

    cupcake = Cupcake(flavor=flavor,
                      size=size,
                      rating=rating,
                      image_url=image_url)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """ Updates cupcake and returns
    What data can you send?
    a JSON {cupcake: {id, flavor, size, rating, image_url}}   """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    data = request.json

    if 'flavor' in data:
        cupcake.flavor = data['flavor']
    # cupcake.flavor = data.get('flavor') or cupcake.flavor
    if 'size' in data:
        cupcake.size = data['size']
    if 'rating' in data:
        cupcake.rating = data['rating']
    if 'image_url' in data:

        #import default image url and use that in or statement
        cupcake.image_url = data['image_url'] or cupcake.image_url

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 200)


@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """ Deletes a cupcake and returns {deleted: [cupcake-id]} """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(deleted = cupcake_id))

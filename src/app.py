"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Starship #edutar para agregar nuevos modelos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

"""
aqui comenzamos nuestro código
"""


# Endpoint users
@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/characters/<int:characters_id>', methods=['PUT', 'GET'])
def get_single_person(characters):
    """
    Single person
    """
    body = request.get_json()  # Input: {'username': 'new_username'}
    if request.method == 'PUT':
        user1 = Characters.query.get(characters)
        user1.username = body.username
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = Characters.query.get(characters_id)
        return jsonify(user1.serialize()), 200
    return "Invalid Method", 404

@app.route('/planets/<int:planets_id>', methods=['PUT', 'GET'])
def get_single_planets(planets):
    """
    Single planets
    """
    body = request.get_json()  # Input: {'username': 'new_username'}
    if request.method == 'PUT':
        user1 = Planets.query.get(planets)
        user1.username = body.username
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = Planets.query.get(planets_id)
        return jsonify(user1.serialize()), 200
    return "Invalid Method", 404

@app.route('/starship/<int:starship_id>', methods=['PUT', 'GET'])
def get_single_starship(starship):
    """
    Single starship
    """
    body = request.get_json()  # Input: {'username': 'new_username'}
    if request.method == 'PUT':
        user1 = Starship.query.get(starship)
        user1.username = body.username
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = Starship.query.get(starship_id)
        return jsonify(user1.serialize()), 200
    return "Invalid Method", 404

"""
aqui termina nuestro código
"""

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

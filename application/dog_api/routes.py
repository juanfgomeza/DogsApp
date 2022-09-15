from urllib import response
from . import dog_api_blueprint
from .. import db
from ..models import Dog
from flask import jsonify, request

@dog_api_blueprint.route('/api/dogs', methods=['GET'])
def dogs():
    dogs = []
    for row in Dog.query.all():
        dogs.append(row.to_json())

    response = jsonify({'results' : dogs})
    return response

@dog_api_blueprint.route('/api/dog/add', methods=['POST'])
def add_dog():
    name = request.form['name']
    color = request.form['color']
    size = request.form['size']
    age = request.form['age']
    gender = request.form['gender']
    breed = request.form['breed']

    dog = Dog()
    dog.name = name
    dog.color = color
    dog.size = size
    dog.age = age
    dog.gender = gender
    dog.breed = breed

    db.session.add(dog)
    db.session.commit()

    response = jsonify({'message': 'Dog added', 'dog': dog.to_json()})
    return response
    

    

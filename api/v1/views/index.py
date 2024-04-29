#!/usr/bin/python3
'''create Flask app; app.view'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats')
def get_stats():
    '''JSON Responses'''
    stats = {
        'states': storage.count('State'),
        'users': storage.count('User'),
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
    }
    return jsonify(stats)

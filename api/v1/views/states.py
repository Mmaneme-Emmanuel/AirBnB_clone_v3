from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def posting():
    '''Creates a State'''
    response = request.get_json()
    if response is None:
        abort(400, {'error': 'Not a JSON'})
    if "name" not in response:
        abort(400, {'error': 'Missing name'})
    stateObject = State(name=response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), 201


@app_views.route('/states/<string:stateid>',
                 methods=['GET'], strict_slashes=False)
def toGetid(stateid):
    '''Updates a State object id'''
    stateObject = storage.get(State, stateid)
    if stateObject is None:
        abort(404)
    return jsonify(stateObject.to_dict()), 200


@app_views.route('/states/<state_id>',
                 methods=['PUT'], strict_slashes=False)
def putinV(state_id):
    '''vladimir'''
    response = request.get_json()
    if response is None:
        abort(400, {'error': 'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key in response.keys():
        if key not in ignoreKeys:
            setattr(stateObject, key, response[key])
    storage.save()
    return jsonify(stateObject.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting(state_id):
    ''' to delete an onbject'''
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), 200

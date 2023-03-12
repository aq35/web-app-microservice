# helper.pyファイル

from flask import jsonify


def app_json_response(data: dict):
    responseData = {'message': 'User created successfully'}
    response = jsonify({**data, **responseData})
    return response, 200

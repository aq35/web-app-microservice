# helper.pyファイル

from flask import jsonify


def app_json_response(data):
    print(data)
    response = jsonify(
        {'message': 'User created successfully'}
        )
    return response, 201

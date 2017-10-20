from flask_api import FlaskAPI
from flask import request, jsonify, abort
# local import
from instance.config import app_config


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    @app.route('/hello/<string:name>', methods=['GET'])
    def appEndPoint(name, **kwargs):
        if request.method == "GET":
            if name:
                response = jsonify({
                    'message': "Hello {}".format(name)
                    })
                response.status_code = 200
                return response
        else:
            # POST Justo for fun

            if name:
                response = jsonify({
                    'string': "hello {}".format(name)
                    })
                response.status_code = 201
                return response

    return app

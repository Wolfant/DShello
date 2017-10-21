import os
from flask_api import FlaskAPI
from flask import request, jsonify, abort
# local import
from instance.config import app_config
from rest import create_app

# config_name = "development"
config_name = os.getenv('APP_SETTINGS', 'production')
app = create_app(config_name)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

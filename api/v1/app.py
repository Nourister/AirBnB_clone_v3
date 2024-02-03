#!/usr/bin/python3
""" A flask application"""

from flask import Flask, jsonify, make_response
from werkzeug.exceptions import NotFound
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

@app.errorhandler(NotFound)
def handle_not_found(error):
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)

from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask import Blueprint, render_template, jsonify
import os

api = Blueprint('api', __name__)


spec = APISpec(
    title="Redemptioner API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


@api.route('/')
def index():
    return render_template('api/index.html')


@api.route("/version")
def get_info():
    """
    Get info on our server
    ---
    get:
        description: Get the version information for our service
        responses:
            200:
                content:
                    application/json:
                        schema:
                            type: object
                            properties:
                                version:
                                    type: string
                                    description: Version number of our service
    """
    return jsonify({
        "version": os.environ.get("VERSION"),
    })

    # Need to register the path


@api.route("/spec")
def get_apispec():
    return jsonify(spec.to_dict())
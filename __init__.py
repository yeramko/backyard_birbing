from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

# from backyard_birbing.search import return_relevant_recipes

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#################################################
# Flask Setup
#################################################
# app = Flask(__name__)
# CORS(app)

#################################################
# Flask Routes
#################################################

import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    @app.route("/")
    def welcome():
        return (
            "Welcome to the birbland!<br/>")

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/api/search/<query>")
    def search_query(query=None):

        try:
            # results = return_relevant_recipes(query)
            # df_to_dict = results.to_dict('r')
            # data = json.dumps(df_to_dict, ensure_ascii=False, indent=4)

            return (
                # data
            )

        except Exception as e:
            return (
                f"{e}"
        )

    return app

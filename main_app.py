#!/usr/bin/python3
"""Main application for integrating all APIs"""

import os
import sys
from flask import Flask
from flask_restx import Api

# Adding the path to the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'api')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data')))

# Importing individual API modules
from api.api_user import ns as user_namespace
from api.api_country import ns as country_namespace
from api.api_city import ns as city_namespace
from api.api_amenity import ns as amenity_namespace
from api.api_place import ns as place_namespace
from api.api_review import ns as review_namespace

app = Flask(__name__)
api = Api(app)

# Adding namespaces to the API
api.add_namespace(user_namespace, path='/users')
api.add_namespace(country_namespace, path='/countries')
api.add_namespace(city_namespace, path='/cities')
api.add_namespace(amenity_namespace, path='/amenities')
api.add_namespace(place_namespace, path='/places')
api.add_namespace(review_namespace, path='/reviews')

if __name__ == '__main__':
    app.run(debug=True)

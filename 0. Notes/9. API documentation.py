# create documentation for your API using swagger_ui.
# pip3 install flask_swagger_ui

#Put the following code in app.py:
from flask_swagger_ui import get_swaggerui_blueprint
....
SWAGGER_URL="/api/docs"  # (1) swagger endpoint e.g. HTTP://localhost:5002/api/docs
API_URL="/static/masterblog.json" # (2) ensure you create this dir and file

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Masterblog API' # (3) You can change this if you like
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# create a new directory 'static' in backend, within it create a new file called masterblog.json in backend/static/masterblog.json:
# add the swagger definition to it:
{
  "swagger": "2.0",
  "info": {
    "title": "Masterblog API",
    "version": "1.0.0"
  },
  "servers": [{ "url": "http://localhost:5001" }],
  "tags": [{ "name": "Post", "description": "Post API - CRUD" }],
}

# adding our API paths to the definition path.
# Add the following code below the “tags” key:

{
    "paths": {
        "/api/posts": {
            "get": {
        "summary": "Returns all posts",
        "produces": ["application/json"],
        "tags": ["Post"],
        "responses": {
          "200": {
            "description": "Successful operation"
          }
        }
      },
        }
    }
}

#  to see the output of everything we’ve done until now.
# Ensure your app is running, then navigate to http://127.0.0.1:5002/api/docs
from flask import Flask
from flask_graphql import GraphQLView
from .schemas import schema


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Index page"

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
        'graphql', schema=schema, graphiql=True
    ))

    @app.errorhandler(404)
    def page_not_found(error):
        return "404 Page not found"
    return app
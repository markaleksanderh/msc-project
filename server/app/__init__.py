from flask import Flask
# from flask_graphql import GraphQLView

def create_app():
    app = Flask(__name__)


    @app.errorhandler(404)
    def page_not_found(error):
        return "404 Page not found"
    return app
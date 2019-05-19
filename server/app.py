from flask import Flask, jsonify
from flask_graphql import GraphQLView
from .schemas import *

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=models, graphiql=True))


@app.route('/')
def index():
    return jsonify({'message': "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


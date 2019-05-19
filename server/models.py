from graphql import GraphQLError
from py2neo import Graph
from py2neo.ogm import GraphObject, Property, RelatedTo


# Set up config file

graph = Graph(
    host="localhost",
    port=7687,
    user="neo4j"
    password="letmein",
)
from graphql import GraphQLError
from py2neo import Graph, Node
from py2neo.ogm import GraphObject, Property, RelatedTo


# Set up config file
graph = Graph(
    host="localhost",
    port=7687,
    user="neo4j",
    password="letmein",
)

class Project(GraphObject):
    __primarykey__ = "name"
    name = Property()

    # def __init__(self, **kwargs):
    #     for key, value in kwargs.items():
    #         if hasattr(self, key):
    #             setattr(self, key, value)
    
    # @property
    # def all(self):
    #     return self.select(graph)


    # def save(self):
    #     graph.push(self)


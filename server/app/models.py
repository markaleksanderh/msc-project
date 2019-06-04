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

class BaseModel(GraphObject):
    def __init__(self, **kwargs):
        for key, value, in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self):
        return self.select(graph)
    
    def save(self):
        graph.push(self)

class Project(BaseModel):
    __primarykey__ = 'name'
    name = Property()

    def fetch(self):
        return self.select(graph, self.name).first()


# class Project(GraphObject):
#     __primarykey__ = "name"
#     name = Property()

    # def __init__(self, **kwargs):
    #     for key, value in kwargs.items():
    #         if hasattr(self, key):
    #             setattr(self, key, value)
    
    # @property
    # def all(self):
    #     return self.select(graph)


    # def save(self):
    #     graph.push(self)


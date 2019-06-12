from graphql import GraphQLError
from py2neo import Graph, Node, Relationship
from py2neo.ogm import GraphObject, Property, RelatedTo


# Set up config file
graph = Graph(
    bolt=True,
    host='172.18.0.2',
    bolt_port=7687,
)

# graph = Graph("http://localhost:7474/db/data/")


test_person = Node("Person", name="Test Person")
graph.create(test_person)


# print(graph)

class Project(GraphObject):
    def __init__(self, name):
        self.name = name
    __primarykey__ = "name"
    name = Property()

    def save(self):
        graph.push(self)

# class BaseModel(GraphObject):
#     def __init__(self, **kwargs):
#         for key, value, in kwargs.items():
#             if hasattr(self, key):
#                 setattr(self, key, value)

#     @property
#     def all(self):
#         return self.select(graph)
    
#     def save(self):
#         graph.push(self)

# class Project(BaseModel):
#     __primarykey__ = 'name'
#     name = Property()

#     def fetch(self):
#         return self.select(graph, self.name).first()


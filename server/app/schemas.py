import graphene

from .models import Project


# Project schema 
class ProjectSchema(graphene.ObjectType):
    name = graphene.String()

# Query
class Query(graphene.ObjectType):
    projects = graphene.List(lambda: ProjectSchema)

# Mutations
# class Mutations(graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query, auto_camelcase=False)
import graphene

from .models import Project


# Project schema 
class ProjectSchema(graphene.ObjectType):
    name = graphene.String()
    description = graphene.String()
    
class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    success = graphene.Boolean()
    project = graphene.Field(lambda: ProjectSchema)

    def mutate(self, info,**kwargs):
        project = Project(**kwargs)
        project.save()
        return CreateProject(project=project, success=True)

# Query
class Query(graphene.ObjectType):
    projects = graphene.List(lambda: ProjectSchema)


# Mutations
class Mutations(graphene.ObjectType):
    create_project = CreateProject.Field()


schema = graphene.Schema(query=Query, auto_camelcase=False)
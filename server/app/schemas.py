import graphene

from .models import Project

# Project schema 
class ProjectSchema(graphene.ObjectType):
    name = graphene.String()

    
# class CreateProject(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True)

#     success = graphene.Boolean()
#     project = graphene.Field(lambda: ProjectSchema)

#     def mutate(self, info,**kwargs):
#         project = Project(**kwargs)
#         project.save()
#         return CreateProject(project=project, success=True)

# Query
# class Query(graphene.ObjectType):

#     projects = graphene.List(lambda: ProjectSchema, name=graphene.String())

class Query(graphene.ObjectType):
    # project = graphene.Field(lambda: ProjectSchema, name=graphene.String())
   
    # def resolve_project(self, info, name):
    #     project = Project(name=name).fetch()
    #     return ProjectSchema(**project.as_dict())
    projects = graphene.List(lambda: ProjectSchema)

    def resolve_projects(self, info):
        [ProjectSchema(**project.as_dict()) for project in Project().all]

# Mutations
# class Mutations(graphene.ObjectType):
#     create_project = CreateProject.Field()


# schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)
schema = graphene.Schema(query=Query, auto_camelcase=False)
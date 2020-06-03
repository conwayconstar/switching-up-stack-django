import graphene

import users.schema


class Query(users.schema.Query, graphene.ObjectType):
    """
    Projects main Query class, this will inherit multiple queries.
    """
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):
    """
    Projects main Mutation class, this will inherit multiple mutations.
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

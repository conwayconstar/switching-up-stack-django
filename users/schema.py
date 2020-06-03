import graphql_jwt
from graphene import Mutation, ObjectType, List, Field, Int, String, ID
from graphene_django.types import DjangoObjectType
from .models import CustomUser as User


class UserType(DjangoObjectType):
    """
    User model's fields are automatically mapped onto the UserType.
    """

    class Meta:
        """
        User model is configured here.
        Set fields you wish to be outputted.
        """
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'last_login',
            'email',
            'occupation',
            'company',
            'profile_title',
            'profile_description',
            'date_joined',
        )


class Query(object):
    """
    User queries.
    """
    users = List(UserType)
    user = Field(UserType, id=Int())
    me = Field(UserType)

    @staticmethod
    def resolve_users(self, info, **kwargs):
        """
        Resolves all users.
        """
        return User.objects.all()

    @staticmethod
    def resolve_user(self, info, **kwargs):
        """
        Resolves a single user by ID.
        """
        return User.objects.get_by_id(**kwargs)

    @staticmethod
    def resolve_me(self, info):
        """
        Resolves the logged in user
        """
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You are not logged in')

        return user


class CreateUser(Mutation):
    """
    Create a user mutation.
    Attributes for the class define the mutation response.
    """
    id = ID()
    email = String()
    first_name = String()
    last_name = String()

    class Arguments:
        """
        Input arguments to create a user.
        """
        email = String(required=True)
        password = String(required=True)
        first_name = String(required=True)
        last_name = String()

    @staticmethod
    def mutate(_, info, email, password, first_name, last_name):
        """
        Use the create_user method and return the
        attributes we specified.
        """
        user = User.objects.create_user(email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name)

        return CreateUser(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name)


class Mutation(ObjectType):
    """
    Mutations for Users.
    """
    create_user = CreateUser.Field()
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

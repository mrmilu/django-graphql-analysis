# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene

# App imports
from django_graphql.schema.mutations import Mutation
from django_graphql.schema.queries import Query
from django_graphql.schema.types import TYPES

schema = graphene.Schema(
    query=Query,
    types=TYPES,
    mutation=Mutation
)

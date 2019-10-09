# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene

# App imports
from shop_demo.django_graphql.schema.mutations import Mutation
from shop_demo.django_graphql.schema.queries import Query
from shop_demo.django_graphql.schema.types import TYPES

schema = graphene.Schema(
    query=Query,
    types=TYPES,
    mutation=Mutation
)

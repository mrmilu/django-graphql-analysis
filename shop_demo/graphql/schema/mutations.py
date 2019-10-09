# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene

# App imports
from products.api.django_graphene.mutations import ProductMutation


class Mutation(
    ProductMutation,
    graphene.ObjectType):
    pass

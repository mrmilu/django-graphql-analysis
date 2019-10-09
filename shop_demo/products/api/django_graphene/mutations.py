# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

# App imports
from shop_demo.products.api.django_graphene.serializers import ProductSerializer


class ProductCreate(SerializerMutation):
    class Meta:
        serializer_class = ProductSerializer
        model_operations = ['create']
        permission_classes = []


class ProductMutation(graphene.ObjectType):
    product_create = ProductCreate.Field()

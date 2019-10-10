from shop_demo.config.settings.base import *

INSTALLED_APPS += ['graphene_django']

# Graphene
GRAPHENE = {
    'SCHEMA': 'shop_demo.django_graphql.schema.schema'
}

DJANGO_GRAPHQL = True
GRAPHQL_ENDPOINT = 'django-graphql'

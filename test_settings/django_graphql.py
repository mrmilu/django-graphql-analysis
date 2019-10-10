from shop_demo.config.settings.django_graphql import *

DEBUG = True

# Graphene
GRAPHENE = {
    'SCHEMA': 'shop_demo.django_graphql.schema.schema'
}

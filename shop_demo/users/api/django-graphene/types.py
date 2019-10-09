# # -*- coding: utf-8 -*-
# # Python imports
#
# # Django imports
#
# # 3rd Party imports
# import graphene
# from graphene_django import DjangoObjectType
#
# # App imports
# from shop_demo.users.models import User
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         name = 'user'
#         model = User
#         interfaces = (graphene.relay.Node,)
#         connection_class = CountableConnectionBase
#         only_fields = [
#             'id',
#             'created',
#             'modified',
#             'name',
#             'description',
#         ]
#         filter_fields = [
#             'id',
#             'name'
#         ]

# # -*- coding: utf-8 -*-
# # Python imports
#
# # Django imports
#
# # 3rd Party imports
#
# # App imports
#
#
# class UserSave(SerializerMutation):
#     class Meta:
#         serializer_class = UserSaveSerializer
#         model_operations = ['create']
#         permission_classes = []
#
#
# class UserMutation(graphene.ObjectType):
#     user_save = UserSave.Field()

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
# class UserSaveSerializer(serializers.ModelSerializer):
#     user_id = IdField(write_only=True, required=False)
#     responsible_id = IdField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'user_id',
#             'name',
#         )
#         read_only_fields = (
#             'id',
#         )

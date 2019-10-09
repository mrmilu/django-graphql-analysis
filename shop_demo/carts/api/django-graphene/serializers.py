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
# class CartSaveSerializer(serializers.ModelSerializer):
#     cart_id = IdField(write_only=True, required=False)
#     responsible_id = IdField(write_only=True)
#
#     class Meta:
#         model = Cart
#         fields = (
#             'id',
#             'cart_id',
#             'name',
#         )
#         read_only_fields = (
#             'id',
#         )

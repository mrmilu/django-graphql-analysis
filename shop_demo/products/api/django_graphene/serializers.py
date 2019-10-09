# -*- coding: utf-8 -*-
# Python imports

# Django imports

# 3rd Party imports
from rest_framework import serializers

# App imports
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # product_id = IdField(write_only=True, required=False)
    # responsible_id = IdField(write_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            # 'product_id',
            'name',
        )
        read_only_fields = (
            'id',
        )

# -*- coding: utf-8 -*-
# Python imports

# Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third party imports
from djmoney.models.fields import MoneyField


# App imports


class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    total = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.pk)


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()

    class Meta:
        verbose_name = _('Product Cart')
        verbose_name_plural = _('Products Cart')

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.pk)

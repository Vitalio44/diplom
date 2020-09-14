import datetime

from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name='Товар', related_name='orders')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Order {self.user.username} - {datetime.datetime.strptime(self.created_at, '%Y-%m-%d')}"

from django.urls import path

from products.views import (product_page, product_review, category_page,
                            cart_page)

urlpatterns = [
    path('cart/', cart_page, name='cart_page'),
    path('category/<int:pk>/', category_page, name='category_page'),
    path('<int:pk>/', product_page, name='product_page'),
    path('<int:pk>/feedback/', product_review),
]

from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    # list_display = ['company_name', 'id', 'registration_data', 'edit_date', 'verify']
    # list_display_links = ['company_name']

    # search_fields = ['ogrn']

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)

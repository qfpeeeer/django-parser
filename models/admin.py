from django.contrib import admin
from .models import Product, History


class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'link', 'shop')
    list_display_links = ('id', 'category', 'title', 'link', 'shop')
    search_fields = ('id', 'category', 'title', 'link', 'shop')
    list_filter = ('id', 'category', 'title', 'link', 'shop')


class HistoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'price', 'date', 'product_id')
    list_display_links = ('id', 'price', 'date', 'product_id')
    search_fields = ('id', 'price', 'date', 'product_id')
    list_filter = ('id', 'price', 'date', 'product_id')


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
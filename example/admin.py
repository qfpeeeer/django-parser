from django.contrib import admin
from .models import Phone, Laptop, Monitor, Keyboard, PhoneHistory, LaptopHistory, MonitorHistory, KeyboardHistory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'shop')
    list_display_links = ('id', 'title', 'link', 'shop')
    search_fields = ('id', 'title', 'link', 'shop')
    list_filter = ('id', 'title', 'link', 'shop')


class ProductAdmin (admin.ModelAdmin):
    list_display = ('id', 'price', 'date', 'category_id')
    list_display_links = ('id', 'price', 'date', 'category_id')
    search_fields = ('id', 'price', 'date', 'category_id')
    list_filter = ('id', 'price', 'date', 'category_id')


admin.site.register(Phone, CategoryAdmin)
admin.site.register(Laptop, CategoryAdmin)
admin.site.register(Monitor, CategoryAdmin)
admin.site.register(Keyboard, CategoryAdmin)

admin.site.register(PhoneHistory, ProductAdmin)
admin.site.register(LaptopHistory, ProductAdmin)
admin.site.register(MonitorHistory, ProductAdmin)
admin.site.register(KeyboardHistory, ProductAdmin)

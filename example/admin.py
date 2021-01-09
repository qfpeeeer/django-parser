from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'price', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_filter = ('price',)


admin.site.register(Data, DataAdmin)

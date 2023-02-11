from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    """Настройки отображения модели Post в интерфейсе админа"""
    list_display = (
        'pk',
        'name',
        'description',
        'price',
    )
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)

from django.contrib import admin

from menu.models import Menu


# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'parent',)
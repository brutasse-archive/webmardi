from django.contrib import admin

from .models import Cheese, Taste

class CheeseAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class TasteAdmin(admin.ModelAdmin):
    list_display = ('cheese', 'user', 'like')

admin.site.register(Cheese, CheeseAdmin)
admin.site.register(Taste, TasteAdmin)

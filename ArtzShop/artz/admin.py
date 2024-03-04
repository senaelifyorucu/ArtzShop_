from django.contrib import admin
from .models import Artz


class ArtzAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')



admin.site.register(Artz, ArtzAdmin)

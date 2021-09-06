from django.contrib import admin

from forecasts.groups.models import CustomGroup

@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    model = CustomGroup
    list_display = ('name', 'guid')

from django.contrib import admin
from .models import RegionModel
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

@admin.register(RegionModel)
class RegionAdmin(DraggableMPTTAdmin):

    mptt_indent_field = 'name'
    list_display = ('tree_actions', 'indented_title', 'create_date', 'uuid')

    list_filter = ('create_date',)
    search_fields = ('name',)
    list_per_page = 25





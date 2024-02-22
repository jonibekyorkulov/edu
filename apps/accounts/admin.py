from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', )
    list_display = ['first_name', 'last_name', 'role', 'passport']
    ordering = ['-create_date']


admin.site.register(User, UserAdmin)
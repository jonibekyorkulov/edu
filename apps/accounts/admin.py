from django.contrib import admin
from .models import User, UserFile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'password')
    list_display = ['first_name', 'last_name', 'role', 'passport']
    ordering = ['-create_date']


admin.site.register(User, UserAdmin)


class UserFileAdmin(admin.ModelAdmin):
    ordering = ['-create_date']
    
admin.site.register(UserFile)
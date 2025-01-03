from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['created_at','user_name', 'user_password', 'age', 'email']

admin.site.register(User, UserAdmin)
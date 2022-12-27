from django.contrib import admin

from users.models import User
from udc_rec_sys.admin import UserStashAdminInline

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (UserStashAdminInline, )

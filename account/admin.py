from django.contrib import admin

# Register your models here.
from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','is_administrator']
    list_filter = ('is_administrator','type',)
    list_editable = ('is_administrator',)
    search_fields = ('email',)

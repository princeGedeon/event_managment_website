from django.contrib import admin

# Register your models here.
from eventapp.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','proprietaire','end_register_date','disable']
    list_filter = ('disable','is_free',)
    list_editable = ('disable',)
    search_fields = ('title',)

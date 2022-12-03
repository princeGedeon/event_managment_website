from django.contrib import admin

# Register your models here.
from eventapp.models import Event,Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title','proprietaire','end_register_date','disable']
    list_filter = ('disable','is_free',)
    list_editable = ('disable',)
    search_fields = ('title',)

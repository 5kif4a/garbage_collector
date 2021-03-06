from django.contrib import admin
from .models import Dump, Event

# Register your models here.
admin.site.site_header = 'Garbage collector'


def get_model_fields(model):
    return [field.name for field in model._meta.get_fields()][1:]


@admin.register(Dump)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Dump)


@admin.register(Event)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Event)

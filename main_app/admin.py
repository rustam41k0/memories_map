from django.contrib import admin

from main_app.models import Memory


@admin.register(Memory)
class MemoryAdmin(admin.OSMGeoAdmin):
    list_display = ("title", "location")

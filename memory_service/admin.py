# Register your models here.
# memory_service/admin.py
from django.contrib import admin

from .models import VectorEntry, VectorMetadata


@admin.register(VectorEntry)
class VectorEntryAdmin(admin.ModelAdmin):
    list_display = ("vector_id", "source_type", "source_id", "created_at")
    search_fields = ("source_type", "source_id")
    readonly_fields = ("vector_id", "created_at")


@admin.register(VectorMetadata)
class VectorMetadataAdmin(admin.ModelAdmin):
    list_display = ("id", "vector", "key", "value")
    search_fields = ("key", "value")

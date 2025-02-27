from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ["file_name", "file_path", "version", "created_by", "created_at"]
    search_fields = ["file_name", "file_path__url_path", "created_by__email", "created_at"]


class UrlManagementAdmin(admin.ModelAdmin):
    search_fields = ["url_path", "created_by__email"]

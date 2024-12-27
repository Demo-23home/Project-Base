from django.contrib import admin
from .models import ContentView
from django.contrib.contenttypes.admin import GenericTabularInline


@admin.register(ContentView)
class ContentViewAdmin(admin.ModelAdmin):
    list_display = ["content_object", "user", "viewer_ip", "created_at"]
    
    
class ContentViewInline(GenericTabularInline):
    model = ContentView
    readonly_fields = ["user", "viewer_ip", "created_at"]
    extra = 0
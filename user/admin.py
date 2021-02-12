from django.contrib import admin

from .models import UMessage

# Register your models here.

@admin.register(UMessage)

class UMessageAdmin(admin.ModelAdmin):

    list_display = ["Name","Email","created_date","Message"]
    list_display_links = ["Name","created_date"]
    search_fields = ["Name"]
    list_filter = ["created_date"]
    class Meta:
        model = UMessage



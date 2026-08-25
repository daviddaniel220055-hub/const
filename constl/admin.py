from django.contrib import admin
from .models import ContactEnquiry


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organisation",
        "email",
        "phone",
        "service",
        "is_read",
        "created_at",
    )

    list_filter = (
        "service",
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "organisation",
        "email",
        "phone",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )
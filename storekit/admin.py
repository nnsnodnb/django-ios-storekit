from django.contrib import admin

from .models import InApp, Receipt, Response


class InAppAdmin(admin.ModelAdmin):
    list_display = (
        "quantity",
        "product_id",
        "transaction_id",
        "original_transaction_id",
        "purchase_date",
        "original_purchase_date",
        "is_trial_period",
    )
    list_display_links = (
        "quantity",
        "product_id",
        "transaction_id",
        "original_transaction_id",
        "purchase_date",
        "original_purchase_date",
    )


admin.site.register(InApp, InAppAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "receipt_type",
        "adam_id",
        "app_item_id",
        "bundle_id",
        "application_version",
        "download_id",
        "version_external_identifier",
        "receipt_creation_date",
        "request_date",
        "original_purchase_date",
        "in_app",
    )
    list_display_links = (
        "receipt_type",
        "adam_id",
        "app_item_id",
        "bundle_id",
        "application_version",
        "download_id",
        "version_external_identifier",
        "receipt_creation_date",
        "request_date",
        "original_purchase_date",
        "in_app",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("in_app")


admin.site.register(Receipt, ReceiptAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("status", "environment", "receipt")
    list_display_links = ("status", "environment", "receipt")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("receipt")


admin.site.register(Response, ResponseAdmin)

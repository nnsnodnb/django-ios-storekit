from django.contrib import admin
from .models import InApp, Receipt, Response, Purchase


class InAppAdmin(admin.ModelAdmin):
    list_display = (
        'quantity', 'product_id', 'transaction_id',
        'original_transaction_id', 'purchase_date', 'original_purchase_date', 'is_trial_period'
    )
    list_display_links = (
        'quantity', 'product_id', 'transaction_id',
        'original_transaction_id', 'purchase_date', 'original_purchase_date'
    )


admin.site.register(InApp, InAppAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        'receipt_type', 'adam_id', 'app_item_id', 'bundle_id', 'application_version', 'download_id',
        'version_external_identifier', 'receipt_creation_date', 'request_date', 'original_purchase_date', 'in_app'
    )
    list_display_links = (
        'receipt_type', 'adam_id', 'app_item_id', 'bundle_id', 'application_version', 'download_id',
        'version_external_identifier', 'receipt_creation_date', 'request_date', 'original_purchase_date', 'in_app'
    )


admin.site.register(Receipt, ReceiptAdmin)


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('status', 'environment', 'receipt')
    list_display_links = ('status', 'environment', 'receipt')


admin.site.register(Response, ResponseAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'product_id', 'quantity', 'purchased_at', 'response')
    list_display_links = ('transaction_id', 'product_id', 'quantity', 'purchased_at', 'response')


admin.site.register(Purchase, PurchaseAdmin)

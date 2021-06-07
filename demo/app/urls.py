from django.urls import path
from .views import receive_normal_receipt, receive_subscribe_receipt


app_name = "app"

urlpatterns = [
    path("normal", receive_normal_receipt, name="normal"),
    path("subscribe", receive_subscribe_receipt, name="subscribe"),
]

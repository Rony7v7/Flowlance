from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.payment, name="payment"),
    path("paypal/", include("paypal.standard.ipn.urls")),
    path("payment_success/", views.payment_success, name="payment_success"),
    path("payment_failed/", views.payment_failed, name="payment_failed"),
    path("payment_process/", views.payment_process, name="payment_process"),
]

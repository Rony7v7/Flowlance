from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("paypal/", include("paypal.standard.ipn.urls")),
    path("payment_failed/", views.payment_failed, name="payment_failed"),
    path("paypal/<int:member_id>/", views.payment_view, name="payment_process"),
    path("confirm/<str:transaction_id>/", views.payment_confirm, name="payment_confirm"),
]

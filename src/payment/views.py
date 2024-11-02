from django.shortcuts import render
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid # Required for generating unique transaction

def payment(request):
    return render(request, "navigation/building.html")

def payment_process(request):
    
    # Get the host
    host = request.get_host()
    
    # Create PayPal Form Dictionary
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10.00",
        "item_name": "Donation",
        "no_shipping": 2,
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": "http://{}{}".format(host, reverse("paypal-ipn")),
        "return_url": "http://{}{}".format(host, reverse("payment_success")),
        "cancel_return": "http://{}{}".format(host, reverse("payment_failed")),
    } 
    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    
    return render(request, "payment/payment.html", {"paypal_form": paypal_form})
    

def payment_success(request):
	return render(request, "payment/payment_success.html", {})

def payment_failed(request):
	return render(request, "payment/payment_failed.html", {})

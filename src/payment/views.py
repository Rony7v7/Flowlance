from django.db.models import Q
from datetime import datetime
import uuid
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from paypal.standard.forms import PayPalPaymentsForm
from project.models import ProjectMember
from .models import Transaction

def filter_transactions(request, freelancer):
    transactions = Transaction.objects.filter(freelancer=freelancer).order_by('-created_at')
    min_amount = request.GET.get("min_amount")
    max_amount = request.GET.get("max_amount")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if min_amount:
        transactions = transactions.filter(amount__gte=min_amount)
    if max_amount:
        transactions = transactions.filter(amount__lte=max_amount)
    if start_date:
        transactions = transactions.filter(created_at__date__gte=start_date)
    if end_date:
        transactions = transactions.filter(created_at__date__lte=end_date)
    
    return transactions

def create_paypal_form(request, transaction_id, paypal_email, amount, freelancer, host):
    paypal_dict = {
        "business": paypal_email,
        "amount": amount,
        "item_name": f"Pago a {freelancer.username}",
        "no_shipping": 2,
        "invoice": transaction_id,
        "currency_code": "USD",
        "notify_url": "http://{}{}".format(host, reverse("paypal-ipn")),
        "return_url": "http://{}{}".format(host, reverse("payment_confirm", args=[transaction_id])),
        "cancel_return": "http://{}{}".format(host, reverse("payment_failed")),
    }
    return PayPalPaymentsForm(initial=paypal_dict)

def create_transaction(freelancer, amount, transaction_id):
    return Transaction.objects.create(
        freelancer=freelancer,
        amount=amount,
        transaction_id=transaction_id,
        status="Pending"
    )

def payment_view(request, member_id):
    freelancer = get_object_or_404(ProjectMember, id=member_id, role='member')
    host = request.get_host()
    amount = "80.00" 
    paypal_form = None

    transactions = filter_transactions(request, freelancer.user)

    if request.method == "POST":
        paypal_email = request.POST.get("paypal_email", freelancer.user.email)
        amount = request.POST.get("amount", amount)
        transaction_id = str(uuid.uuid4())

        paypal_form = create_paypal_form(request, transaction_id, paypal_email, amount, freelancer.user, host)
        create_transaction(freelancer.user, amount, transaction_id)

    return render(request, "payment/payment.html", {
        "paypal_form": paypal_form,
        "freelancer": freelancer,
        "transactions": transactions,
        "amount": amount,
    })

def payment_confirm(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        transaction.status = "Success"
        transaction.save()
    except Transaction.DoesNotExist:
        freelancer = get_object_or_404(ProjectMember, user__email=settings.PAYPAL_RECEIVER_EMAIL).user
        transaction = Transaction.objects.create(
            freelancer=freelancer,
            amount="90.00",
            transaction_id=transaction_id,
            status="Success",
            created_at=timezone.now()
        )
    
    return render(request, "payment/payment_success.html", {"transaction": transaction})

def dashboard(request):
    return render(request, "dashboard/company_dashboard.html", {})

def payment_failed(request):
    return render(request, "payment/payment_failed.html", {})

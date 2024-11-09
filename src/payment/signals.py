# TODO: IMPLEMENT IPN SIGNALS BEFORE DEPLOYMENT
# from django.dispatch import receiver
# from paypal.standard.ipn.signals import valid_ipn_received
# from .models import Transaction

# @receiver(valid_ipn_received)
# def payment_notification(sender, **kwargs):
#     ipn_obj = sender

#     # Busca la transacción por transaction_id
#     try:
#         transaction = Transaction.objects.get(transaction_id=ipn_obj.invoice)
#     except Transaction.DoesNotExist:
#         return  # Si no existe la transacción, simplemente termina

#     # Actualiza el estado según la respuesta de PayPal
#     if ipn_obj.payment_status == "Completed":
#         transaction.status = "Success"
#     else:
#         transaction.status = "Failed"

#     transaction.save()

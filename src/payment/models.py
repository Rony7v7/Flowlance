from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)  # ID único de la transacción
    status = models.CharField(max_length=20)  # Puede ser "Success", "Failed", etc.
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la transacción

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.freelancer.username}"

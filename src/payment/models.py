from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True) 
    status = models.CharField(max_length=20)  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.freelancer.username}"

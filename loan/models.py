from django.db import models
from django.contrib.auth.models import User
import random

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    id_number = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_phone = models.CharField(max_length=15)
    employment_status = models.CharField(
        max_length=20,
        choices=[
            ('employed', 'Employed'),
            ('self_employed', 'Self Employed'),
            ('unemployed', 'Unemployed')
        ]
    )
    loan_limit = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def assign_loan_limit(self):
        loan_limits = [1000, 1500, 2000, 2500, 3000]
        self.loan_limit = random.choice(loan_limits)
        self.save()

    def calculate_processing_fee(self):
        return 0.1 * self.loan_limit

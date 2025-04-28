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
        loan_limits = [2500, 2700, 2900, 3000, 3200, 3400, 3500, 3700, 3900,
        4000, 4200, 4400, 4500, 4700, 4900,
        5000, 5200, 5400, 5500, 5700, 5900,
        6000, 6200, 6400, 6500, 6700, 6900,
        7000, 7200, 7400, 7500, 7700, 7900,
        8000, 8200, 8400, 8500, 8700, 8900,
        9000, 9200, 9400, 9500, 9700, 9900, 10000]
        self.loan_limit = random.choice(loan_limits)
        self.save()

    def calculate_processing_fee(self):
        return 0.1 * self.loan_limit

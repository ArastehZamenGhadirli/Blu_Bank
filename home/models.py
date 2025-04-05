from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)


class Account(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=10)
    amount = models.FloatField(default=0)

class BaseProfit(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Profit percentage (e.g., 5 for 5%)"
    )
    duration = models.PositiveIntegerField(help_text="Duration in days")

    def __str__(self):
        return f"{self.title} ({self.percentage}%, {self.duration} days)"


class Profit(models.Model):
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(
        to=Account, on_delete=models.CASCADE, related_name="Account_Profit"
    )
    base_profit = models.ForeignKey(BaseProfit, on_delete=models.CASCADE, null=True)



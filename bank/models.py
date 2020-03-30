from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    accountnumber = models.BigIntergerField(primaryKey=True, editable=True)
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

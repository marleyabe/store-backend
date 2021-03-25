from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.
TYPE_USER = [
    ("E", "Employee"),
    ("C", "Client"),
    ("D", "DEV"),
    ("A", "Admin")
]


class User(DjangoUser):
    
    phone = models.CharField('Phone', max_length=15)
    postalCode = models.CharField('Postal Code', null=True, max_length=9)

    typeUser = models.CharField("Type User", choices=TYPE_USER, default="C", max_length=9)
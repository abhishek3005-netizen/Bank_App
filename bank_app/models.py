from django.db import models
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    account_no = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.IntegerField()
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
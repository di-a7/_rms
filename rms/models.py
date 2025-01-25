from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=15)

class Food(models.Model):
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Table(models.Model):
   number = models.IntegerField()
   is_available = models.BooleanField(default = False)

class Order(models.Model):
   PENDING = 'P'
   COMPLETED = 'C'
   STATUS_CHOICE = {
      (PENDING, 'Pending'),
      (COMPLETED, 'Completed'),
   }
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   table = models.ForeignKey(Table, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   total_price = models.FloatField(default=1)
   status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)
   payment = models.BooleanField(default=False)

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete = models.PROTECT)
   food = models.ForeignKey(Food, on_delete= models.PROTECT)
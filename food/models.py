from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Item(models.Model):
     user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
     item_name = models.CharField(max_length=200)
     item_desc = models.CharField(max_length=200)
     item_price = models.IntegerField()
     itme_image = models.CharField(max_length=500,default="https://images.squarespace-cdn.com/content/v1/5dccbf96737b35229eaeed90/1605013441797-X97344Z3UQ0RHYH2Z49P/Placeholder_Pizza.png?format=2500w")
     
     def __str__(self):
          return self.item_name
     
     # def get_absolute_url(self):
     #      return reverse("food:detail",kwargs={"pk":self.pk})
     
     def get_absolute_url(self):
          return reverse("food:detail",kwargs={"pk":self.pk})
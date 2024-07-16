from django.db import models

# Create your models here.
class Customer(models.Model):
  creation_date = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.CharField(max_length=255)
  phone = models.CharField(max_length=10)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  province = models.CharField(max_length=255)
  country = models.CharField(max_length=125)
  
  def __str__(self):
    return self.first_name +" "+self.last_name
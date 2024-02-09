from django.db import models

#Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =models.CharField(max_length=120)
    phone =models.CharField(max_length=12)
    descc =models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.name, self.email
    # def __str__(self):
    #     return  self.email
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=150)
    author=models.CharField(max_length=150)

    def __str__(self):
        return "Book ID : "+str(self.pk)+", Book name is : "+ self.name

from django.db import models

# Create your models here.

# authentication
class Login(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.username





class customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=1000)




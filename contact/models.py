from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.BigIntegerField()
    massage = models.TextField()

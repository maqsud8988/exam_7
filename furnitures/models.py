from django.db import models

class Furnitures(models.Model):
    WhatWeDo = models.CharField(max_length=400)
    image = models.ImageField()

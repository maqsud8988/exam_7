from django.db import models

class Service(models.Model):
    AboutOurCarService = models.TextField()

    class Meta:
        app_label = 'about'
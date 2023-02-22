from django.db import models

class SetupAi(models.Model):
    text = models.CharField(max_length=100)

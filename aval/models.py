from django.db import models

class Dados(models.Model):
    Nome = models.CharField(max_length=100)

from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=100)

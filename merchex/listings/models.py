from django.db import models 

class Connection(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

class Entrer_code(models.Model):
    code = models.TextField()

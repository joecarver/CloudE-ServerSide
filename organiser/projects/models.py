from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(required=True, max_length=254)

class Project(models.Model):
    title = models.TextField(required=True)
    admin = models.ForeignKey(User)

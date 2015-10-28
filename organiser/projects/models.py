from django.db import models

# Create your models here.

class AppUser(models.Model):
    username = models.CharField(blank=False, max_length=254)

class Project(models.Model):
    title = models.TextField(blank=False)
    admin = models.ForeignKey(User)

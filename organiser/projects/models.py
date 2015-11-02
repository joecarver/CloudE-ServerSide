from django.db import models

# Create your models here.

class AppUser(models.Model):
    username = models.CharField(blank=False, max_length=254)

    def __unicode__(self):
        return self.username

class Project(models.Model):
    title = models.TextField(blank=False)
    admin = models.ForeignKey(AppUser)

    def __unicode__(self):
        return self.title + ' by: ' + self.admin.username
    

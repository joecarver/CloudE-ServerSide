from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class AppUser(models.Model):
    username = models.CharField(blank=False, max_length=254, unique=True)
    avatar = models.CharField(default='JamesCameron', max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'User ' + self.username

class Project(models.Model):
    title = models.TextField(blank=False)
    admin = models.ForeignKey(AppUser)

    def __unicode__(self):
        return self.title + ' admin by: ' + self.admin.username


def get_project_dependencies(sender, instance, **kwargs):
     #instance.product.stock -= instance.amount
     if kwargs.get('created', False):
		ProjectAssignee(proj=instance, assignee=instance.admin).save()
		Column(name="TO DO", proj=instance).save()
		Column(name="IN PROGRESS", proj=instance).save()
		Column(name="DONE", proj=instance).save()
post_save.connect(get_project_dependencies, sender=Project, dispatch_uid="smth_sensible")
  
class ProjectAssignee(models.Model):
	proj = models.ForeignKey(Project)
	assignee = models.ForeignKey(AppUser)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		#don't allow duplicate pairings
		unique_together = ['proj', 'assignee']

	def __unicode__(self):
		return self.assignee.username + ' assigned to ' + self.proj.title

class Column(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=254, blank=False)
	proj = models.ForeignKey(Project)

	def __unicode__(self):
		return self.name + " in project " + self.proj.title

class Task(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	summary = models.TextField(blank=False)
	description = models.TextField()
	proj = models.ForeignKey(Project)
	column = models.ForeignKey(Column)
	dueDate = models.DateField(blank=False)
	posInColumn = models.IntegerField(blank=False)
	dueDate = models.DateField(blank=True)

	class Meta:
		unique_together = ['column', 'posInColumn']
	def __unicode__(self):
		return self.summary #maybe add some more info

class TaskAssignee(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	tsk = models.ForeignKey(Task)
	assignee = models.ForeignKey(AppUser)

	class Meta:
		unique_together = ['tsk', 'assignee']

	def __unicode__(self):
		return self.tsk.summary + " - in project - " + self.tsk.proj.title + " - assigned to: " + self.assignee.usernameAp

class TaskRequiredSkill(models.Model):
	tsk = models.ForeignKey(Task)
	skill = models.TextField(blank=False)

	class Meta:
		unique_together = ['tsk', 'skill']

	def __unicode__(self):
		return self.skill + ' needed by ' + self.tsk.summary

class Notification(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	sender = models.ForeignKey(AppUser, related_name='%(class)s_sender')
	receiver = models.ForeignKey(AppUser, related_name='%(class)s_receiver', blank=False)
	task = models.ForeignKey(Task)
	project = models.ForeignKey(Project)
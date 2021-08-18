from django.contrib.auth.models import User
from django.db import models

# Project model
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    project_disc = models.CharField(max_length=200, default='')
    api_key = models.CharField(max_length=200)
    create_date = models.DateTimeField('Creat Date', auto_now_add=True)
    project_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.project_name

# Data label model
class prjDataLabel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    def __str__(self):
        return self.label

# Data model
class prjData(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    label = models.ForeignKey(prjDataLabel, on_delete=models.CASCADE)
    data = models.TextField()
    insert_date = models.DateTimeField('Insert Date', auto_now_add=True)
    def __str__(self):
        return self.data

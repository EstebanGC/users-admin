from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Here, we create the fields of every task. Each one will use the models library to design the type of the field.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #As we're using a relational db, we can turn on the function that allow us to delete on cascade. 
    #You know, like if there are certain amount of tasks with a shared id... if I delete that id.. all tasks related to that id will be deleted too.

    def __str__(self):
        return self.title + '- by ' + self.user.username
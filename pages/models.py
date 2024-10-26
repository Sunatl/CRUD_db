from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    name = models.CharField( max_length=50)
    due_date = models.DateField(auto_now=False)
    status = models.CharField( max_length=50)
    priority = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_active =  models.BooleanField(default=True)
    def __str__(self):
        return self.name
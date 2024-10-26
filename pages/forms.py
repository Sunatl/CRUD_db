from django import forms
from .models import *

class Tasksform(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ("name","due_date","status","priority","description","user")
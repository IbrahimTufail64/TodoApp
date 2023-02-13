from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = tasks
        fields = '__all__'
from django import forms
from django.forms import ModelForm
from .models import *
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()



class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}), label=False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)

	class Meta:
		model = Task
		fields = ['title', 'due']
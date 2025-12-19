
from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=['title','description','file','deadline','priority']

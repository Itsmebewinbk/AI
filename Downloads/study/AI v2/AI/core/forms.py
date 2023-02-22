from django import forms
from .models import SetupAi

class SetupAiForm(forms.ModelForm):
    class Meta:
        model = SetupAi
        fields = ['text']
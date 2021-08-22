from django import forms
from .models import News
class NewsForm(forms.ModelForm):
    '''News Form'''
    class Meta:
        model=News
        fields='__all__'


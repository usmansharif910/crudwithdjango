#from  django.core import validators
from django import forms
from matplotlib import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('all',)
        fields = ['name', 'email','password','comment',]
        widgets= {
            'name': forms.TextInput (attrs={'class':'form-control'}),
            'email': forms.EmailInput (attrs={'class':'form-control'}),
            'password': forms.PasswordInput (attrs={'class':'form-control'}),
            'comment': forms.TextInput (attrs={'class':'form-control'}),
        }
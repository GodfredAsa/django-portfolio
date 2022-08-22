from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2' ]
        labels ={
            'first_name': 'Name'
        }
        widgets = {
            # 'tags': forms.CheckboxSelectMultiple(),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'featured_image': forms.Media(),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.TextInput(attrs={'class': 'form-control '}),
            'password2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }  
from turtle import update
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Skill

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
            'featured_image': forms.Media(),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.TextInput(attrs={'class': 'form-control '}),
            'password2': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }  
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['name', 'username','location', 'bio', 
            'short_intro', 'profile_image','social_github', 'social_youtube', 'social_linkedin', 
            'social_website', 'social_twitter']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'location': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'bio': forms.Textarea(),
            'short_intro': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'profile_image': forms.ImageField(),
            'social_github': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'social_youtube': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'social_linkedin': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'social_website': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'social_twitter': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }  
        
        # def __init__(self, *args, **kwargs) -> None:
        #     super(ProfileForm, self).__init__( *args, **kwargs)
        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'input'})
              
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        # exclude  = ['owner']
        
        # def __init__(self, *args, **kwargs) -> None:
        #     super(SkillForm, self).__init__( *args, **kwargs)
        #     for name, field in self.fields.items():
        #         field.widget.attrs.update({'class': 'input'}) 
          
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        }  
    
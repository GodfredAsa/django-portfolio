from statistics import mode
from django.forms import ModelForm
from .models import Project,Review
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            # 'tags': forms.CheckboxSelectMultiple(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #featured_image': forms.ImageField(), #causes error 
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'demo_link': forms.TextInput(attrs={'class': 'form-control'}),
            'source_link': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),  
        }  
        
    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
        
        # you can repeat for all form fields 
        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})
        
class ReviewForm(ModelForm):
    class Meta:
        model  = Review
        fields = ['value', 'body']
        labels = { 'value': 'Place your vote',
                   'body': 'Add a comment with your vote'
        }
        
        widgets = {
            'value': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        } 
        
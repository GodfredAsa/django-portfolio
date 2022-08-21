from pydoc import describe
from unicodedata import name
from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    # topSkills = profile.skill_set.exclude(description__exact = "") # profile skill with description 
    skills = profile.skill_set.filter() # profile skill without description 
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/user-profile.html', context)
    

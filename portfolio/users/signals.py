from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
# decorator the action performed 
from django.dispatch import receiver

# signal method
# it takes in the signal method and the sender : sender is a model in this instance a profile 
# @receiver(post_save, sender = Profile)
def createProfile(sender, instance, created, **kwargs):
    print("singal trigered in here")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
            
        )
    
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    
    print("Deleting...")

# # with these 2 instances decoratoras can be used for them  used on line 44
post_save.connect(createProfile, sender=User )
post_delete.connect(deleteUser, sender= Profile)

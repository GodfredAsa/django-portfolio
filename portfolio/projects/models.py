from email.policy import default
from tkinter import CASCADE, FLAT
from django.db import models
from users.models import Profile
import uuid

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    featured_image = models.ImageField(null = True, blank = True, default ="default.jpg" )
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True) 
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['-vote_total','vote_ratio', 'created', 'title']
    
    @property   
    def reviewers(self):
        # returns a list of IDs
        queryset = self.review_set.all().values_list('owner__id', flat = True) 
        return queryset
    
    @property   
    def getVoteCount(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_count = reviews.count()
        ratio = up_votes / total_count * 100
        
        # updating the vote_total and and vote_ratio
        self.vote_total = total_count
        self.vote_ratio = ratio
        self.save()
        
        
        
class Review(models.Model):
    # ensure a user as only 1 review to a project
    VOTE_TYPE = (('up', 'Up Vote'), ('down', 'Down Vote'))
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    class Meta:
        # this list in a list tying the project and the owner ensures that 
        unique_together = [['owner', 'project']]
    
    def __str__(self) -> str:
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name

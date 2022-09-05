from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import  Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # overriding the return type of the owner from ID to object 
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many = True)
    reviews = serializers.SerializerMethodField()
    class Meta:
        model  = Project
        fields = '__all__'
        
# serializer method must starts with get_ followed by preferred name
# serializer method fields is used to calculate on a particular field   
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
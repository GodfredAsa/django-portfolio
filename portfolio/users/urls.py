from django.urls import path
from . import views

urlpatterns = [

     path('', views.profiles, name="profiles"), 
     path('login/', views.loginUser, name="login"), 
     path('register/', views.registerUser, name="register"), 
     path('account/', views.userAccount, name="account"), 
     path('logout/', views.logoutUser, name="logout"), 
     path('edit-account/', views.editAccount, name="edit-account"), 
     path('profile/<str:pk>/', views.user_profile, name="user-profile"), 
     
]

from django.urls import path
from .views import user_login,user_signup,user_logout
urlpatterns = [

    path('',user_signup,name='SignUp'),
    path('login/',user_login,name='LogIn'),
     path('logout/',user_logout,name='LogOut'),

    
]
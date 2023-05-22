"""Blog_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BlogApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.user_signup,name='SignUp'),
    path('login/',views.user_login,name='LogIn'),
    path('profile/',views.comment,name='Profile'),
    path('logout/',views.user_logout,name='LogOut'),
    path('create_post',views.create_post,name='create_post'),
    path('profile/<slug>', views.create_comment, name='create_comment'),
      path('update_post/<int:id>/', views.update_post, name='update_post'),
     path('comm/<int:id>/', views.create_comments, name='create_comments'),
       path('update_comm/<int:id>/', views.update_comment, name='update_comments'),
    #    path('post/<int:post_id>/like/', views.like_post, name='like_post'),

  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





from django.urls import path
from .views import user_post,create_post,update_post,delete_post
urlpatterns = [

    
    path('profile/',user_post,name='Profile'),
    path('create_post',create_post,name='create_post'),
    # path('profile/<slug>', views.create_comment, name='create_comment'),
      path('update_post/<int:id>/',update_post, name='update_post'),
        path('delete_post/<int:post_id>/',delete_post, name='delete_post'),
    #  path('comm/<int:id>/', views.create_comments, name='create_comments'),
    #    path('update_comm/<int:id>/', views.update_comment, name='update_comments'),


    
]
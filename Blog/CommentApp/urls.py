


from django.urls import path
from .views import create_comments,update_comment,create_comment,delete_comment
urlpatterns = [
      path('profile/<slug>', create_comment, name='create_comment'),
 path('comm/<int:id>/',create_comments, name='create_comments'),
       path('update_comm/<int:id>/',update_comment, name='update_comments'),
               path('delete_comment/<int:comm_id>/',delete_comment, name='delete_comment'),


]
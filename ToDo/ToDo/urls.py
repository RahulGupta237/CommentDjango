"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Account import views

urlpatterns = [
    path("admin/", admin.site.urls),
  
    path('',views.user_signup,name='SignUp'),
    path('login/',views.user_login,name='LogIn'),
    path('profile/',views.user_profile,name='Profile'),
    path('logout/',views.user_logout,name='LogOut'),
    # #  path('pass/',views.user_change_password,name='ChangedPassword'),
    # # path('forget/',views.user_forget_password,name='ForgetPassword'),
    path('edit/',views.user_edit_profile,name='Edit'),
    path('detail/<int:id>',views.user_detail,name='Detail'),
    path('create/', views.create_todo_list, name='create'),
    path('items/', views.create_item_list, name='items'),
    path('List_todo',views.todo_list,name='List_todo'),
    path('itms_todo',views.items_todo_list,name='items_todo'),
     path('EditTodo/<int:id>',views.edit_todo_list,name='EditTodo'),
      path('DeleteTodo/<int:id>',views.delete_todo_list,name='DeleteTodo'),
         path('EditItem/<int:id>',views.edit_items_list,name='EditItem'),
      path('DeleteItem/<int:id>',views.delete_item_list,name='DeleteItem'),
       path('add_user/',views.add_user,name='add_user'),
        path('delete_user/<int:id>',views.delete_user,name='delete_user'),
          path('edit_user/<int:id>',views.edit_user,name='edit_user'),
           path('todo_user/<int:id>',views.all_user_todoitems,name='todo_user'),
              path('items_todo_user/<int:id>',views.all_userItems_todoitems,name='items_todo_user'),
            path('admin_todo_user/<int:id>',views.admin_todo_list,name='admin_todo_user'),
              path('admin_items_todo_user/<int:id>',views.admin_items_todo_list,name='admin_items_todo_user'),
               path('activate/<int:id>',views.activate_deactivate_todo_list,name='activate'),
                path('activate/todo_user/<int:id>',views.all_user_todoitems,name='activate_todo'),

    
    

]


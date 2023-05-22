from django.shortcuts import render,redirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect, get_object_or_404
from BlogApp.models import CustomUser as User,Post,Comment
from BlogApp.forms import CustomUserCreationForm, UserLogin, PostForm,CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count,F
def comment(request):
    user_detail = Post.objects.all()
    # yx=Post.objects.annotate(publish=Count('Comment'))
    x = Post.objects.annotate(comment_count=Count('Comment')).annotate(published=F('publish')).order_by('-id')
    comment=Comment.objects.all()
    return render(request,"post.html",context={"userD":x,"comment":comment})




def user_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        group_name = request.POST.get('email')
        print(group_name)
        if form.is_valid():
            print("form validation")
            user = form.save()
            group_name = request.POST.get('group')
            print(group_name)
            if group_name == 'superuser':
                user.is_superuser = True
                user.is_staff = True
            user.save()
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                print("i am group user")
            except:
                print("Hi i am normal user")
            finally:
                messages.success(request,"Suceessfully account created")
                return HttpResponseRedirect('/login/')  # Replace "home" with your desired URL after signup
        else:
            print("outside form validation")
    else:
       if request.user.is_authenticated:
           return redirect("Profile")
       else:
           form = CustomUserCreationForm()
    return render(request, 'UserApp/signup.html', {'forms': form})




def user_login(request):

    fm=UserLogin()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request,email=email, password=password)
        print(user)
        if user is not None:
            print("i am login")
            # Authentication successful, log the user in
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            print("i am login")
            print(request.user)
            messages.success(request,"successfully login")
            return HttpResponseRedirect('/profile/')
            # return redirect('home') # Redirect to home page or any other page
        else:
            # Authentication failed, show an error message
            print("you are fake")
            messages.error(request,f"wrong credential for {email}")
    else:
         
            fm=UserLogin()
            print("i am user")
    return render(request,"UserApp/login.html",{"forms":fm})
    return render(request, 'login.html')






@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



@login_required
def create_post(request):
    form = PostForm(request.POST)
    
    if request.method == 'POST':
    
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.author = request.user
            todo_list.save()
            print("i am here")

            messages.success(request,"todolist Item successfully created")
            return redirect('Profile')
    
    return render(request, 'UserApp/item_list_todo.html', {'forms': form})
from django.http import JsonResponse
@login_required
def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_text = request.POST.get('comment_text')
    print("slug",slug)
    if comment_text:
        comment = Comment.objects.create(
            post=post,
            created_by=request.user,
              comment_text=comment_text
        )
        comment.save()
       
    return redirect('Profile')

@login_required
def create_comments(request,id):
    post = get_object_or_404(Post,id=id)
  
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted successfully.')

            return redirect('Profile')
        else:
            messages.error(request, 'There was an error posting your comment. Please try again.')

        return redirect('Profile')
    else:
        form = CommentForm()


    return render(request, 'UserApp/create_todo_list.html', {'forms': form})

from django.utils import timezone
@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    print("i am here",post.slug)

    if request.user == post.author:
        if request.method == 'POST':
            post.title = request.POST['title']
            post.description = request.POST['content']
            post.updated_at = timezone.now()
            post.is_edited=True
            post.save()
            return redirect('Profile')
       
    else:
        return redirect('Profile')

def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    print("i am here",comment.comment_text)

    if request.user == comment.created_by:
        if request.method == 'POST':
            print(request.POST['content'])
            print("i am inside comment")
            
            comment.comment_text = request.POST['content']
            comment.updated_at = timezone.now()
            # post.is_edited=True
            comment.save()
            return redirect('Profile')
       
    else:
        return redirect('Profile')



# @login_required
# def like_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     like, created = PostLike.objects.get_or_create(user=request.user, post=post)
#     if not created:
#         like.delete()

#     post.like_count = post.likes.count()
#     post.save()
#     return redirect('Profile')
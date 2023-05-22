from django.shortcuts import render,redirect
from django.shortcuts import render,redirect, get_object_or_404
from PostApp.models import Post,Category
from account.models import CustomUser as User

from PostApp.forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


from CommentApp.models import Comment
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count,F
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_post(request):
    group=Category.objects.all()
    user_detail = Post.objects.all()
    # yx=Post.objects.annotate(publish=Count('Comment'))
    x = Post.objects.annotate(comment_count=Count('Comment')).annotate(published=F('publish')).order_by('-id')
    comment=Comment.objects.all()
    return render(request,"post_comment/post.html",context={"userD":x,"comment":comment,"cat":group})










@login_required
def create_post(request):
    form = PostForm(request.POST)
    
    if request.method == 'POST':
    
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.author = request.user
            todo_list.save()
            print("i am here")

            messages.success(request,"Share publically Post successfully ")
            return redirect("PostApp:Profile")
    
    return render(request, 'post_template/item_list_todo.html', {'forms': form})
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    print("i am here",post.slug)

    if request.user == post.author:
        if request.method == 'POST':
            Category_title = request.POST['my_dropdown']
            print(Category)
            my_object = Category.objects.get(title=Category_title)
            print(my_object.id)
            # try:
            #     my_object = Category.objects.get(title=Category)
            #     print(my_object)
            # except ObjectDoesNotExist:
            #         print("rahulll")
            post.category=my_object



            post.title = request.POST['title']
            post.description = request.POST['content']
            post.updated_at = timezone.now()
            post.is_edited=True
            post.save()
            return redirect("PostApp:Profile")
       
    else:
        return redirect("PostApp:Profile")

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("PostApp:Profile")
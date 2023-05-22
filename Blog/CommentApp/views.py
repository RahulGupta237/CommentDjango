from django.shortcuts import render,redirect

from django.shortcuts import render,redirect, get_object_or_404
from account.models import CustomUser as User
from CommentApp.models import Comment
from PostApp.models import Post
from CommentApp.forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect

from rest_framework import status



from django.utils import timezone

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
       
    return redirect("PostApp:Profile")

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

            return redirect("PostApp:Profile")
        else:
            messages.error(request, 'There was an error posting your comment. Please try again.')

        return redirect("PostApp:Profile")
    else:
        form = CommentForm()


    return render(request, 'UserApp/create_todo_list.html', {'forms': form})


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
            comment.is_edited=True
            comment.save()
            messages.success(request, f'Your comment  successfully. edited')
            return redirect('PostApp:Profile')
       
    else:
        return redirect('PostApp:Profile')



def delete_comment(request, comm_id):
    comm = Comment.objects.get(id=comm_id)
    comm.delete()
    messages.success(request, 'Your comment  successfully deleted.')
    return redirect("PostApp:Profile")
    
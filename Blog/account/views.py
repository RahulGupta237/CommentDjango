from django.shortcuts import render,redirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect, get_object_or_404
from account.forms import CustomUserCreationForm, UserLogin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_protect

@csrf_protect
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
           return redirect("PostApp:Profile")
       else:
           form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'forms': form})



@csrf_protect
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
            return redirect("PostApp:Profile")
            # return redirect('home') # Redirect to home page or any other page
        else:
            # Authentication failed, show an error message
            print("you are fake")
            messages.error(request,f"wrong credential for {email}")
    else:
         
            fm=UserLogin()
            print("i am user")
    return render(request,"account/login.html",{"forms":fm})
    return render(request, 'login.html')






@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


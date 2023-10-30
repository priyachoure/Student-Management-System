from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def HOME(request):
    return render(request,'hod/home.html')

"""
@login_required: This is a decorator in Django used to restrict access to a particular view
(in this case, the HOME view) to authenticated users only. If a user is not authenticated 
(i.e., they are not logged in), they will be redirected to the login page. 
You can specify the login URL as an argument to the decorator, which is login_url='/ ' in this case."""
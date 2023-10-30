from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser


def Base(request):
    return render(request, "base.html")


def Login(request):
    return render(request, 'login.html')


def dologin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))

    if user != None:
        login(request, user)
        user_type = user.user_type
        if user_type == '1':
            # return HttpResponse("this is HOD page")
            return redirect("hod_home")
        elif user_type == '2':
            return HttpResponse('This is staff page')
        elif user_type == '3':
            return HttpResponse('this is student page')
        else:
            # message
            messages.error(request, "Email and Password are Invalid!")
            return redirect('login')
    else:
        # messages
        messages.error(request, "Email and Password are Invalid!")
        return redirect('login')


def dologout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)
    # print(user)  # to find out who is user.

    context = {
        "user": user,
    }
    return render(request, 'profile.html')


def profile_update(request):

    profile_pic = request.FILES.get("profile_pic")
    firstname = request.POST.get('first_name')
    lastname = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    # print(profile_pic,firstname,lastname,email,username,password)
    # try:
    #     CustomUser.
    # except:

    return render(request, 'profile.html')

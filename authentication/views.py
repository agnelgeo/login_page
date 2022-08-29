
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    
    return render(request,"index.html")

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist, Try another")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"E-mail already registered")
            return redirect('home')

        if len(username)>10:
            messages.error(request, 'Username must be less than 10 characters')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,"Passwords didn't match")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,'username must be alphanumeric')
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,'Your account was created sucessfully')

        return redirect('home')


    return render(request,"signup.html")

def signin(request):

    if request.method == 'POST':
        username =  request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username,password = pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,'index.html', {"fname":fname})
        else:
            messages.error(request,'incorrect credintials')
            return redirect('home')

    return render(request,"signin.html")

def signout(request):

    logout(request)
    messages.success(request, "loggedout sucessfully")
    return redirect('home')

def forgotpass(request):

    return render(request,"forgot.html")
    
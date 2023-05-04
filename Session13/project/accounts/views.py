from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile
from .models import User

# Create your views here.
def home(request):
    return render(request, "accounts/home.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        exist_user = User.objects.filter(username=username)
        
        if exist_user:
            user_error = "해당 유저가 이미 존재합니다."
            return render(request, 'accounts/signup.html', {'user_error': user_error})

        new_user = User.objects.create_user(
            username = username,
            password = password
        )

        auth.login(request, new_user)
        return redirect('blog:home')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:home')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'blog/home.html')




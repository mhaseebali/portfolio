from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm

# Create your views here.

# def req(request):
#     return render(request, 'home.html', {
#       "sometext": "challenge_text"
#     })




def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')



    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')

    return render(request, 'myapp/login_register.html')
    


def logOutUser(request):
    logout(request)
    messages.error(request, 'user was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form1 = CustomUserCreationForm()

    if request.method == 'POST':
        form1 = CustomUserCreationForm(request.POST)
        if form1.is_valid():
            user = form1.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, 'An error was occurred during registration')

    context = {'page': page, 'form': form1}
    return render(request, 'myapp/login_register.html', context)


def req1(request):
    return render(request, 'myapp/base.html')

def req2(request):
    return render(request, 'myapp/designs.html')




      
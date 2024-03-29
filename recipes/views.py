from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'home.html')


# def signup(request):
#     return render(request, "auth/signup.html")


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, "auth/signup.html", {'form':form})
        
    else:
        form = UserCreationForm()
        return render(request, "auth/signup.html", {'form':form})


def login_view(request):

    if request.user.is_authenticated:
        return redirect('root')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('root')
        
        else:
            return render(request, "auth/login.html", {'form':form})
        
    else:
        form = AuthenticationForm()
        return render(request, "auth/login.html", {'form':form})


def log_out(request):
    logout(request)
    return redirect('root')


def home(request):
    return render(request, "home")


def about(request):
    return render(request, "about")


def contact(request):
    return render(request, "contact")


def dashboard(request):
    return render(request, "dashboard")


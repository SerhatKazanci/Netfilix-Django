from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
# Create your views here.
def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def userRegister(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def userLogout(request):
    logout(request)
    return redirect('index')

def createProfile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.owner = request.user
            profile.save()
            messages.success(request, 'Profiliniz başarıyla oluşturuldu.')
            return redirect('profiles')
    
    context = {
        'form':form
    }

    return render(request, 'create-profile.html', context)

def userProfile(request):
    profile = request.user
    context = {
        'profile':profile
    }
    return render(request, 'hesap.html', context)

def userDelete(request):
    profile = request.user
    profile.delete()
    return redirect('index')
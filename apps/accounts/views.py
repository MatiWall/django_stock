from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .forms import signupForm, editProfileForm

# Create your views here.



def userSignup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/home/')
    else: 
        form = signupForm()
        return render(request,'accounts/signup.html', {'form' : form} )


def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        
        if form.is_valid():

            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/home/')

    elif request.method == 'GET':
        form = AuthenticationForm()
        

    return render(request, 'accounts/login.html', {'form' : form})

def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/accounts/login/')

    pass


def userProfile(request):

    return render(request, 'accounts/profile.html', {'user': request.user})

def userProfileEdit(request):
    if request.method == 'POST':
        form = editProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
    else:
        form = editProfileForm(instance = request.user)
    return render(request, 'accounts/editProfile.html', {'form': form})

def userChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile/')
        else:
            return redirect('/profile/changePassword/')
    else:
        form = PasswordChangeForm(user = request.user)
    
    return render(request, 'accounts/changePassword.html', {'form': form })


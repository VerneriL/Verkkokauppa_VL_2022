from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
        'title': 'register'
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)        
    context = {
        'title': 'my profile',
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)

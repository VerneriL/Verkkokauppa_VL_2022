from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FeedBackForm



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
    context = {
    'title': 'my profile',
    }
    return render(request, 'users/profile.html', context)


@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)               
    context = {
        'title': 'update',
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/update.html', context)


@login_required
def contact(request):
    if request.method == 'POST':
        feedback_form = FeedBackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
            messages.success(request, f'Thank you for your feedback!')
            return redirect('profile-page')
    else:
        feedback_form = FeedBackForm()
    context = {
        'title': 'Contact us',
        'feedback_form': feedback_form,
    }        
    return render(request, 'users/contact.html', context)
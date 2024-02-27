from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileEditForm, UserPasswordChangeForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def aboutus(request):
    return render(request, 'home/aboutus.html')

def location(request):
    return render(request, 'home/location.html')


@login_required
def user_profile_edit(request):
    if request.method == 'POST':
        if 'profile_submit' in request.POST:  # Check if profile update form is submitted
            user_form = UserProfileEditForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('user_profile_edit')
            else:
                messages.error(request, 'Please correct the errors in the profile form.')

        elif 'password_submit' in request.POST:  # Check if password change form is submitted
            password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Prevents logout
                messages.success(request, 'Your password was successfully updated!')
                return redirect('user_profile_edit')
            else:
                messages.error(request, 'Please correct the errors in the password form.')

    else:
        user_form = UserProfileEditForm(instance=request.user)
        password_form = UserPasswordChangeForm(user=request.user)
    
    return render(request, 'account/user_profile_edit.html', {
        'user_form': user_form,
        'password_form': password_form
    })

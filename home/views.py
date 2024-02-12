from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        user_form = UserProfileEditForm(request.POST, instance=request.user)
        password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if user_form.is_valid() and (not password_form.data['old_password'] or password_form.is_valid()):
            user_form.save()
            if password_form.data['old_password']:  # Checks if the password fields were filled
                password_form.save()
                messages.success(request, 'Your password was successfully updated!')
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_profile_edit')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserProfileEditForm(instance=request.user)
        password_form = UserPasswordChangeForm(user=request.user)
    return render(request, 'account/user_profile_edit.html', {
        'user_form': user_form,
        'password_form': password_form
    })

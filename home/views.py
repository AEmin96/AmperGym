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
        user_form = UserProfileEditForm(request.POST, instance=request.user)
        password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            user = password_form.save()  # Save the form and get the updated user instance
            
            # Update session to prevent logging out the user after password change
            update_session_auth_hash(request, user)
            
            if request.is_ajax():
                return JsonResponse({'success': True, 'message': 'Your profile and password were successfully updated!'}, status=200)
            else:
                messages.success(request, 'Your profile and password were successfully updated!')
                return redirect('user_profile_edit')
        else:
            errors = {**user_form.errors, **password_form.errors}
            if request.is_ajax():
                return JsonResponse({'success': False, 'errors': errors}, status=400)
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserProfileEditForm(instance=request.user)
        password_form = UserPasswordChangeForm(user=request.user)
    
    return render(request, 'account/user_profile_edit.html', {
        'user_form': user_form,
        'password_form': password_form
    })
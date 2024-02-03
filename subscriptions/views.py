from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def subscriptions(request): 
    return render(request, 'subscriptions/subscriptions.html')

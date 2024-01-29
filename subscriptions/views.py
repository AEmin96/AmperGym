from django.shortcuts import render

# Create your views here.
def subscriptions(request):
    return render(request, 'subscriptions/subscriptions.html')

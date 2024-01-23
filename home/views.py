from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def aboutus(request):
    return render(request, 'home/aboutus.html')

def location(request):
    return render(request, 'home/location.html')

def testimonials(request):
    return render(request, 'home/testimonials.html')
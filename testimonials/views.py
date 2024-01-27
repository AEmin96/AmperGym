from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial


def testimonials(request):
    return render(request, 'testimonials.html')

def add_testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/add_testimonial.html', {'form': form})

def testimonial_list_view(request):
    testimonials = Testimonial.objects.all()


    for testimonial in testimonials:
        testimonial.filled_stars = range(testimonial.rating)
        testimonial.empty_stars = range(5 - testimonial.rating)

    return render(request, 'testimonials/testimonials.html', {'testimonials': testimonials})
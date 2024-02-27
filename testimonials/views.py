from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial


def testimonials(request):
    return render(request, 'testimonials.html')

def add_testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            # If user is authenticated, set the name field to the username
            if request.user.is_authenticated:
                form.instance.name = request.user.username
            form.save()
            return redirect('testimonials')
    else:
        # If user is authenticated, initialize the form with the name field pre-filled
        if request.user.is_authenticated:
            form = TestimonialForm(initial={'name': request.user.username})
        else:
            form = TestimonialForm()

    return render(request, 'testimonials/add_testimonial.html', {'form': form})

def testimonial_list_view(request):
    rating_filter = request.GET.get('rating', None)

    if rating_filter:
        testimonials = Testimonial.objects.filter(rating=rating_filter)
    else:
        testimonials = Testimonial.objects.all()

    # Order testimonials by the newest posted date and time
    testimonials = testimonials.order_by('-created_at')

    for testimonial in testimonials:
        testimonial.filled_stars = range(testimonial.rating)
        testimonial.empty_stars = range(5 - testimonial.rating)

    return render(request, 'testimonials/testimonials.html', {'testimonials': testimonials})

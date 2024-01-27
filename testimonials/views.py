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
            return redirect('testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/add_testimonial.html', {'form': form})

def testimonial_list_view(request):
    rating_filter = request.GET.get('rating', None)

    # Retrieve all testimonials or filter by star rating
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

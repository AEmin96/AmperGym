from django.urls import path
from .views import testimonial_list_view, add_testimonial_view
urlpatterns = [
    path('', testimonial_list_view, name='testimonials'),
    path('testimonials/', testimonial_list_view, name='testimonial_list'),
    path('add_testimonial/', add_testimonial_view, name='add_testimonial'),
]

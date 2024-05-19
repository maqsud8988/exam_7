from django.shortcuts import render
from django.views import View
from .models import Testimonial

class TestimonialView(View):
    def get(self, request):
        testimonial = Testimonial.objects.all()
        contexts = {
            "testimonial": testimonial
        }
        return render(request, "testimonial.html", contexts)


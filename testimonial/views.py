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

    # def post(self, request):
    #     search = request.POST.get("search")
    #     testimonial = Testimonial.objects.filter(name__icontains=search)
    #     contexs = {
    #         "testimonial": testimonial
    #     }
    #     return render(request, "testimonial.html", contexs)
    #



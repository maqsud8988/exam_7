from django.shortcuts import render
from django.views import View
from .models import Service

class AboutView(View):
    def get(self, request):
        service = Service.objects.first()
        # print("-----------------------------------", service)
        contexs = {
            "service": service
        }
        return render(request, "about.html", contexs)


from django.shortcuts import render, redirect
from django.views import View
from about.models import Service
from django.contrib.auth import authenticate

class LandingView(View):
    def get(self, request):
        if not authenticate(request):
            return redirect('login')
        service = Service.objects.all()
        context = {
            "services": service
        }
        return render(request, "index.html", context)

class LandingView(View):
    def get(self, request):
        service = Service.objects.all()
        context = {
            "services": service
        }
        return render(request, "index.html", context)


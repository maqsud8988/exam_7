from django.shortcuts import render
from django.views import View
from .models import Furnitures

class FurnituresView(View):
    def get(self, request):
        furnitures = Furnitures.objects.all()
        contexs = {
            "furnitures": furnitures
        }
        return render(request, "furnitures.html", contexs)

    def post(self, request):
        search = request.POST.get("search")
        furnitures = Furnitures.objects.filter(name__icontains=search)
        contexs = {
            "furnitures": furnitures
        }
        return render(request, "furnitures.html", contexs)
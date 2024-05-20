from django.shortcuts import render
from django.views import View
from .models import Contact

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        search = request.POST.get("search")
        contact = Contact.objects.filter(name__icontains=search)
        contexs = {
            "contact": contact
        }
        return render(request, "contact.html", contexs)
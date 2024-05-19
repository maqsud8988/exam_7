from django.urls import path
from .views import FurnituresView


urlpatterns = [
    path("", FurnituresView.as_view(), name="furnitures"),
]

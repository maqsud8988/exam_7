from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import FurnituresApiViewSet

router = DefaultRouter()
router.register("furnitures", viewset=FurnituresApiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]

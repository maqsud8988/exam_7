from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import FurnituresApiViewSet, AboutApiViewSet, ContactApiViewSet, TestimonialApiViewSet

router = DefaultRouter()
router.register("about", viewset=AboutApiViewSet)
router.register("contact", viewset=ContactApiViewSet)
router.register("furnitures", viewset=FurnituresApiViewSet)
router.register("testimonial", viewset=TestimonialApiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token),
]

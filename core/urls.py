from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('contact/', include('contact.urls')),
    path('', include('home.urls')),
    path("about/", include('about.urls')),
    path("furnitures/", include('furnitures.urls')),
    path("testimonial/", include('testimonial.urls')),
    path("api/", include('api.urls')),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

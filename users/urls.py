# from django.urls import path
# from .views import UserRegisterView, UserLoginView, UserLogOutView
#
#
# urlpatterns = [
#     path("register/", UserRegisterView.as_view(), name="register"),
#     path("login/", UserLoginView.as_view(), name="login"),
#     path("logout/", UserLogOutView.as_view(), name="logout")
# ]
from django.urls import path
from .views import user_register, user_login, user_logout

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

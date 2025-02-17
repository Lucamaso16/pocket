from django.urls import path
from .views import register, CustomLoginView, user_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', user_logout, name='logout'),
]

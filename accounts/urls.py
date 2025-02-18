from django.urls import path
from .views import register, CustomLoginView, user_logout, profile_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
]

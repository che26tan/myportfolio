from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.signup, name='signup'),
]
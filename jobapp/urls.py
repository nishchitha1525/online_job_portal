from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alt'),  # Add this line
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('jobs/', views.jobs, name='jobs'),
    path('apply/', views.apply, name='apply'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('change-password/', views.change_password, name='change_password'),
]
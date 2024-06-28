from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', LogoutView.as_view(template_name='authentication/logout.html'), name='logout'),
    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('doctor_dashboard/', views.doctor_view, name='doctor_dashboard'),
    path('patient_dashboard/', views.patient_view, name='patient_dashboard'),
]

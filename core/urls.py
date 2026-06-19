from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enquire/', views.submit_enquiry, name='submit_enquiry'),
    path('brochure/', views.download_brochure, name='download_brochure'),
    path('success/', views.success, name='success'),
    path('api/courses/', views.courses_api, name='courses_api'),
]

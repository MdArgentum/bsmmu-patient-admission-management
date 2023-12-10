from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient_admission/', views.patient_admission, name='patient_admission'),
    path('admited_patient/', views.admited_patient, name='admited_patient'),
    path('old_patient/', views.old_patient, name='old_patient'),
    path('contact/', views.contact, name='contact'),

    path('realised_patient/<int:pk>/', views.realised_patient, name='realised_patient'),
    path('patient_single/<int:pk>/', views.patient_single, name='patient_single'),
    path('generate-pdf/<int:pk>/', views.generate_pdf, name='generate_pdf'),
    
]

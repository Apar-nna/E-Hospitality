from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient_update'),

    path('medical-records/create/', views.MedicalRecordCreateView.as_view(), name='medical_record_create'),
    path('medical-records/<int:pk>/update/', views.MedicalRecordUpdateView.as_view(), name='medical_record_update'),

    path('appointments/create/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment_update'),

    path('treatment-plans/create/', views.TreatmentPlanCreateView.as_view(), name='treatment_plan_create'),
    path('treatment-plans/<int:pk>/update/', views.TreatmentPlanUpdateView.as_view(), name='treatment_plan_update'),
]

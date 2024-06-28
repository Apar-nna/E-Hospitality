# authentication/patient/urls.py
from django.urls import path
from . import views
from .views import appointment_create, AppointmentListView, AppointmentRescheduleView, MedicalRecordListView, \
    MedicalRecordDetailView, MedicalRecordCreateView, MedicalRecordUpdateView, BillingCreateView, PaymentCreateView, \
    InsuranceDetailView, InsuranceCreateView, InsuranceUpdateView
app_name = 'patient'
urlpatterns = [
    path('appointment/', appointment_create, name='appointment'),
    path('appointments/', AppointmentListView.as_view(), name='appointments'),
    path('appointment/reschedule/<int:pk>/', AppointmentRescheduleView.as_view(), name='appointment-reschedule'),
    path('appointment/cancel/<int:pk>/', views.cancel_appointment, name='appointment-cancel'),
    path('medical-records/', MedicalRecordListView.as_view(), name='medical-record-list'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('medical-records/new/', MedicalRecordCreateView.as_view(), name='medical-record-create'),
    path('medical-records/<int:pk>/update/', MedicalRecordUpdateView.as_view(), name='medical-record-update'),
    path('billing/create/', views.BillingCreateView.as_view(), name='billing-create'),
    path('payment/create/<int:pk>/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payments/', views.PaymentListView.as_view(), name='payments'),
    path('insurance/', InsuranceDetailView.as_view(), name='insurance-detail'),
    path('insurance/create/', InsuranceCreateView.as_view(), name='insurance-create'),
    path('insurance/update/', InsuranceUpdateView.as_view(), name='insurance-update'),


    # Add more URLs as needed
]

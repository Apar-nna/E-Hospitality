from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .models import Patient, MedicalRecord, Appointment, TreatmentPlan
from .forms import PatientForm, MedicalRecordForm, AppointmentForm, TreatmentPlanForm

class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = '/patients/'  # Redirect to patient list

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = '/patients/'  # Redirect to patient list

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_record_form.html'
    success_url = '/medical-records/'  # Redirect to medical record list

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient  # Assuming patient is linked to user
        return super().form_valid(form)

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_record_form.html'
    success_url = '/medical-records/'  # Redirect to medical record list

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = '/appointments/'  # Redirect to appointment list

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient  # Assuming patient is linked to user
        return super().form_valid(form)

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = '/appointments/'  # Redirect to appointment list

class TreatmentPlanCreateView(CreateView):
    model = TreatmentPlan
    form_class = TreatmentPlanForm
    template_name = 'treatment_plan_form.html'
    success_url = '/treatment-plans/'  # Redirect to treatment plan list

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient  # Assuming patient is linked to user
        return super().form_valid(form)

class TreatmentPlanUpdateView(UpdateView):
    model = TreatmentPlan
    form_class = TreatmentPlanForm
    template_name = 'treatment_plan_form.html'
    success_url = '/treatment-plans/'  # Redirect to treatment plan list


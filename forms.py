from django import forms
from .models import Patient, MedicalRecord, Appointment, TreatmentPlan

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['date_of_birth', 'contact_info']  # Add more fields as needed

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'medications', 'allergies', 'treatment_history']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'purpose']

class TreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = ['plan_description', 'start_date', 'end_date']


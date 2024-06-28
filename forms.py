from django import forms
from .models import Appointment, MedicalRecord, Billing, Payment, Insurance


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Appointment
        fields = ['department', 'appointment_date', 'appointment_time', 'description']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'medications', 'allergies', 'treatment_history']

class BillingForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Billing
        fields = ['invoice_number', 'amount', 'due_date']

class PaymentForm(forms.ModelForm):
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    cvv = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'type': 'text'}))

    class Meta:
        model = Payment
        fields = ['amount_paid', 'expiry_date', 'cvv']

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['provider_name', 'policy_number', 'coverage_details']



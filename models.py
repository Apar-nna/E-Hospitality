from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

class Appointment(models.Model):
    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('General', 'General'),
    ]

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Rescheduled', 'Rescheduled'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='General')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    rescheduled_date = models.DateField(blank=True, null=True)
    rescheduled_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} in {self.department}"


class MedicalRecord(models.Model):
    DIAGNOSIS_CHOICES = [
        ('Blood Analysis', (
            ('blood_count', 'Blood Count'),
            ('glucose_tolerance_test', 'Glucose Tolerance Test'),
            ('enzyme_analysis', 'Enzyme Analysis')
        )),
        ('Angiography', (
            ('cerebral_angiography', 'Cerebral Angiography'),
        )),
        ('Brain Scanning', (
            ('echoencephalography', 'Echoencephalography'),
            ('magnetoencephalography', 'Magnetoencephalography'),
            ('pneumoencephalography', 'Pneumoencephalography')
        )),
        ('Skin Test', (
            ('patch_test', 'Patch Test'),
            ('schick_test', 'Schick Test'),
            ('tuberculin_test', 'Tuberculin Test')
        )),
    ]

    diagnosis = models.CharField(max_length=255, choices=DIAGNOSIS_CHOICES)
    medications = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    treatment_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='medical_records')

    def __str__(self):
        return f"Medical record for {self.patient.username}"

class Billing(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"Billing for {self.patient.username}: Invoice {self.invoice_number}"

class Payment(models.Model):
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount_paid} for {self.billing}"

class Insurance(models.Model):
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=100)
    coverage_details = models.TextField(blank=True)

    def __str__(self):
        return f"Insurance for {self.patient.username}"




